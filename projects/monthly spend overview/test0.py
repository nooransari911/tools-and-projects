import openpyxl
from google.cloud import storage
from google.cloud import bigquery
import datetime
import pandas as pd
import plotly.express as px
from flask import Flask, render_template
import os, json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# BigQuery configuration
BQ_PROJECT = os.environ.get('BQ_PROJECT')  # Fetch from environment
BQ_DATASET = os.environ.get('BQ_DATASET')  # Fetch from environment

# Google Cloud Storage configuration
GCS_BUCKET = os.environ.get('GCS_BUCKET')  # Fetch from environment

# Function to process the latest statement from GCS
def process_latest_statement():
    """Cloud Function triggered by a file upload to GCS."""

    # 1. Get the latest .xlsx file from GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(GCS_BUCKET)
    blobs = bucket.list_blobs()
    latest_file = None
    latest_timestamp = datetime.datetime.min
    for blob in blobs:
        if blob.name.endswith('.xlsx'):
            month_str, year_str = blob.name[:-5].split('-')
            month_num = datetime.datetime.strptime(month_str, '%b').month
            timestamp = datetime.datetime(int(year_str), month_num, 1)
            if timestamp > latest_timestamp:
                latest_timestamp = timestamp
                latest_file = blob

    if latest_file is None:
        print("No .xlsx files found in the bucket.")
        return

    # 2. Download the latest file
    latest_file.download_to_filename('statement.xlsx')

    # 3. Process statement data
    workbook = openpyxl.load_workbook('statement.xlsx')
    sheet = workbook.active

    # Identify relevant columns
    date_column = None
    payee_column = None
    withdrawal_column = None
    deposit_column = None
    for i, col in enumerate(sheet[1]):  # Check header row
        if col.value == 'Date':
            date_column = i
        elif col.value == 'Narration':
            payee_column = i
        elif col.value == 'Withdrawal Amt.':
            withdrawal_column = i
        elif col.value == 'Deposit Amt.':
            deposit_column = i

    if any(col is None for col in [date_column, payee_column, withdrawal_column, deposit_column]):
        print("Could not find all required columns: Date, Narration, Withdrawal Amt., Deposit Amt.")
        return

    transactions = []
    for row in sheet.iter_rows(values_only=True):
        # Skip header row
        if row[0] is None:
            continue

        payee = row[payee_column]
        if "UPI-" in payee:
            payee = payee.replace("UPI-", "")
        payee = payee[:20]  # Limit to 20 characters

        transaction = {
            "date": row[date_column],
            "payee": row[payee_column][:20],
            "withdrawal_amt": row[withdrawal_column],
            "deposit_amt": row[deposit_column],
        }
        transactions.append(transaction)

    transactions = transactions[1:]
    transactions_json = json.dumps(transactions, indent=4)
    print(f"{transactions_json}\n\n\n\n")


    # 4. Save data to BigQuery
    client = bigquery.Client(project=BQ_PROJECT)  # Default credentials should be used

    # Create the dataset if it doesn't exist
    dataset_ref = client.dataset(BQ_DATASET)
    client.create_dataset(dataset_ref, exists_ok=True)  # Create if doesn't exist

    # Create the table if it doesn't exist
    table_ref = dataset_ref.table('transactions')

    # Define schema for the table
    schema = [
        bigquery.SchemaField("date", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("payee", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("withdrawal_amt", bigquery.enums.SqlTypeNames.FLOAT),
        bigquery.SchemaField("deposit_amt", bigquery.enums.SqlTypeNames.FLOAT),
    ]

    table = bigquery.Table(table_ref, schema=schema)
    # Create the table using the defined schema
    #table = client.create_table(table, exists_ok=True)  # Use client.create_table() directly


    errors = client.insert_rows_json (table_ref, transactions)
    if errors == []:
        print("Data loaded successfully")
    else:
        print(f"Errors: {errors}")


"""query viz = f
            SELECT payee, SUM(withdrawal_amt) AS total_spent, SUM(deposit_amt) AS total_deposited
            FROM `{BQ_PROJECT}.{BQ_DATASET}.transactions`
            WHERE CAST(SUBSTR(date, 4, 2) AS INT64) = CAST(SUBSTR("{month}", 4, 2) AS INT64)
                AND CAST(SUBSTR(date, 7, 2) AS INT64) = CAST(SUBSTR("{month}", 1, 2) AS INT64)
            GROUP BY payee
        """


def viz_data (query):
    # Query BigQuery for the requested month's data
    client = bigquery.Client(project=BQ_PROJECT)

    query_job = client.query_and_wait(query)
    results = query_job

    data = [dict(row) for row in results]
    df = pd.DataFrame(data)
    # print (f"\n\nDf is:\n{df.to_string()}")

    df_spending = df.sort_values(by='total_spent', ascending=False)
    df_deposits = df.sort_values(by='total_deposited', ascending=False)
    df_spending = df_spending.dropna(subset=['total_spent'])  # Drop rows with null in total_spent
    df_deposits = df_deposits.dropna(subset=['total_deposited'])  # Drop rows with null in total_deposited

    FIG_WIDTH = 1000
    FIG_HEIGHT = 700
    # Create pie chart for spending
    fig_pie_spending = px.pie(
        df_spending,
        names='payee',
        values='total_spent',
        title=f"Spending Breakdown"
    )
    fig_pie_spending.update_layout(width=FIG_WIDTH, height=FIG_HEIGHT)
    # Create bar chart (you can use either df_spending or df_deposits)
    fig_bar = px.bar(df_spending, x="payee", y="total_spent", title=f"Spending by Payee")
    fig_bar.update_layout(width=FIG_WIDTH, height=FIG_HEIGHT)
    fig_bar.update_xaxes(tickangle=45)

    # Convert charts to HTML
    pie_chart_spending = fig_pie_spending.to_html(full_html=False)
    bar_chart = fig_bar.to_html(full_html=False)

    df_spending = df_spending.drop('total_deposited', axis=1)
    df_deposits = df_deposits.drop('total_spent', axis=1)
    df_sp_html = df_spending.to_html(classes='table table-striped', index=False)
    df_de_html = df_deposits.to_html(classes='table table-striped', index=False)

    return render_template('index.html',
                           pie_chart_spending=pie_chart_spending, bar_chart=bar_chart,
                           df_sp_html=df_sp_html, df_de_html=df_de_html)






# Function to generate visualizations for the current month
@app.route('/')
def visualize_current_month():
    # Get the current month
    current_month = datetime.datetime.now().strftime('%Y-%m')
    query = f"""
                SELECT payee, SUM(withdrawal_amt) AS total_spent, SUM(deposit_amt) AS total_deposited
                FROM `{BQ_PROJECT}.{BQ_DATASET}.transactions`
                WHERE CAST(SUBSTR(date, 4, 2) AS INT64) = CAST(SUBSTR("{current_month}", 4, 2) AS INT64)
                    AND CAST(SUBSTR(date, 7, 2) AS INT64) = CAST(SUBSTR("{current_month}", 1, 2) AS INT64)
                GROUP BY payee
            """
    return viz_data (query)


# Function to generate visualizations for a specific month
@app.route('/<year>-<month>')
def visualize_specific_month(year, month):
    requested_month = f"{year}-{month}"
    query = f"""
            SELECT payee, SUM(withdrawal_amt) AS total_spent, SUM(deposit_amt) AS total_deposited
            FROM `{BQ_PROJECT}.{BQ_DATASET}.transactions`
            WHERE CAST(SUBSTR(date, 4, 2) AS INT64) = CAST(SUBSTR("{requested_month}", 4, 2) AS INT64)
                AND CAST(SUBSTR(date, 7, 2) AS INT64) = CAST(SUBSTR("{requested_month}", 1, 2) AS INT64)
            GROUP BY payee
        """
    return viz_data(query)




@app.route('/rx/<year>')
def visualize_year(year):
    query = f"""
        SELECT payee, SUM(withdrawal_amt) AS total_spent, SUM(deposit_amt) AS total_deposited
        FROM `{BQ_PROJECT}.{BQ_DATASET}.transactions`
        WHERE CAST(SUBSTR(date, 7, 2) AS INT64) = CAST(SUBSTR('{year}', 1, 2) AS INT64)
        GROUP BY payee
    """
    return viz_data(query)



@app.route ("/hx")
def process ():
    process_latest_statement()
    return ("<h1>Done</h1>")


if __name__ == '__main__':
    #Run the Flask app for visualizations
    app.run(debug=True, host='0.0.0.0')