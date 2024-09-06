# 2024-09-07 03:33:51.417919;

# Total Time taken: 266.614270608

total input tokens: 87697

total output tokens: 8192

## Module 2: AWS Academy Data Engineering: Data-Driven Organizations Student Guide

### 1.1 Data-Driven Organizations

#### 1.1.1 Introduction

This module provides an overview of data-driven organizations, covering:

- How data analytics and AI/ML contribute to data-driven decisions.
- The layers of a data pipeline and data transformations within them.
- The roles of data engineers and data scientists in building data pipelines.
- The influence of modern data strategies on infrastructure design.

#### 1.1.2 Module Objectives

Upon completion, you will be able to:

- **Distinguish:** Data analytics from Artificial Intelligence (AI) and Machine Learning (ML) applications.
- **Identify:** The layers within a data pipeline.
- **Describe:** Actions taken on data as it moves through a pipeline.
- **Define:** Responsibilities of data engineers and data scientists in data pipeline processing.
- **Explain:** Three modern data strategies impacting data infrastructure development.

#### 1.1.3 Module Overview

**Presentation Sections**

- Data-driven decisions
- The data pipeline - infrastructure for data-driven decisions
- The role of the data engineer in data-driven organizations
- Modern data strategies

**Knowledge Checks**

- Online knowledge check
- Sample exam question

#### 1.1.4 Data-Driven Decisions

**The Need for Data-Driven Decisions**

Organizations are increasingly investing in data and analytics to become more data-driven. This shift is driven by the vast amounts of data generated from websites, mobile apps, and smart devices.

**How Data Drives Decisions**

Data science plays a crucial role in data-driven decisions, using two main categories:

- **Data Analytics:** Analyzes large datasets to identify patterns and trends, generating actionable insights. Well-suited for structured data with a limited number of variables.
- **AI/ML:** Uses mathematical models to predict data at scale, learning from examples in large datasets. Ideal for unstructured data and complex variables.

**Examples of Data-Driven Decisions**

- **Individuals:** Restaurant recommendations, personalized shopping suggestions, fraud detection.
- **Organizations:** Predicting fraudulent transactions, optimizing website design, personalized customer experiences.

**Challenges of Data-Driven Decisions**

While data offers opportunities, it also presents challenges:

- **Data Costs:** Managing and storing large volumes of data can be expensive.
- **Unstructured Data:** Analyzing unstructured data like images and text requires specialized tools.
- **Security Risks:** Protecting sensitive data is paramount.
- **Query Processing:** Processing large datasets can be time-consuming.

**The Value of Data Over Time**

Data's value diminishes over time. Real-time data enables proactive decisions, while older data serves reactive and historical analysis.

**Trade-offs in Data-Driven Decisions**

Balancing cost, speed, and accuracy is essential when building data infrastructure to support decision-making.

#### 1.1.5 The Data Pipeline - Infrastructure for Data-Driven Decisions

**What is a Data Pipeline?**

A data pipeline is the infrastructure that supports data-driven decision-making, encompassing:

- Ingesting data from various sources.
- Storing and processing data.
- Enabling data analysis and insight generation.

**Designing a Data Pipeline**

- Begin with the business problem and work backward to identify data requirements.
- Choose appropriate infrastructure based on data volume, velocity, and variety.

**Layers of a Data Pipeline**

- **Ingestion:** Acquiring data from sources.
- **Storage:** Persisting data in appropriate formats.
- **Processing:** Transforming and preparing data for analysis.
- **Analysis & Visualization:** Exploring data and generating insights.

**Data Wrangling**

Data wrangling refers to manipulating and transforming raw data for analysis, including:

- **Discovery:** Identifying data sources and understanding their characteristics.
- **Cleaning:** Removing inconsistencies and errors.
- **Normalization:** Standardizing data formats.
- **Enrichment:** Adding valuable information to datasets.

**Iterative Nature of Data Processing**

Data processing is often iterative, involving multiple cycles of refinement and analysis.

#### 1.1.6 The Role of the Data Engineer in Data-Driven Organizations

**Data Engineer vs. Data Scientist**

Both roles work with data pipelines, but their focuses differ:

- **Data Engineer:** Builds and manages the infrastructure that data passes through.
- **Data Scientist:** Analyzes the data in the pipeline to extract insights.

**Questions for Building a Data Pipeline**

Data engineers and scientists ask questions about:

- Data availability, location, format, and quality.
- Security requirements and access controls.
- Data volume, update frequency, and processing speed.
- Potential insights and suitable analysis tools.

**Iterative Design Process**

Designing a data pipeline is an iterative process, requiring ongoing collaboration between data engineers and scientists.

#### 1.1.7 Modern Data Strategies

**Strategies for Building Data Infrastructure**

- **Modernize:** Migrate to cloud-based, purpose-built services, reducing operational overhead and increasing agility.
- **Unify:** Create a single source of truth for data, enabling cross-organizational access and collaboration.
- **Innovate:** Incorporate AI/ML to uncover new insights and drive proactive decision-making.

**The Importance of Data as a Strategic Asset**

Treating data as a valuable asset empowers organizations to make better decisions, respond faster to change, and unlock new opportunities.

**Key Takeaways:**

- Data-driven organizations leverage data science for informed decisions.
- The data pipeline provides the infrastructure for data processing and analysis.
- Data engineers and scientists collaborate to build and analyze data pipelines.
- Modern data strategies emphasize modernization, unification, and innovation.


---


## Module 3: AWS Academy Data Engineering - Elements of Data

### 2.1 Elements of Data

#### 2.1.1 Introduction

This module focuses on understanding the characteristics of data that influence data pipeline design.

#### 2.1.2 Module Objectives

Upon completion, you will be able to:

- **List:** The five Vs of data.
- **Describe:** The impact of volume and velocity on your data pipeline.
- **Compare and contrast:** Structured, semistructured, and unstructured data types.
- **Identify:** Data sources commonly used to feed data pipelines.
- **Pose questions:** About data to assess its veracity.
- **Suggest methods:** To improve the veracity of data in your pipeline.

#### 2.1.3 Module Overview

**Presentation Sections**

- The five Vs of data: volume, velocity, variety, veracity, and value
- Volume and velocity
- Variety - data types
- Variety - data sources
- Veracity and value
- Activities to improve veracity and value

**Activity**

- Planning Your Pipeline

**Knowledge Checks**

- Online knowledge check
- Sample exam question

#### 2.1.4 The Five Vs of Data

**Understanding Data Characteristics**

The five Vs of data are critical for pipeline design:

- **Volume:** The amount of data to be processed.
- **Velocity:** The speed at which data enters and moves through the pipeline.
- **Variety:** The types and formats of data, including structured, semistructured, and unstructured.
- **Veracity:** The accuracy, trustworthiness, and quality of data.
- **Value:** The insights that can be extracted from data.

**Strategies for Value Extraction**

- Ensure data meets business needs.
- Evaluate data acquisition feasibility.
- Match pipeline design to data characteristics.
- Balance cost and performance.
- Empower users to focus on insights.
- Implement data governance and cataloging.

**The Importance of Veracity**

Bad data can lead to worse decisions than limited data. Maintaining data integrity is crucial for reliable analysis.

#### 2.1.5 Volume and Velocity

**Impact on Pipeline Layers**

Volume and velocity influence decisions across all pipeline layers:

- **Ingestion:** Choosing methods to handle data influx.
- **Storage:** Selecting storage types and scaling for capacity.
- **Processing:** Determining processing power and distributed solutions.
- **Analysis & Visualization:** Scaling tools for data volume and real-time needs.

**Examples of Decisions Based on Volume and Velocity**

- **Ingestion:** Streaming vs. batch ingestion for high-velocity data.
- **Storage:** Short-term vs. long-term storage based on data value over time.
- **Processing:** Big data frameworks for massive datasets.
- **Analysis & Visualization:** Real-time dashboards for streaming data.

#### 2.1.6 Variety - Data Types

**Types of Data**

- **Structured:** Organized in rows and columns with a well-defined schema (e.g., relational databases).
- **Semistructured:** Possesses a self-describing structure but lacks a rigid schema (e.g., JSON, XML).
- **Unstructured:** Lacks a predefined structure (e.g., images, videos, text).

**Challenges of Data Variety**

- **Data Formatting:** Different formats might require specific analysis tools.
- **Ingestion Complexity:** Combining diverse data types can complicate pipelines.
- **Data Veracity:** Maintaining data quality across multiple sources can be challenging.

**The Rise of Unstructured Data**

Most data growth today involves unstructured data, requiring specialized tools and AI/ML techniques for analysis.

#### 2.1.7 Variety - Data Sources

**Common Data Source Types**

- **On-premises databases:** Existing organizational data.
- **Public datasets:** Aggregated data about specific topics.
- **Time-series data:** Generated by events, IoT devices, and sensors.

**Pipeline Considerations Based on Source Type**

- **Organizational data:** Often structured and readily analyzed, but might contain sensitive information.
- **Public datasets:** Often semistructured, requiring transformations and data merging.
- **Time-series data:** Requires streaming ingestion and storage for real-time processing.

**Benefits and Challenges of Data Source Variety**

- **Benefits:** Enriched analysis through data combination.
- **Challenges:** Increased processing complexity due to diverse structures and content.

#### 2.1.8 Veracity and Value

**Veracity Drives Value**

Trustworthy data is essential for reliable analysis and decision-making. Bad data can lead to incorrect conclusions and negative outcomes.

**Maintaining Data Veracity**

- **Discovery:** Assessing data quality and lineage.
- **Cleaning and Transformation:** Removing inconsistencies, duplicates, and outliers.
- **Prevention:** Implementing security measures, data audits, and governance processes.

**Examples of Data Issues**

- **Missing data**
- **Ambiguity**
- **Statistical bias**
- **Duplicates**
- **Software bugs**
- **Human error**

**Best Practices for Cleaning Data**

- Define what "clean" means for each data source.
- Trace errors back to their source.
- Change data thoughtfully and retain auditable records.

**Data Transformation Techniques**

Transformations prepare data for analysis, including:

- Converting data types.
- Replacing values.
- Merging datasets.
- Aggregating data.

**Importance of Data Integrity and Consistency**

- Secure all layers of the pipeline.
- Implement least privilege access controls.
- Maintain audit trails.
- Enforce data compliance and governance.
- Maintain a single source of truth for data elements.

#### 2.1.9 Key Takeaways

- The five Vs of data (volume, velocity, variety, veracity, and value) drive pipeline design decisions.
- Volume and velocity determine scaling and throughput requirements.
- Data variety requires handling different types and sources, impacting processing complexity.
- Veracity is crucial for data trustworthiness and value extraction.
- Cleaning, transformation, and data integrity measures ensure data quality.


---

## Module 4: AWS Academy Data Engineering - Design Principles and Patterns for Data Pipelines

### 3.1 Design Principles and Patterns for Data Pipelines

#### 3.1.1 Introduction

This module covers the evolution of data architectures and how AWS services support modern data architectures. 

#### 3.1.2 Module Objectives

Upon completion, you will be able to:

- **Use:** The AWS Well-Architected Framework to design analytics workloads.
- **Recount:** Key milestones in the evolution of data stores and architectures.
- **Describe:** Components of modern data architectures on AWS.
- **Cite:** AWS design considerations and key services for a streaming analytics pipeline.

#### 3.1.3 Module Overview

**Presentation Sections**

- AWS Well-Architected Framework and Lenses
- The evolution of data architectures
- Modern data architecture on AWS
- Modern data architecture pipeline: Ingestion and storage
- Modern data architecture pipeline: Processing and consumption
- Streaming analytics pipeline

**Activity**

- Using the Well-Architected Framework

**Labs**

- Querying Data by Using Athena

**Knowledge Checks**

- Online knowledge check
- Sample exam question

#### 3.1.4 AWS Well-Architected Framework

**Pillars of the Framework**

The Well-Architected Framework provides best practices across six pillars:

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability

**Well-Architected Lenses**

Lenses extend guidance to specific domains:

- **Data Analytics Lens:** Focuses on designing well-architected analytics workloads.
- **ML Lens:** Addresses differences between application and ML workloads.

**Activity: Using the Well-Architected Framework**

This activity involves utilizing the Data Analytics Lens to identify best practices for building data pipelines.

#### 3.1.5 The Evolution of Data Architectures

**Application Architecture Evolution**

- From monolithic mainframes to distributed systems:
    - Client-server architecture
    - Three-tier architecture
    - Microservices

**Data Store Evolution**

- **Hierarchical databases:** Limited relationship handling capabilities.
- **Relational databases:** Structured data storage with robust querying.
- **Nonrelational databases:** Flexible data models for diverse data types.
- **Data lakes:** Centralized storage for raw, unstructured, and structured data.
- **Purpose-built data stores:** Optimized storage for specific data types and workloads.

**Data Architecture Evolution**

- **Data warehouses:** Separate analytical databases for reporting and BI.
- **Big data systems:** Distributed frameworks for handling massive datasets.
- **Lambda architecture:** Combining batch and stream processing for real-time insights.

#### 3.1.6 Modern Data Architecture on AWS

**Key Design Considerations**

- **Scalable data lake:** Centralized storage for all data types.
- **Performant and cost-effective components:** Purpose-built services for specific needs.
- **Seamless data movement:** Easy integration and data flow between components.
- **Unified governance:** Centralized management and security policies.

**Data Movement Types**

- **Outside in:** Moving data from purpose-built stores to the data lake.
- **Inside out:** Moving data from the data lake to purpose-built stores.
- **Around the perimeter:** Moving data between purpose-built stores without accessing the data lake.

**Avoiding Data Swamps**

Proper data cataloging, security, and governance are crucial to prevent data lakes from becoming unusable.

**AWS Services for Modern Data Architecture**

- **Amazon S3:** Data lake storage.
- **Athena:** Interactive querying of data in S3.
- **Amazon Redshift:** Data warehousing.
- **Amazon OpenSearch Service:** Real-time analytics and log analytics.
- **Amazon EMR:** Big data processing.
- **Amazon Aurora:** Relational database engine.
- **Amazon DynamoDB:** Nonrelational database for high-performance applications.
- **Amazon SageMaker:** AI/ML service.
- **AWS Glue:** Data movement and transformation.
- **AWS Lake Formation:** Data lake management and governance.

#### 3.1.7 Modern Data Architecture Pipeline: Ingestion and Storage

**Ingestion Layer**

- **Matching services to data characteristics:**
    - Amazon AppFlow: SaaS applications.
    - AWS Database Migration Service: Relational databases.
    - AWS DataSync: File shares.
    - Amazon Kinesis Data Streams and Firehose: Streaming data sources.

**Storage Layer**

- **Storage:**
    - Amazon S3: Data lake.
    - Amazon Redshift: Data warehouse.
- **Catalog:**
    - AWS Glue Data Catalog: Metadata storage.
    - AWS Lake Formation: Centralized governance and catalog.

**Storage Zones in Amazon S3**

- **Landing zone:** Initial data landing and cleaning.
- **Raw zone:** Permanent storage of raw data.
- **Trusted zone:** Structured data for the data warehouse.
- **Curated zone:** Enriched and validated data for analysis.

**Data Catalog Layer**

- **AWS Glue:** Schema generation, crawling, and metadata management.
- **AWS Lake Formation:** Centralized permissions management and schema-on-read for Redshift Spectrum.

#### 3.1.8 Modern Data Architecture Pipeline: Processing and Consumption

**Processing Layer**

- **SQL-based processing:** Amazon Redshift.
- **Big data processing:** Amazon EMR and AWS Glue.
- **Near real-time processing:** Amazon Kinesis Data Analytics or Spark Streaming on EMR or Glue.

**Consumption Layer**

- **Interactive SQL:** Athena.
- **Business intelligence:** Amazon Redshift and QuickSight.
- **Machine learning:** Amazon SageMaker.

#### 3.1.9 Streaming Analytics Pipeline

**Key Design Considerations**

- **Throughput:** Handling high-velocity data.
- **Loose coupling:** Independent and scalable components.
- **Parallel consumers:** Multiple consumers processing the same stream.
- **Checkpointing and replay:** Fault tolerance and data durability.

**Amazon Kinesis Services**

- **Kinesis Data Streams:** Durable storage for streaming data.
- **Kinesis Data Firehose:** Delivering streaming data to data stores and analytics services.
- **Kinesis Data Analytics:** Real-time analytics on streaming data.

#### 3.1.10 Key Takeaways

- The AWS Well-Architected Framework provides best practices for designing analytics workloads.
- Data architectures evolved to handle increasing data volume, variety, and velocity.
- Modern data architectures unify disparate data sources using a data lake.
- AWS offers purpose-built services for each layer of the data pipeline, including ingestion, storage, processing, and consumption.
- Streaming analytics pipelines require specific considerations for throughput, loose coupling, parallel consumers, and checkpointing.

---

## Module 5: AWS Academy Data Engineering: Securing and Scaling the Data Pipeline

### 4.1 Securing and Scaling the Data Pipeline

#### 4.1.1 Introduction

This module covers best practices for securing and scaling analytics and ML workloads. 

#### 4.1.2 Module Objectives

Upon completion, you will be able to:

- **Highlight:** How cloud security best practices apply to data pipelines.
- **List:** AWS services that secure a data pipeline.
- **Cite:** Factors driving performance and scaling decisions across each pipeline layer.
- **Describe:** How infrastructure as code supports security and scalability.
- **Identify:** The function of common AWS CloudFormation template sections.

#### 4.1.3 Module Overview

**Presentation Sections**

- Cloud security review
- Security of analytics workloads
- ML security
- Scaling: An overview
- Creating a scalable infrastructure
- Creating scalable components

**Knowledge Checks**

- Online knowledge check
- Sample exam question

#### 4.1.4 Cloud Security Review

**Shared Responsibility Model**

- **AWS:** Secures the underlying infrastructure (hardware, software, facilities, and networks).
- **Customer:** Responsible for securing their applications, data, and configurations within AWS.

**Design Principles for Data Security**

- **Implement a strong identity foundation:** Least privilege access and separation of duties.
- **Enable traceability:** Logging, monitoring, and auditing.
- **Apply security at all layers:** Defense-in-depth approach with multiple security controls.
- **Automate security best practices:** Infrastructure as code and automated security mechanisms.
- **Protect data in transit and at rest:** Encryption, tokenization, and access control.
- **Keep people away from data:** Reduce direct access and manual processing.
- **Prepare for security events:** Incident management and response plans.

**Access Management**

- **Authentication:** Verifying user identities.
- **Authorization:** Granting access based on permissions.
- **Principle of Least Privilege:** Granting only necessary permissions.

**AWS Identity and Access Management (IAM)**

- Centralized service for managing user access and permissions.
- Integration with most AWS services.
- Supports federated identity management, granular permissions, MFA, and audit trails.

**Data Security**

- **Data at rest:** Data stored in nonvolatile storage.
    - Secure key management.
    - Encryption at rest.
    - Access control and auditing.
- **Data in transit:** Data moving between systems.
    - Secure key and certificate management.
    - Encryption in transit.
    - Network communication authentication.

**AWS Key Management Service (AWS KMS)**

- Managed service for creating and managing cryptographic keys.
- Uses HSMs to protect keys.
- Integration with other AWS services.
- Supports usage policies for controlling key access.

**Logging and Monitoring**

- **Logging:** Collecting and recording activity and event data.
    - CloudTrail: AWS service for logging API calls and events.
- **Monitoring:** Continuously verifying security and performance.
    - CloudWatch: Service for monitoring AWS resources and applications.

#### 4.1.5 Security of Analytics Workloads

**Classify and Protect Data**

- Understand data classifications and protection policies.
- Identify data owners and have them set classifications.
- Record classifications in the Data Catalog.
- Implement encryption policies for each data class.
- Implement data retention policies for each data class.
- Require downstream systems to honor classifications.

**Control Data Access**

- Allow data owners to determine access permissions.
- Build user identity solutions for unique identification.
- Implement appropriate data access authorization models (RBAC, dataset-level, column-level).
- Establish an emergency access process.

**Control Access to Workload Infrastructure**

- Prevent unintended access through IAM policies and network isolation.
- Implement least privilege policies for source and downstream systems.
- Monitor infrastructure changes and user activities.
- Secure audit logs.

#### 4.1.6 ML Security

**ML Lifecycle Phases**

- Identify the business goal
- Frame the ML problem
- Process data
- Train, tune, and evaluate
- Deploy model
- Monitor and evaluate

**Security Best Practices for Each Phase**

- **Identify the business goal:** Review software licenses and privacy agreements.
- **Frame the ML problem:** Implement least privilege access and role-based authentication.
- **Process data:** Secure data storage and processing environments, protect sensitive data, enforce data lineage, and retain only relevant data.
- **Train, tune, and evaluate:** Detect risks of transfer learning, secure the ML environment, and protect against data poisoning threats.
- **Deploy model:** Secure model artifacts and ensure secure communication with deployment endpoints.
- **Monitor and evaluate:** Monitor model performance and detect anomalies or malicious activities.

#### 4.1.7 Scaling: An Overview

**Scaling Considerations**

- **Performance goals:** Identify key performance metrics and targets.
- **Data characteristics:** Volume, velocity, variety, and processing requirements.
- **Resource utilization:** Monitor and optimize resource usage.
- **Cost management:** Balance performance with cost efficiency.

#### 4.1.8 Creating a Scalable Infrastructure

**Infrastructure as Code (IaC)**

- **Repeatability:** Consistent deployments across environments.
- **Reusability:** Leveraging tested templates for new deployments.
- **Automation:** Reducing manual configuration and errors.

**AWS Services for IaC**

- **CloudFormation:** Infrastructure provisioning and management using templates.
- **AWS CDK:** Defining infrastructure using programming languages.

#### 4.1.9 Creating Scalable Components

**Scaling Batch Processing**

- **Performance goals:** Completion time, budget constraints, and error thresholds.
- **AWS Glue:**
    - Horizontal scaling: Increasing the number of workers.
    - Vertical scaling: Using larger worker types.
- **File size and compression:** Choose splittable formats and codecs for parallel processing.

**Scaling Stream Processing**

- **Throughput:** Handling high-velocity data.
- **Amazon Kinesis Data Streams:**
    - Automatic shard scaling based on throughput needs.
    - Manual shard adjustments.

#### 4.1.10 Key Takeaways

- Secure data pipelines by implementing strong identity foundations, enabling traceability, and applying security at all layers.
- Apply specific security best practices to analytics and ML workloads throughout their lifecycles.
- Scale data pipelines by identifying performance goals, understanding data characteristics, and utilizing appropriate AWS services and configuration options.
- Infrastructure as code supports security and scalability by enabling repeatable and reusable deployments.

---


## Module 6: AWS Academy Data Engineering - Ingesting and Preparing Data

### 1.1 Ingesting and Preparing Data

#### 1.1.1 Introduction

This module discusses how to ingest and prepare data for analysis.

#### 1.1.2 Module Objectives

Upon completion, you will be able to:

- **Differentiate:** Between Extract, Transform, Load (ETL) and Extract, Load, Transform (ELT) processes.
- **Define:** Data wrangling within the context of data ingestion.
- **Describe:** Key tasks within each data wrangling step:
    - Discovery
    - Structuring
    - Cleaning
    - Enriching
    - Validating
    - Publishing

#### 1.1.3 Module Overview

**Presentation Sections**

- ETL and ELT Comparison
- Data Wrangling Introduction
- Data Discovery
- Data Structuring
- Data Cleaning
- Data Enriching
- Data Validating
- Data Publishing

**Knowledge Checks**

- Online Knowledge Check
- Sample Exam Question

#### 1.1.4 ETL and ELT Comparison

**Ingesting Data**

Data ingestion involves acquiring data from external sources and preparing it for analysis within a pipeline.

**ETL (Extract, Transform, Load)**

- **Extract:** Data from external sources.
- **Transform:** Data into a structured format suitable for analysis.
- **Load:** Transformed data into structured storage (e.g., data warehouse).

**ELT (Extract, Load, Transform)**

- **Extract:** Data from external sources.
- **Load:** Raw data into a data lake (e.g., Amazon S3).
- **Transform:** Data as needed for specific analysis scenarios.

**Benefits of ETL**

- Automated routine transformations.
- Filtering sensitive data upfront.

**Benefits of ELT**

- Faster ingestion by delaying transformations.
- Greater flexibility for data exploration and new queries.

**The Evolving Ingestion Process**

- Modern data architectures blend ETL and ELT approaches.
- Data engineers, analysts, and scientists might perform different transformations at different stages.
- Pipelines should evolve based on usage patterns and insights.

#### 1.1.5 Data Wrangling Introduction

**Data Wrangling**

Transforming raw data from multiple sources into a valuable dataset for analysis.

**Data Wrangling in ETL vs. ELT**

- **Traditional ETL:** Primarily performed by data engineers using batch jobs.
- **ELT:** Enables business users and data scientists to transform data within the data lake before refinement.

**Data Wrangling Steps**

- **Discovery:** Identifying and understanding data sources.
- **Structuring:** Mapping raw data into a suitable format for storage and analysis.
- **Cleaning:** Removing inconsistencies, errors, and unwanted data.
- **Enriching:** Combining data sources and adding valuable information.
- **Validating:** Ensuring data accuracy and integrity.
- **Publishing:** Making the wrangled dataset available for analysis.

#### 1.1.6 Data Discovery

**Tasks in Data Discovery**

- Determine if the source serves the business purpose.
- Understand data organization and access methods.
- Assess required tools and skills.
- Decide whether to proceed with the data source.

**Example Scenario**

- Combining support ticket data from two different systems.
- Identifying relationships, formats, data needs, organization, and available tools.

#### 1.1.7 Data Structuring

**Tasks in Data Structuring**

- Organize storage (folder structure, partitions, access controls).
- Parse source files into a structured format.
- Map source fields to target fields.
- Manage file size (splitting, merging, compression).

**Example Scenario**

- Parsing and mapping fields from a JSON support ticket file.

#### 1.1.8 Data Cleaning

**Tasks in Data Cleaning**

- Removing unwanted data (PII, irrelevant fields, duplicates, corrupted data).
- Filling in missing values.
- Validating and modifying data types.
- Fixing outliers.

**Example Scenario**

- Cleaning support ticket data by replacing missing values, removing corrupted data, and validating data types.

#### 1.1.9 Data Enriching

**Tasks in Data Enriching**

- Merging data sources into a single dataset.
- Adding new fields and calculating new values.

**Example Scenario**

- Combining support ticket data from two sources.
- Adding a sales region field by querying the sales system.

#### 1.1.10 Data Validating

**Tasks in Data Validating**

- Auditing the dataset for expected rows, consistency, formats, data types, duplicates, PII, and outliers.
- Addressing any data integrity issues.

#### 1.1.11 Data Publishing

**Tasks in Data Publishing**

- Determine the target destination (data lake, data warehouse, other data stores).
- Configure access controls (IAM policies, data access permissions).

#### 1.1.12 Key Takeaways

- Ingestion involves extracting, transforming, and loading data into the pipeline.
- ETL transforms data before loading, while ELT loads raw data and transforms it later.
- Data wrangling is a multi-step process to prepare data for analysis.
- Data discovery, structuring, cleaning, enriching, validating, and publishing are key data wrangling steps.

---

## Module 7: AWS Academy Data Engineering: Ingesting by Batch or by Stream

### 2.1 Ingesting by Batch or by Stream

#### 2.1.1 Introduction

This module explores batch and stream ingestion methods, focusing on AWS services like Glue and Kinesis.

#### 2.1.2 Module Objectives

Upon completion, you will be able to:

- **List:** Key tasks for building an ingestion layer.
- **Describe:** AWS services for ingestion tasks.
- **Illustrate:** How AWS Glue automates batch ingestion.
- **Describe:** Amazon Kinesis streaming services and features.
- **Identify:** Configuration options for scaling ingestion in Glue and Kinesis.
- **Describe:** Characteristics of ingesting IoT data using AWS IoT services.

#### 2.1.3 Module Overview

**Presentation Sections**

- Comparing batch and stream ingestion
- Batch ingestion processing
- Purpose-built ingestion tools
- AWS Glue for batch ingestion processing
- Scaling considerations for batch processing
- Kinesis for stream processing
- Scaling considerations for stream processing
- Ingesting IoT data by stream

**Lab**

- Performing ETL on a Dataset by Using AWS Glue

**Knowledge Checks**

- Online knowledge check
- Sample exam question

#### 2.1.4 Comparing Batch and Stream Ingestion

**Batch Ingestion**

- Processes data in batches at intervals (on demand, scheduled, or event-triggered).
- Suitable for large datasets and complex transformations.
- Typically used in ETL processes.

**Stream Ingestion**

- Continuously processes data as it arrives.
- Handles high-velocity data and real-time analytics.

**Data Volume and Velocity as Key Drivers**

- High volume and velocity favor stream processing.
- Lower volume and less time-sensitive data can be handled by batch processing.

#### 2.1.5 Batch Ingestion Processing

**Tasks for Building a Batch Pipeline**

- Connect to the source and select data.
- Define source and target schemas.
- Securely transfer data.
- Perform transformations and load into storage.

**Workflow Orchestration**

- Managing job dependencies and handling failures.

**Key Characteristics for Batch Processing Design**

- **Ease of use:** Developer-friendly tools and interfaces.
- **Data volume and variety:** Handling diverse data types and sources.
- **Orchestration and monitoring:** Tools for managing complex workflows.
- **Scaling and cost management:** Flexibility to scale up and down as needed.

#### 2.1.6 Purpose-built Ingestion Tools

**AWS Services for Batch Ingestion**

- **Amazon AppFlow:** Ingesting data from SaaS applications.
- **AWS Database Migration Service:** Migrating data from relational databases.
- **AWS DataSync:** Ingesting data from file systems.
- **AWS Data Exchange:** Integrating third-party datasets.

**Selecting the Right Tool**

Choose the tool that best matches the data source type and business requirements.

#### 2.1.7 AWS Glue for Batch Ingestion Processing

**Features of AWS Glue**

- **Schema identification:** Automatically generates schemas using crawlers.
- **Data cataloging:** Centralized catalog for data discovery and governance.
- **Job authoring:** Visual interface for creating and managing ETL jobs (AWS Glue Studio).
- **Serverless processing:** Apache Spark-based runtime engine.
- **ETL orchestration:** Workflows for managing complex pipelines.
- **Monitoring and troubleshooting:** CloudWatch integration and job run insights.

**Benefits of AWS Glue**

- Simplifies ETL tasks through automation and visual tools.
- Serverless architecture reduces operational overhead.
- Provides comprehensive monitoring and troubleshooting capabilities.

#### 2.1.8 Scaling Considerations for Batch Processing

**Performance Goals**

- Completion time
- Budget constraints
- Error thresholds

**Scaling AWS Glue Jobs**

- **Horizontal scaling:** Adding more workers for parallel processing.
- **Vertical scaling:** Using larger worker types for memory-intensive tasks.

**File Size and Compression**

- Choose splittable file formats and compression codecs for efficient parallel processing.

#### 2.1.9 Kinesis for Stream Processing

**Tasks for Building a Stream Processing Pipeline**

- **Producers:** Put data records on the stream.
- **Data stream:** Provides durable storage for streaming data.
- **Consumers:** Read and process data from the stream.

**Key Characteristics for Stream Ingestion and Processing**

- **Throughput:** Handling high data volumes.
- **Loose coupling:** Independent and scalable components.
- **Parallel consumers:** Multiple consumers processing the same stream simultaneously.
- **Checkpointing and replay:** Fault tolerance and data durability.

#### 2.1.10 Purpose-built Kinesis Services

**Amazon Kinesis Services for Streaming**

- **Kinesis Data Streams:** Durable storage for streaming data.
- **Kinesis Data Firehose:** Delivering streaming data to data stores and analytics services.
- **Kinesis Data Analytics:** Real-time analytics on streaming data.

**Kinesis Data Streams**

- Handles high-volume, continuous data ingestion.
- Supports multiple producers and consumers.
- Provides encryption and access control for security.

**Kinesis Data Firehose**

- Ingests and delivers streaming data to destinations (S3, Redshift, OpenSearch Service).
- Performs transformations using Lambda functions.

**Kinesis Data Analytics**

- Analyzes streaming data in real time using SQL or Apache Flink.

#### 2.1.11 Scaling Considerations for Stream Processing

**Throughput Management**

- **Kinesis Data Streams:**
    - Automatic shard scaling based on throughput.
    - Manual shard adjustments.

#### 2.1.12 Ingesting IoT Data by Stream

**AWS IoT Services**

- **AWS IoT Core:** Securely connect and manage IoT devices.
- **AWS IoT Analytics:** Process and analyze IoT data.

**Ingesting IoT Data**

- Devices publish data to AWS IoT Core.
- IoT rules route and transform messages.
- Kinesis Data Firehose delivers data to Amazon S3 or other destinations.

#### 2.1.13 Lab: Performing ETL on a Dataset by Using AWS Glue

- Use AWS Glue to perform ETL on a dataset, including creating a crawler, configuring a job, and analyzing results.

#### 2.1.14 Key Takeaways

- Batch ingestion processes data in batches, while stream ingestion handles continuous data flow.
- AWS Glue simplifies batch ingestion with schema identification, job authoring, and orchestration features.
- Amazon Kinesis services provide durable storage, transformation, and analytics capabilities for streaming data.
- Both batch and stream ingestion methods offer scaling options to handle varying data volumes and workloads.
- AWS IoT services enable secure and scalable ingestion of data from IoT devices.

---

## Module 8: AWS Academy Data Engineering - Storing and Organizing Data

### 3.1 Storing and Organizing Data

#### 3.1.1 Introduction

This module explores various storage options for data lakes, data warehouses, and purpose-built databases in AWS.

#### 3.1.2 Module Objectives

Upon completion, you will be able to:

- **Define:** Storage types in a modern data architecture.
- **Distinguish:** Between data storage types.
- **Select:** Data storage options based on specific needs.
- **Implement:** Secure storage practices for cloud-based data.

#### 3.1.3 Module Overview

**Presentation Sections**

- Storage in the modern data architecture
- Data lake storage
- Data warehouse storage
- Purpose-built databases
- Storage in support of the pipeline
- Securing storage

**Lab**

- Storing and Analyzing Data by Using Amazon Redshift

**Knowledge Checks**

- Online knowledge check
- Sample exam question

#### 3.1.4 Storage in the Modern Data Architecture

**Centralized Storage**

- **Data Lake:** Stores raw, unstructured, and structured data using Amazon S3.
- **