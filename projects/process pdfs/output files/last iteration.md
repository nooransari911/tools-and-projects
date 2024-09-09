2024-09-09 11:59:07.723195;

## Data Ingestion and Preparation: ETL, ELT, and Data Wrangling

### 1.1 Introduction

This module explores the essential processes of ingesting and preparing data for use in data pipelines, focusing on two primary approaches: Extract, Transform, Load (ETL) and Extract, Load, Transform (ELT). We'll delve into the intricacies of data wrangling, a multifaceted process involving various steps to transform raw data into valuable datasets for downstream analysis.

### 1.2 Ingesting Data: A Foundation for Data Pipelines

Data ingestion is the crucial first step in building a data pipeline. It involves extracting data from external sources, loading it into the pipeline's storage, and transforming it to meet the specific needs of downstream processes.

#### 1.2.1 ETL and ELT: Two Contrasting Approaches

**Extract, Transform, Load (ETL)** is the traditional data ingestion method. It involves extracting data from its source, transforming it into a structured format suitable for analytics applications, and then loading it into a structured storage system like a data warehouse.

**Extract, Load, Transform (ELT)** is a newer approach, driven by the emergence of data lakes for handling large volumes of unstructured and semi-structured data.  ELT extracts data from its source, performs minimal initial transformations to store it in a relatively raw state within a data lake. Data is then transformed as needed for specific use cases as consumers access and analyze it.

#### 1.2.2 Comparing ETL and ELT: Choosing the Right Approach

The choice between ETL and ELT depends largely on your business needs, the nature of your data, and the type of analysis you plan to perform.

**ETL Advantages:**

* **Automated Routine Transformations:** ETL saves time for analysts by storing data in a ready-to-analyze format.
* **Filtering Sensitive Data:** Performing transformations upfront allows you to filter out sensitive information (e.g., personally identifiable information), reducing compliance risks.

**ETL is well-suited for structured data destined for a data warehouse.** By performing transformations upfront, you can streamline analysis and mitigate security concerns.

**ELT Advantages:**

* **Faster Ingestion:** ELT can expedite the ingestion process by delaying transformations until later.
* **Greater Flexibility:** ELT provides greater flexibility for creating new queries by allowing access to raw data.

**ELT is well-suited for unstructured data destined for a data lake.** It offers faster ingestion and increased flexibility for data exploration.

#### 1.2.3 The Dynamic Nature of Ingestion Processes

It's important to remember that the ingestion process is dynamic. As your understanding of the data evolves and usage patterns change, the pipeline's transformations and processes might need adjustments to optimize performance and value.

**For instance:**

* Data engineers might automate a nightly batch process to ingest support ticket data.
* Data scientists might later request that comment fields are no longer truncated, as they are necessary for sentiment analysis.
* Data analysts might routinely apply a common date format transformation, leading to its inclusion in the ingestion process.

Modern data architectures often blur the lines between ETL and ELT. Different roles might perform different parts of the ingestion and transformation process using various tools and access methods. For example:

* Data engineers might use ingestion tools to handle common transformations before loading data into a data lake.
* Data analysts might apply transformations on ingested data to prepare it for specific reports.
* Data scientists might perform additional discovery and transformation to investigate data relationships.

### 1.3 Data Wrangling: The Art of Transforming Raw Data into Insights

Data wrangling encompasses the complex processes involved in transforming large amounts of unstructured or structured raw data from diverse sources into a meaningful and valuable dataset for downstream processes or users. While data wrangling can be performed by data engineers, data scientists, and data analysts, each role might perform different types of wrangling based on their needs and the initial state of the data.

#### 1.3.1  Data Wrangling: Addressing Data Variety

Data wrangling is essential for managing data variety. For example, a company might combine various data types to personalize customer experiences. Imagine a company that wants to leverage data to provide personalized health recommendations:

* **Querying an On-premises Database:** The company queries its database to identify patients overdue for visits.
* **Combining Public Health Data:** Public health data is combined with customer data to identify demographic risk factors for heart attacks.
* **Real-time Mobile App Monitoring:** Real-time heart monitoring data from a mobile app is evaluated for anomalies, potentially alerting patients or their doctors.

To deliver personalized predictions, data engineers must bring all this data together and make it available in the data pipeline, enabling data scientists to build machine learning (ML) models.

#### 1.3.2 Data Wrangling Steps:  A Detailed Breakdown

The data wrangling process generally aligns with ETL processing, but there are crucial distinctions.

* **Traditional ETL:** Data engineers typically focused on scripting and automating transformations with batch jobs, while analysts and data scientists worked with refined data.
* **Data Wrangling:** More associated with an ELT flow, allowing business users or data scientists to transform datasets within the pipeline storage layer before refinement for specific use cases.

Cloud tools and services are increasingly abstracting infrastructure and coding tasks, giving more users direct access to data extraction and transformation. Data engineers must still build complete analytics pipelines and transform data, but they also need to stay informed about tools that empower greater autonomy for analysts and data scientists.

#### 1.3.3 Example: ELT and Data Wrangling in a Modern Data Architecture

Let's illustrate how data wrangling steps can be integrated into a modern data architecture using an ELT flow. Consider this example architecture:

* **Data Ingestion:** Data is ingested into a storage layer consisting of an Amazon S3 data lake and an Amazon Redshift data warehouse.
* **S3 Buckets as Zones:** S3 buckets serve as zones within the data lake, storing data in different states:
    * **Landing Zone:**  Temporary storage for initial cleaning and validation.
    * **Raw Zone:**  Permanent storage for ingested data in its relatively raw state.
    * **Trusted Zone:** Data structured for use in the data warehouse.
    * **Curated Layer:** Data enriched and validated for low-latency access and complex querying in Amazon Redshift.

**Wrangling Steps in the Example Architecture:**

* **Landing Zone:** Data is cleaned and validated before being stored in the raw zone.
* **Raw Zone:** Data in the raw zone can be used for additional use cases.
* **Trusted Zone:** Data is structured, enriched, and validated before being stored in the curated layer.
* **Curated Layer:** Datasets are ready for ingestion into the Amazon Redshift data warehouse.

**Comparison to ETL:**

* The same wrangling tasks would still be necessary in a traditional ETL flow.
* In ETL, all transformations would be performed on the data in a temporary staging location before loading it directly into the data warehouse.
* Raw data would not be available to users until processing is complete.

### 1.4 Data Wrangling Steps: A Detailed Examination

#### 1.4.1 Data Discovery:  Understanding Your Data Sources

Data discovery is the initial step in data wrangling, and it's an iterative process that involves different roles (analyst, data scientist, data engineer) focusing on different aspects. As a data engineer, your responsibility is to identify potential sources, query them, and analyze the raw data to determine its value for your business purpose.

**Key Tasks During Data Discovery:**

* **Determine if a Source Serves Your Business Purpose:**
    * Identify relationships within and between data sources.
    * Identify data formats (e.g., CSV, Parquet, ORC).
    * Determine the desired data range from each source (e.g., time period or range of attribute values).
* **Determine Data Organization:**
    * Choose appropriate folder structures and file sizes.
    * Establish partitions for target database tables.
    * Consider access control and security measures.
* **Determine Required Tools and Skills:**
    * Assess existing tools for storing, securing, transforming, and querying the data.
    * Determine if you have the necessary skills and resources to extract and prepare the data.
* **Decide Whether to Proceed:**
    * Based on analysis, you might decide to work with the source or determine that the effort and cost don't justify the value.

#### 1.4.2 Data Discovery Example Scenario

Imagine a company with a SaaS product that acquires a startup with a different customer support system. A data analyst requests the ingestion of support ticket data from both products to analyze the relationships between support experiences, ticket volumes, and contract renewals. The analyst wants to know the number and types of technical issues for each customer in 2020, with regional sales teams accessing only their customers. The existing sales analytics pipeline uses AWS services and stores customer data in an Amazon Redshift data warehouse, but lacks customer support data.

#### 1.4.3 Data Discovery Example: Querying Data Sources

**Tables:**

* **Ticket table in existing support system (supp1):**

    |ticket_id|requestor_id|submitter_id|assignee_id|group|subject|status|priority|ticket_type|create_date|updated_date|solved_date|
    |---|---|---|---|---|---|---|---|---|---|---|---|
    ||||||||High|||||
    ||||||||Low|||||

* **Ticket table in acquired support system (supp2):**

    |issue_id|cust_num|description|status|priority|create_date|updated_date|closed_date|
    |---|---|---|---|---|---|---|---|
    ||||1|||||
    ||||3|||||
    ||||5|||||

* **Customer table in the data warehouse:**

    |customer_id|cust_name|primary_poc|status|sales_group|
    |---|---|---|---|---|

The data engineer would examine the fields and data in the source data for customer support tickets and identify related information in the data warehouse to determine how to get the desired data into the pipeline.

#### 1.4.4 Data Discovery Tasks:  Example Scenario

||||||
|---|---|---|---|---|
|Identify relationships|Identify formats|Determine what you need/how to get it|Determine how to organize and access|Determine tools and skills available|
|supp1 requestor_id = supp2 cust_num = customer|Ticket systems export .json files Storage target = S3 bucket|Ticket status = "open", "solved", "closed" Tickets where create_date or updated_date = 2020|Access is by sales region Create sales region prefixes in an S3 bucket Analysts will query with Amazon Redshift Spectrum or Amazon Athena|Based on the exploratory nature of the request, it needs a one-time extract with minimal automation The easiest option available is to use Microsoft Excel to wrangle the data Excel can import .json and export .csv files|
|customer_id supp1 ticket_id = supp2 issue_id|||||
|supp1 subject = supp2 description|||||
|supp1 priority "High", "Medium", "Low" = supp2 priority 1, 2, 3|||||

This table summarizes the discovery activities for the example scenario, providing information for the data engineer to decide how to extract and structure the data for ingestion.

#### 1.4.5 Data Structuring:  Mapping and Organizing Your Data

The data structuring step follows data discovery and focuses on mapping data from source files into a format that supports combining and storing it with other data. The goal is to optimize the structure of the raw dataset, minimizing costs and maximizing pipeline performance.

**Key Tasks in Data Structuring:**

* **Organize Storage:** Create infrastructure, set up access controls, create IAM access policies, etc.
* **Parse the Source File:** Convert defined strings or patterns in the source into formats suitable for structured tables or categorization in the data lake.
* **Map Fields:** Match source fields to appropriate fields in the target storage.
* **Manage File Size:** Optimize file size for storage and retrieval by splitting or combining files and applying compression.

#### 1.4.6 Data Structuring Example: Parsing supp2 File and Mapping Fields

In the example scenario, the structuring step involves exporting a .json file from the customer support ticket system, loading it into Excel, and letting Excel parse the file. The data engineer would modify the cust_num field to match the customer_id field in the data warehouse and modify other columns (issue_id, description, closed_date) to match those in supp1.

#### 1.4.7 Data Cleaning:  Ensuring Data Accuracy and Consistency

The data cleaning step follows data structuring and focuses on preparing the raw data for use in the pipeline. Cleaning is usually performed per source, based on its characteristics.

**Data Cleaning Tasks:**

* **Removing Unwanted Data:** Removing columns with PII, irrelevant fields, duplicate values, corrupted data, or unwanted characters.
* **Filling in Missing Data Values:** Converting blank fields to zeroes for numeric fields or adding generic values to fill mandatory fields.
* **Validating and Modifying Data Types:** Ensuring data types in the source file match the target and modifying those that don't (e.g., converting text strings to properly formatted date fields).
* **Fixing Outliers:** Identifying outliers and either removing them or fixing them at the source.

The methods and results of cleaning might differ depending on who performs it. For example, a data engineer might replace blank fields with values that fit the data type, while a data analyst might replace blanks with corrected values.

#### 1.4.8 Data Cleaning Example: Removing and Fixing Data

In the example scenario, the cleaning step would include:

* Replacing blank customer_id with a placeholder.
* Removing corrupted data from a subject field.
* Validating and modifying data types (numeric priority values and date fields).

#### 1.4.9 Data Enriching:  Expanding and Combining Your Data

The data enriching step follows cleaning and focuses on bringing together related data from disparate sources to create the necessary dataset for analysis.

**Key Tasks in Data Enriching:**

* **Merge Sources:** Combine data from cleaned source files into a single dataset.
* **Supplement Data:** Add additional values to support analysis or desired visualization.

Data enriching can be simple (merging similar files) or complex (combining data from multiple, different sources).

#### 1.4.10 Data Enriching Example:  Combining Disparate Sources

In the support ticket example, the primary enriching step is to combine the two sets of support ticket files into a single file. The data engineer might query the sales system to get the sales owner by customer_id and use this information to add a sales_region column to the combined file.

#### 1.4.11 Data Validating:  Ensuring Data Integrity

The data validating step follows enriching and ensures the veracity of the dataset created for analytics or ML use cases.

**Key Tasks in Data Validating:**

* **Audit Your Work:**
    * Count expected rows.
    * Check consistency.
    * Check expected formats and data types.
    * Check for duplicates.
    * Check for PII.
    * Check for outliers.
* **Fix the Data:**
    * Address audit findings.
    * Address issues at the source.
    * Fix issues with integration tools or scripts.

Validating shares similarities with cleaning. Cleaning focuses on ensuring data is suitable for pipeline loading, while validating ensures the integrity of the combined dataset.

#### 1.4.12 Data Publishing: Making Your Data Available

The data publishing step follows validating and focuses on making the wrangled dataset available to users for analysis or further processing.

**Key Tasks in Data Publishing:**

* **Determine the Target Destination:**
    * Data lake (e.g., Amazon S3 bucket)
    * Data warehouse (e.g., Amazon Redshift)
    * Other data stores
* **Configure Access Controls:**
    * IAM policies
    * Data access permissions
    * Data sharing mechanisms

Publishing might involve:

* Loading the dataset into a data lake or data warehouse.
* Creating a shared folder or directory for the dataset.
* Publishing the dataset as a public API for external access.

### 1.5 Conclusion:  Building Effective Data Pipelines

Data ingestion and preparation are fundamental steps in creating valuable data pipelines. By mastering the key concepts and steps involved in ETL, ELT, and data wrangling, you can effectively ingest and prepare data for various analytics and ML use cases. 
