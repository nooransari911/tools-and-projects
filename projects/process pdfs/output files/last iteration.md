2024-09-09 13:13:57.007463;

## Data Ingestion and Preparation

This module focuses on the process of ingesting and preparing data for use in data pipelines, setting the stage for further analysis and insights.

### 1.1. Ingesting and Preparing Data

#### 1.1.1 Introduction

This section explores the process of ingesting and preparing data, laying the foundation for creating valuable data pipelines.

#### 1.1.2 Module Objectives

By the end of this module, you will be able to:

* **Distinguish** between Extract, Transform, Load (ETL) and Extract, Load, Transform (ELT) processes.
* **Define** data wrangling and its role in data ingestion.
* **Describe** the essential tasks involved in each data wrangling step:
    * Discovery
    * Structuring
    * Cleaning
    * Enriching
    * Validating
    * Publishing

#### 1.1.3 Module Overview

This module delves into the intricacies of data ingestion, building upon the knowledge from previous modules. We will analyze ETL and ELT approaches and unpack the steps involved in data wrangling, ultimately equipping you with the tools and understanding to navigate this crucial process.

##### 1.1.3.1 Presentation Sections

* ETL and ELT Comparison
* Data Wrangling: An Overview
* Data Discovery
* Data Structuring
* Data Cleaning
* Data Enriching
* Data Validating
* Data Publishing

##### 1.1.3.2 Knowledge Checks

* Online Knowledge Check
* Sample Exam Question

This module concludes with a sample exam question and an online knowledge check to solidify your understanding of data ingestion and preparation.

### 1.2. ETL and ELT Comparison

This section explores the core processes used to ingest data into an analytics pipeline, comparing the traditional ETL approach with the more modern ELT approach.

#### 1.2.1 Ingesting Data: Storing and Processing

Data ingestion involves bringing data from external sources into your pipeline for analysis and processing. This process is intricately linked to storing and processing data, forming a crucial part of the data pipeline.

The ingestion process typically involves the following steps:

* **Extraction:** Gathering data from an external source outside your pipeline.
* **Loading:** Placing the extracted data into temporary storage within the pipeline.
* **Processing:** Transforming the data before or after loading it into permanent storage.

The extent and nature of transformations, as well as their placement within the pipeline, are heavily influenced by business needs and the type of data being ingested.

#### 1.2.2 ETL and ELT

##### 1.2.2.1 Extract, Transform, Load (ETL)

The ETL approach, a traditional method, involves:

1. **Extraction:** Extracting structured data from its source.
2. **Transformation:** Transforming the data to match the desired format for analytics applications.
3. **Loading:** Loading the transformed data into structured storage, often a data warehouse.

##### 1.2.2.2 Extract, Load, Transform (ELT)

ELT, a newer approach, emerged with the rise of data lakes to handle vast amounts of unstructured and semi-structured data. ELT involves:

1. **Extraction:** Extracting unstructured or structured data.
2. **Loading:** Loading the data into the data lake, retaining as much of its raw form as possible.
3. **Transformation:** Transforming the data as needed for specific analytics scenarios, often performed later when accessing the data for specific use cases.

#### 1.2.3 Benefits of ETL

* **Automated routine transformations:** ETL simplifies analysis by storing data that is already prepared for use.
* **Filtering sensitive data:** Performing transformations upfront allows you to remove personally identifiable information (PII) or other sensitive data, mitigating compliance risks.

ETL is particularly suitable for structured data destined for a data warehouse. Pre-processing transformations optimize analysis time and minimize security concerns.

#### 1.2.4 Benefits of ELT

* **Faster ingestion:** ELT can accelerate the ingestion process by postponing transformations until a later stage.
* **Greater flexibility:** ELT provides more flexibility for creating new queries by offering access to raw data, allowing for greater exploration.

ELT is well-suited for unstructured data destined for a data lake. It delivers faster ingestion and enhances flexibility for data exploration.

#### 1.2.5 The Evolving Ingestion Process

The ingestion process is dynamic, evolving based on the needs of both pipeline builders and users.

**Example:**

* A data engineer automates a nightly batch process to ingest support ticket data.
* A data scientist requests that comment fields are no longer truncated, as they are needed for sentiment analysis.
* Data analysts routinely apply a common date format transformation and request its inclusion in the ingestion process.

Modern data architectures often blur the lines between ETL and ELT, with different roles using various tools to perform different parts of the ingestion and transformation process.

**For example:**

* Data engineers might use ingestion tools to handle common transformations before loading data into a data lake.
* Data analysts might apply transformations on ingested data to prepare it for specific reports.
* Data scientists might perform additional discovery and transformation to investigate hypotheses about data relationships.

The ingestion process requires continuous monitoring and adjustment based on usage patterns and evolving needs. This includes:

* **Optimizing performance:** Including recurring transformations in pre-loading processing can improve performance and reduce costs.
* **Addressing new needs:** Reducing the amount of pre-loading transformations might be necessary to accommodate new requirements.

As a data engineer, it's crucial to monitor pipeline performance, access patterns, and usage to maximize its value and adapt to changing demands.

#### 1.2.6 Key Takeaways: ETL and ELT Comparison

* Ingestion involves pulling data into the pipeline and applying transformations.
* ETL is suitable for structured data destined for a data warehouse.
* ELT is suitable for unstructured data destined for a data lake.
* The ETL and ELT processing should evolve to optimize pipeline value and adapt to evolving needs.

### 1.3. Data Wrangling: An Overview

This section delves into the high-level processes involved in preparing data for ingestion into an analytics pipeline, highlighting the crucial role of data wrangling.

#### 1.3.1 Data Wrangling

Data wrangling is the complex process of transforming large amounts of unstructured or structured raw data from multiple sources, each with its own schema, into a meaningful and valuable dataset for downstream processes or users.

While data engineers, data scientists, and data analysts might all engage in data wrangling, their individual roles and activities within this process vary based on their needs and the initial state of the data.

#### 1.3.2 Data Wrangling Addresses Data Variety

Data wrangling is essential for managing data variety, as exemplified by the following scenario:

**Example:**

* A company queries its on-premises database to identify patients overdue for visits.
* Public health data is combined with customer data to identify demographic risk factors for heart attacks, allowing for personalized information for patients with those risks.
* Real-time heart monitoring data from a mobile app is analyzed for anomalies, potentially alerting patients or their doctors.

Data engineers must bring together all this diverse data and make it accessible within the pipeline, empowering data scientists to build machine learning (ML) models for personalized predictions.

#### 1.3.3 Data Wrangling Steps

The data wrangling process often aligns with ETL processing, but there are distinctions:

* **Traditional ETL:** Data engineers focused on scripting and automating transformations with batch jobs, while analysts and data scientists worked with refined data.
* **Data Wrangling:** More associated with an ELT flow, allowing business users or data scientists to directly transform datasets within the pipeline storage layer before refinement for specific use cases.

Cloud tools and services are increasingly abstracting infrastructure and coding tasks, granting more users direct access to data extraction and transformation. While data engineers remain crucial for building complete analytics pipelines and transforming data, they must stay informed about tools that empower analysts and data scientists with greater autonomy.

#### 1.3.4 Example: ELT and Data Wrangling in a Modern Data Architecture

This section illustrates how data wrangling steps can be integrated into a modern data architecture using an ELT flow.

**Example Architecture:**

* Data is ingested into a storage layer containing an Amazon S3 data lake and an Amazon Redshift data warehouse.
* S3 buckets are used as zones within the data lake, storing data in different states:
    * **Landing zone:** Temporary storage for initial cleaning and validation.
    * **Raw zone:** Permanent storage for ingested data in its relatively raw state.
    * **Trusted zone:** Data structured for use in the data warehouse.
    * **Curated layer:** Data enriched and validated for low-latency access and complex querying in Amazon Redshift.

**Wrangling Steps in the Example Architecture:**

* **Landing zone:** Data is cleaned and validated before being stored in the raw zone.
* **Raw zone:** Data in the raw zone can be used for additional use cases.
* **Trusted zone:** Data is structured, enriched, and validated before being stored in the curated layer.
* **Curated layer:** Datasets are ready for ingestion into the Amazon Redshift data warehouse.

**Comparison to ETL:**

* The same wrangling tasks would still be necessary in a traditional ETL flow.
* In ETL, all transformations would be performed on the data in a temporary staging location before loading it directly into the data warehouse.
* Raw data would not be available to users until processing is complete.

#### 1.3.5 Key Takeaways: Data Wrangling Introduction

* Data wrangling is a multi-step process for transforming large amounts of data from multiple sources for analytics.
* Data wrangling is crucial for data scientists building ML models.
* Data wrangling steps might overlap, iterate, or not occur in some ingestion processes.
* Data wrangling steps include discovery, structuring, cleaning, enriching, validating, and publishing.

### 1.4. Data Discovery

This section delves into the data discovery step of the data wrangling process, emphasizing the iterative nature of this crucial step and its importance in evaluating the suitability of data sources.

#### 1.4.1 Decisions and Tasks in Discovery

The data discovery step is iterative, with different roles (analyst, data scientist, data engineer) focusing on different aspects. As a data engineer, your responsibility is to identify potential data sources, query them, and analyze the raw data to determine its value for your business purpose.

Key tasks during data discovery include:

* **Determine if a source serves your business purpose:**
    * Identify relationships within and between data sources.
    * Identify data formats (e.g., CSV, Parquet, ORC).
    * Determine the desired data range from each source (e.g., time period or range of attribute values).
* **Determine data organization:**
    * Choose appropriate folder structures and file sizes.
    * Establish partitions for target database tables.
    * Consider access control and security measures.
* **Determine required tools and skills:**
    * Assess existing tools for storing, securing, transforming, and querying the data.
    * Determine if you have the necessary skills and resources to extract and prepare the data.
* **Decide whether to proceed:**
    * Based on your analysis, you might decide to work with the source or determine that the effort and cost don't justify the value.

#### 1.4.2 Data Discovery Example Scenario

**Scenario:**

* A company with a SaaS product acquires a startup with a different customer support system.
* A data analyst requests ingestion of support ticket data from both products to analyze relationships between support experiences, ticket volumes, and contract renewals.
* The analyst wants to know the number and types of technical issues for each customer in 2020, with regional sales teams accessing only their customers.
* The existing sales analytics pipeline uses AWS services and stores customer data in an Amazon Redshift data warehouse, but lacks customer support data.

#### 1.4.3 Data Discovery Example: Query Data Sources

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

#### 1.4.4 Data Discovery Tasks: Example Scenario

||||||
|---|---|---|---|---|
|Identify relationships|Identify formats|Determine what you need/how to get it|Determine how to organize and access|Determine tools and skills available|
|supp1 requestor_id = supp2 cust_num = customer|Ticket systems export .json files Storage target = S3 bucket|Ticket status = "open", "solved", "closed" Tickets where create_date or updated_date = 2020|Access is by sales region Create sales region prefixes in an S3 bucket Analysts will query with Amazon Redshift Spectrum or Amazon Athena|Based on the exploratory nature of the request, it needs a one-time extract with minimal automation The easiest option available is to use Microsoft Excel to wrangle the data Excel can import .json and export .csv files|
|customer_id supp1 ticket_id = supp2 issue_id|||||
|supp1 subject = supp2 description|||||
|supp1 priority "High", "Medium", "Low" = supp2 priority 1, 2, 3|||||

This table summarizes the discovery activities for the example scenario, providing information for the data engineer to decide how to extract and structure the data for ingestion.

#### 1.4.5 Key Takeaways: Data Discovery

* Data discovery is iterative and role-dependent.
* Tasks include identifying relationships and formats, determining data filtering and organization in target storage.
* The primary outcomes are identification of required tools and resources and a decision to move forward.

### 1.5. Data Structuring

This section explores the data structuring step of the data wrangling process, focusing on the transformation of data from its raw format into a structure suitable for integration with other data.

#### 1.5.1 The Data Structuring Step within Data Wrangling

The structuring step follows discovery and focuses on mapping data from source files into a format that supports combining and storing it with other data. The goal is to optimize the structure of the raw dataset, minimizing costs and maximizing pipeline performance.

#### 1.5.2 Decisions and Tasks in Data Structuring

|||||
|---|---|---|---|
|Organize storage|Parse the source file|Map fields|Manage file size|
|- Control access.|- Convert strings and patterns into fields or attributes.|- Match source fields to target fields.|- Split or merge files.|
|- Create the folder structure.|||- Compress files.|
|- Establish partitions.||||

Key tasks in data structuring include:

* **Organize storage:** Create infrastructure, set up access controls, create IAM access policies, etc.
* **Parse the source file:** Convert defined strings or patterns in the source into formats suitable for structured tables or categorization in the data lake.
* **Map fields:** Match source fields to appropriate fields in the target storage.
* **Manage file size:** Optimize file size for storage and retrieval by splitting or combining files and applying compression.

#### 1.5.3 Data Structuring Example: Parse supp2 File and Map Fields

In the example scenario, the structuring step involves exporting a .json file from the customer support ticket system, loading it into Excel, and letting Excel parse the file. The data engineer would modify the cust_num field to match the customer_id field in the data warehouse and modify other columns (issue_id, description, closed_date) to match those in supp1.

#### 1.5.4 Key Takeaways: Data Structuring

* Data structuring involves mapping raw data from source files into a format suitable for combining and storing with other data.
* It includes organizing storage and access, parsing source files, mapping source fields to target fields, and optimizing file size.

### 1.6. Data Cleaning

This section explores the data cleaning step of the data wrangling process, emphasizing the preparation of raw data for use in the pipeline through the identification and correction of errors and inconsistencies.

#### 1.6.1 The Cleaning Step within Data Wrangling

The cleaning step follows structuring and focuses on preparing the raw data for use in the pipeline. Cleaning is usually performed per source, based on its characteristics.

#### 1.6.2 Decisions and Tasks in Cleaning

Data cleaning includes tasks such as:

* **Removing unwanted data:** Removing columns with PII, irrelevant fields, duplicate values, corrupted data, or unwanted characters.
* **Filling in missing data values:** Converting blank fields to zeroes for numeric fields or adding generic values to fill mandatory fields.
* **Validating and modifying data types:** Ensuring data types in the source file match the target and modifying those that don't (e.g., converting text strings to properly formatted date fields).
* **Fixing outliers:** Identifying outliers and either removing them or fixing them at the source.

The methods and results of cleaning might differ depending on who performs it. For example, a data engineer might replace blank fields with values that fit the data type, while a data analyst might replace blanks with corrected values.

#### 1.6.3 Data Cleaning Example: Remove and Fix Data

In the example scenario, the cleaning step would include:

* Replacing blank customer_id with a placeholder.
* Removing corrupted data from a subject field.
* Validating and modifying data types (numeric priority values and date fields).

#### 1.6.4 Key Takeaways: Data Cleaning

* Data cleaning prepares source data for use in a pipeline.
* Cleaning is usually performed per source and includes tasks such as removing duplicates, fixing values, and adjusting data types.
* The resolution of cleaning tasks depends on the role of the person performing them.

### 1.7. Data Enriching

This section explores the data enriching step of the data wrangling process, focusing on the process of bringing together related data from disparate sources to create a dataset that is ready for analysis.

#### 1.7.1 The Enriching Step within Data Wrangling

The enriching step follows cleaning and focuses on bringing together related data from disparate sources to create the necessary dataset for analysis.

#### 1.7.2 Decisions and Tasks in Enriching

|||
|---|---|
|Merge sources|Supplement data|
|- Combine data from cleaned source files into a single dataset.|- Add additional values to support analysis or desired visualization.|

Data enriching can be simple (merging similar files) or complex (combining data from multiple, different sources).

#### 1.7.3 Data Enriching Example: Combine Disparate Sources

In the support ticket example, the primary enriching step is to combine the two sets of support ticket files into a single file. The data engineer might query the sales system to get the sales owner by customer_id and use this information to add a sales_region column to the combined file.

#### 1.7.4 Key Takeaways: Data Enriching

* Data enriching combines data sources and adds value to the data.
* Tasks include merging sources, adding additional fields, and calculating new values.

### 1.8. Data Validating

This section explores the data validating step of the data wrangling process, emphasizing the importance of ensuring the veracity and accuracy of the dataset created for analysis or ML use cases.

#### 1.8.1 The Validating Step within Data Wrangling

The validating step follows enriching and ensures the veracity of the dataset created for analytics or ML use cases.

#### 1.8.2 Decisions and Tasks in Validating

|||
|---|---|
|Audit your work|Fix the data|
|- Count expected rows.|- Address audit findings.|
|- Check consistency.|- Address issues at the source.|
|- Check expected formats and data types.|- Fix issues with integration tools or scripts.|
|- Check for duplicates.||
|- Check for PII.||
|- Check for outliers.||

Validating shares similarities with cleaning. Cleaning focuses on ensuring data is suitable for pipeline loading, while validating ensures the integrity of the combined dataset.

#### 1.8.3 Key Takeaways: Data Validating

* Data validating ensures the veracity of the dataset created for analytics or ML use cases.
* Tasks include auditing the dataset for expected rows, consistency, formats, data types, duplicates, PII, and outliers.
* Validation might involve automated checks, manual inspections, or a combination of both.

### 1.9. Data Publishing

This section explores the data publishing step of the data wrangling process, focusing on making the wrangled dataset available to users for analysis or further processing.

#### 1.9.1 The Publishing Step within Data Wrangling

The publishing step follows validating and focuses on making the wrangled dataset available to users for analysis or further processing.

#### 1.9.2 Decisions and Tasks in Publishing

|||
|---|---|
|Determine the target destination|Configure access controls|
|- Data lake (e.g., Amazon S3 bucket)|- IAM policies|
|- Data warehouse (e.g., Amazon Redshift)|- Data access permissions|
|- Other data stores|- Data sharing mechanisms|

Publishing might involve:

* Loading the dataset into a data lake or data warehouse.
* Creating a shared folder or directory for the dataset.
* Publishing the dataset as a public API for external access.

#### 1.9.3 Key Takeaways: Data Publishing

* Data publishing focuses on making the wrangled dataset available for analysis or further processing.
* It involves determining the target destination, configuring access controls, and potentially using data sharing mechanisms.

### 1.10. Conclusion

Data ingestion and preparation are vital steps in creating valuable data pipelines. By understanding the key concepts and steps involved, you can effectively ingest and prepare data for various analytics and ML use cases, unlocking valuable insights from your data.

Remember to continuously monitor and adapt your ingestion process to ensure optimal performance, efficiency, and alignment with evolving needs. As data pipelines become more sophisticated and complex, your mastery of data ingestion and preparation will become increasingly crucial for driving successful data-driven outcomes.