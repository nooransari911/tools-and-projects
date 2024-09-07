2024-09-07 14:35:27.504197;

## AWS Academy Data Engineering Student Guide

This document combines and restructures content from multiple AWS Academy Data Engineering modules to create a comprehensive guide. It covers topics such as data-driven organizations, data pipelines, data characteristics, data ingestion and preparation, storage options, big data processing, machine learning, and automation. 

**Table of Contents:**

1. **Module 2: Data-Driven Organizations**
    - Introduction
    - Data-Driven Decisions
        - How Individuals and Organizations Make Decisions
        - Fueling Decisions with Data Science: Data Analytics vs. AI/ML
        - Business Examples and Use Cases
        - Trade-offs and Challenges of Data-Driven Decisions
    - The Data Pipeline: Infrastructure for Data-Driven Decisions
        - Basic Layers and Actions in a Data Pipeline
        - Iterative Processing and Data Wrangling
    - The Role of the Data Engineer and Data Scientist
    - Modern Data Strategies
        - Modernize, Unify, and Innovate
2. **Module 3: Elements of Data**
    - Introduction
    - The Five Vs of Data
        - Volume and Velocity
        - Variety: Data Types and Data Sources
        - Veracity and Value
    - Activities to Improve Veracity and Value
        - Evaluating Veracity, Cleaning Data, Transformations
        - Maintaining Data Integrity and Consistency
3. **Module 4: Design Principles and Patterns for Data Pipelines**
    - Introduction
    - AWS Well-Architected Framework and Lenses
    - The Evolution of Data Architectures
    - Modern Data Architecture on AWS
        - Key Design Considerations
        - AWS Purpose-built Data Stores and Analytics Tools
        - Data Movement and Governance Services
4. **Module 5: Securing and Scaling the Data Pipeline**
    - Introduction
    - Cloud Security Review
        - Shared Responsibility Model
        - Design Principles for Data Security
        - Access Management (Authentication and Authorization)
        - AWS Identity and Access Management (IAM)
        - Data Security (Data at Rest and Data in Transit)
        - AWS Key Management Service (AWS KMS)
        - Logging and Monitoring (CloudTrail and CloudWatch)
    - Security of Analytics Workloads
        - Classify and Protect Data
        - Control Data Access
        - Control Access to Workload Infrastructure
    - Securing the Stream Processing Pipeline
    - ML Security
        - AWS Well-Architected Framework: ML Lens
5. **Module 6: Ingesting and Preparing Data**
    - Introduction
    - ETL and ELT Comparison
        - Ingesting Data: Extract, Transform, Load vs. Extract, Load, Transform
        - Benefits of Each Approach
    - Data Wrangling
        - Steps: Discovery, Structuring, Cleaning, Enriching, Validating, Publishing
        - Example Scenario and Tasks
6. **Module 7: Ingesting by Batch or by Stream**
    - Introduction
    - Comparing Batch and Stream Ingestion
        - Data Flow and Key Drivers
    - Batch Ingestion Processing
        - Tasks, Key Characteristics, and Design Considerations
    - Purpose-built Ingestion Tools
        - Amazon AppFlow, AWS Database Migration Service, AWS DataSync, AWS Data Exchange
    - AWS Glue for Batch Ingestion Processing
        - Features: Schema Identification, Data Cataloging, Job Authoring, Serverless Processing, Orchestration, Monitoring
    - Scaling Considerations for Batch Processing
        - Scaling and Cost Management in AWS Glue
        - Horizontal and Vertical Scaling with AWS Glue Workers
        - Trade-offs of File Size and Compression
    - Kinesis for Stream Processing
        - Tasks and Key Characteristics
    - Purpose-built Kinesis Services
        - Kinesis Data Streams: Ingestion, Storage, Consumers
        - Kinesis Data Firehose: Ingestion, Transformation, Delivery
    - Scaling Considerations for Stream Processing
    - Ingesting IoT Data by Stream
7. **Module 8: Storing and Organizing Data**
    - Introduction
    - Storage in the Modern Data Architecture
    - Types of Cloud Storage: Block, File, and Object
    - Data Lake Storage
        - Amazon Simple Storage Service (Amazon S3)
        - Amazon S3 Storage Classes
        - Example Architecture of a Data Lake
        - AWS Lake Formation
    - Data Warehouse Storage
        - Amazon Redshift
        - Example Architecture of a Data Warehouse
        - Amazon Redshift Spectrum
    - Purpose-Built Databases
        - Factors in Choosing a Database
        - Workloads: Transactional, Analytical, Caching
        - Data Models: Relational, Key-Value, Document, Graph
        - Performance, Operations Burden, Geographic Requirements
        - Common Use Cases and AWS Services
    - Storage in Support of the Pipeline
        - Comparing Storage in ETL and ELT Pipelines
        - Examples: ETL and ELT Architectures
    - Securing Storage
        - Access Policy Options
        - Encryption
8. **Module 9: Processing Big Data**
    - Introduction
    - Big Data Processing Concepts
        - Batch vs. Streaming Data Processing
    - Frameworks that Support Big Data Processing
        - Apache Hadoop, Apache Spark, Apache Flink, Apache Hive, Presto, Apache Pig
    - Apache Hadoop
        - Characteristics, Benefits, Challenges
        - Hadoop Distributed File System (HDFS)
        - Yet Another Resource Negotiator (YARN)
        - Hadoop MapReduce
        - Common Hadoop Frameworks
    - Apache Spark
        - Characteristics and Benefits
        - Spark Clusters and Components
    - Amazon EMR
        - Characteristics and Benefits
        - Clusters and Nodes
        - Amazon EMR Service Architecture
        - Processing Data in Amazon EMR
    - Managing Amazon EMR Clusters
        - Launching and Configuring Clusters
        - Cluster Characteristics (Long-Running vs. Transient)
        - Connecting to Your Cluster
        - Scaling Your Cluster Resources
    - Apache Hudi
9. **Module 10: Processing Data for ML**
    - Introduction
    - ML Concepts
        - Comparing ML to Traditional Analytics
        - ML Models and Algorithms
        - Types of ML Models (Supervised, Unsupervised, Reinforcement)
        - Subcategories of AI (Neural Networks, Deep Learning, Generative AI)
        - The Evolution of ML
        - ML Data Concepts (Labels, Features, Samples)
    - The ML Lifecycle
        - Phases: Frame ML Problem, Process Data, Develop Model, Deploy Model, Monitor and Evaluate
        - Common Roles: Data Scientist, Data Engineer, Operations Team, AI/ML Architect
    - Framing the ML Problem
        - Working Backwards from the Business Problem
        - Key Steps and Considerations
        - Determining if ML is the Best Approach
    - Collecting Data
        - Key Steps and Considerations
        - Protecting Data Veracity
        - Collecting Enough Data for Training and Testing
    - Applying Labels to Training Data
        - Data Labeling Process
        - Amazon SageMaker Ground Truth
    - Preprocessing Data
        - Preprocessing Strategies
        - Exploratory Data Analysis
    - Feature Engineering
        - Feature Creation, Transformation, Extraction, Selection
        - Dimensionality Reduction
    - Developing a Model
        - Model Training, Tuning, and Evaluation
    - Deploying a Model
        - Deployment Options
    - Monitoring and Evaluating a Model
        - Key Metrics
    - AWS ML Infrastructure Services
        - Amazon SageMaker
    - Generative AI and Amazon CodeWhisperer
    - Other AWS AI/ML Services
10. **Module 11: Analyzing and Visualizing Data**
    - Introduction
    - Considering Factors That Influence Tool Selection
        - Business Needs (Granularity of Insight, Visualizing Insights)
        - Data Characteristics (Volume, Velocity, Variety, Veracity, Value)
        - Access to Data (Authorization Level, Roles and Functions)
    - Comparing AWS Tools and Services
        - Amazon Athena (Interactive Query Service)
        - Amazon QuickSight (BI Service)
        - Amazon OpenSearch Service (Search and Analytics Engine)
    - Selecting Tools for a Gaming Analytics Use Case
        - Personas: Analyst, Business User, DevOps Engineer
        - Example Pipeline and Use Cases
11. **Module 12: Automating the Pipeline**
    - Introduction
    - Automating Infrastructure Deployment
        - Benefits of Automation
        - Infrastructure as Code (IaC)
    - CI/CD
        - Continuous Integration (CI)
        - Continuous Delivery (CD)
        - Continuous Deployment
    - Automating with AWS Step Functions
        - Features and Integration with Athena
        - How Step Functions Works (Workflows, States, Tasks)
        - Step Functions Interface (States Browser, Canvas, Inspector)
        - State Types (Task, Pass, Choice, Parallel, Wait, Map, Succeed, Fail)
12. **Module 13: Bridging to Certification**
    - Introduction
    - AWS Certification Overview
        - AWS Certified Data Analytics – Specialty
        - AWS Certified Machine Learning – Specialty
    - Exam Readiness Resources
        - Exam Guides, Sample Questions, AWS Well-Architected, Whitepapers, FAQs
    - Exam Readiness Training
    - Additional Resources
        - AWS Training and Certification Portal
        - AWS Skill Builder
        - Official Practice Question Sets
        - AWS Documentation
13. **Module 14: IoT Use Case**
    - The Business Problem (E-Bike Rental Program)
    - The IoT Reference Architecture
    - Ingestion and Processing
        - Connecting Devices to AWS IoT Core
        - Configuring IoT Rules
        - Configuring Kinesis Data Firehose Delivery Stream
    - Storage
        - Organizing and Cataloging Data
    - Analysis and Visualization
        - Querying and Visualizing Data
        - Geospatial Visualization


## 1. Module 2: Data-Driven Organizations 

### 1.1 Introduction 

This module provides an overview of data-driven organizations, the role of data science in decision-making, the concept of data pipelines, and modern data strategies.

### 1.2 Data-Driven Decisions 

#### 1.2.1 How Individuals and Organizations Make Decisions 

Data-driven organizations leverage data science to inform their decisions. This has become increasingly common as the volume of available data has grown and the cost of technology to analyze data has decreased.

#### 1.2.2 Fueling Decisions with Data Science: Data Analytics vs. AI/ML 

There are two main approaches to data science: 
- **Data analytics:** involves the systematic analysis of large datasets to identify patterns and trends. It relies on programming logic and statistical methods. Data analytics is suitable for structured data with a limited number of variables.
- **Artificial Intelligence (AI) and Machine Learning (ML):** AI/ML models use mathematical algorithms to learn from data and make predictions. They can handle unstructured data and complex variables. The key difference is that AI/ML learns from examples within data, making it ideal for complex situations where traditional rule-based logic is difficult to define.

#### 1.2.3 Business Examples and Use Cases 

Here are some examples of how organizations use data science: 
- **Credit card companies:** use AI/ML to detect fraudulent transactions in real-time. 
- **Ecommerce sites:** personalize the user experience and recommend products using AI/ML.
- **Healthcare providers:** utilize data analytics to identify patients at risk of certain diseases. 
- **Farmers:** leverage IoT data and ML models to optimize planting, watering, and harvesting decisions. 

#### 1.2.4 Trade-offs and Challenges of Data-Driven Decisions 

While data-driven decision-making offers significant benefits, there are also trade-offs and challenges: 
- **Cost:** Storing and processing large amounts of data can be expensive. 
- **Speed:** Analyzing complex datasets can be time-consuming, potentially delaying decision-making.
- **Accuracy:** The quality of the data and the chosen analytical approach significantly impact the accuracy of the insights and predictions.
- **Security:** Protecting the privacy and security of data is critical, especially when dealing with sensitive information.
- **Unstructured data:**  Dealing with the increasing volume of unstructured data requires specialized tools and techniques.

### 1.3 The Data Pipeline: Infrastructure for Data-Driven Decisions 

#### 1.3.1 Basic Layers and Actions in a Data Pipeline 

A data pipeline provides the infrastructure for data-driven decision-making. It typically includes the following layers:

- **Ingestion:** The process of collecting data from various sources. 
- **Storage:** Storing data in a secure and scalable manner. 
- **Processing:** Transforming, cleaning, and preparing data for analysis. 
- **Analysis & Visualization:** Analyzing data to extract insights and presenting them in a user-friendly format. 

#### 1.3.2 Iterative Processing and Data Wrangling 

Data processing within a pipeline is often iterative, involving multiple rounds of refinement and evaluation to improve the quality of insights. Data wrangling encompasses the tasks involved in transforming data as it moves through the pipeline, including:

- **Discovery:** Understanding the characteristics and structure of data sources. 
- **Cleaning:**  Removing inconsistencies, duplicates, and errors.
- **Normalization:** Transforming data into a consistent format. 
- **Enrichment:**  Adding additional data or calculating new values to enhance the dataset. 
- **Transformation:**  Converting data into a format suitable for analysis. 

### 1.4 The Role of the Data Engineer and Data Scientist 

Data engineers are responsible for designing, building, and maintaining the data pipeline infrastructure, ensuring efficient data ingestion, storage, and processing. They focus on the technical aspects of data management and work closely with data scientists to understand their data requirements.

Data scientists are responsible for analyzing data, developing ML models, and extracting insights to inform decision-making. They work with data engineers to ensure they have access to the necessary data and tools to perform their analysis. 

### 1.5 Modern Data Strategies 

#### 1.5.1 Modernize, Unify, and Innovate 

Organizations seeking to become data-driven should adopt these key strategies:

- **Modernize:** Migrate from on-premises infrastructure to cloud-based services, leveraging purpose-built tools and data stores for greater agility and cost-effectiveness. 
- **Unify:** Break down data silos, create a single source of truth for data, and democratize access to data across the organization, enabling users to directly access and analyze relevant data. 
- **Innovate:**  Embrace AI/ML to discover new insights from vast amounts of data, move from reactive to proactive decision-making, and leverage cloud services with AI/ML features to empower users with varying levels of technical expertise. 

## 2. Module 3: Elements of Data

### 2.1 Introduction

This module introduces the five Vs of data and their impact on data pipeline design. It also discusses methods for improving data veracity and value.

### 2.2 The Five Vs of Data

#### 2.2.1 Volume and Velocity

- **Volume:** refers to the amount of data that needs to be processed.
- **Velocity:** refers to the speed at which data enters and moves through the pipeline.

These factors drive the scaling and throughput requirements for the pipeline. They impact decisions regarding ingestion methods, storage types, processing power, and analysis techniques.

#### 2.2.2 Variety: Data Types and Data Sources

- **Variety:** refers to the different types and formats of data.

**Data Types:**
- **Structured:** Organized in rows and columns, with a defined schema (e.g., relational database tables).
- **Semi-structured:** Has recognizable elements and attributes, but lacks a rigid schema (e.g., CSV, JSON, XML).
- **Unstructured:** Does not have a predefined structure (e.g., images, videos, audio files).

**Data Sources:**
- **Organizational Stores:** Databases and file systems owned and managed by the organization.
- **Public Datasets:** Data aggregated about a specific topic (e.g., census data, health data).
- **Time-Series Data:** Data generated continuously by events or sensors (e.g., IoT devices, clickstream data).

Combining different data types and sources can enrich analysis, but it also introduces complexity in processing and managing data veracity.

#### 2.2.3 Veracity and Value

- **Veracity:** refers to the accuracy, precision, and trustworthiness of data.
- **Value:** refers to the insights and actions derived from data.

Data veracity is critical because bad data can lead to poor decisions. Maintaining data integrity requires evaluating the trustworthiness of sources, cleaning and transforming data, and preventing unwanted changes. 

### 2.3 Activities to Improve Veracity and Value

#### 2.3.1 Evaluating Veracity, Cleaning Data, Transformations

- **Evaluating Veracity:** Ask questions about the source data's reliability, lineage, and potential biases.
- **Cleaning Data:** 
    - Define a consistent understanding of "clean data".
    - Trace errors back to their source.
    - Make changes thoughtfully, understanding their impact on data meaning.
    - Retain raw data if it holds business value.
- **Transformations:** Convert data into a consistent format, handle missing values, and fix outliers. Transformations can be simple (e.g., renaming columns) or complex (e.g., aggregating data, joining tables).

#### 2.3.2 Maintaining Data Integrity and Consistency

- **Secure all layers of the pipeline:** Implement security measures at each stage to prevent unauthorized access and data breaches.
- **Grant least privilege access:**  Limit user permissions to only the resources and actions necessary to perform their tasks.
- **Apply best practices:** Follow industry best practices for data management, security, and compliance.
- **Keep audit trails:** Track changes to data and configurations for accountability and traceability.
- **Implement data governance:** Define policies, processes, and tools to manage data quality, security, and access.
- **Maintain a single source of truth:**  Ensure data consistency by designating one data store as the authoritative source for each data element.

## 3. Module 4: Design Principles and Patterns for Data Pipelines

### 3.1 Introduction

This module explores design principles and patterns for building robust and scalable data pipelines. It covers the AWS Well-Architected Framework, the evolution of data architectures, and the components of a modern data architecture on AWS.

### 3.2 AWS Well-Architected Framework and Lenses

- The **AWS Well-Architected Framework** provides best practices and guidance for designing and operating cloud workloads across six pillars:
    - Operational Excellence
    - Security
    - Reliability
    - Performance Efficiency
    - Cost Optimization
    - Sustainability

- **Lenses** extend the framework's guidance to specific domains, such as data analytics and machine learning.

- The **Data Analytics Lens** provides specific recommendations for designing, building, and operating analytics workloads, addressing factors such as data volume, velocity, variety, veracity, and value.

### 3.3 The Evolution of Data Architectures

Data stores and architectures have evolved over time to accommodate the growing volume, variety, and velocity of data:

- **Hierarchical Databases:** Limited ability to define relationships among data.
- **Relational Databases:** Well-defined schemas, optimized for structured data.
- **Data Warehouses:** Optimized for analytical queries and reporting.
- **Non-relational Databases:** Flexible schemas, suitable for semi-structured and unstructured data.
- **Big Data Systems:** Distributed processing frameworks for handling massive datasets.
- **Lambda Architecture:** Combines batch and stream processing for near real-time insights.
- **Data Lakes:** Centralized repositories for storing all types of data, regardless of structure.

### 3.4 Modern Data Architecture on AWS

A modern data architecture on AWS utilizes a centralized data lake (Amazon S3) integrated with purpose-built data stores and analytics tools:

#### 3.4.1 Key Design Considerations

- **Scalable Data Lake:** Amazon S3 provides a highly scalable and durable storage solution for the data lake.
- **Performant and Cost-Effective Components:** Choose services that balance performance and cost for specific use cases.
- **Seamless Data Movement:** Services like AWS Glue facilitate data movement and transformation between data stores.
- **Unified Governance:** AWS Lake Formation simplifies data lake management, including security, cataloging, and access control.

#### 3.4.2 AWS Purpose-built Data Stores and Analytics Tools

- **Amazon Redshift:** Fully managed data warehouse service.
- **Amazon OpenSearch Service:** Search and analytics engine for real-time analytics, including log analytics.
- **Amazon EMR:** Big data processing framework.
- **Amazon Aurora:** Cloud-native relational database engine.
- **Amazon DynamoDB:** Fully managed NoSQL database service.
- **Amazon SageMaker:** AI/ML platform.

#### 3.4.3 Data Movement and Governance Services

- **AWS Glue:** Serverless data integration service for ETL, data cataloging, and schema discovery.
- **AWS Lake Formation:**  Simplifies data lake management, security, and access control.

## 4. Module 5: Securing and Scaling the Data Pipeline

### 4.1 Introduction

This module focuses on securing and scaling data pipelines. It covers cloud security best practices, AWS services for security and scaling, and infrastructure as code.

### 4.2 Cloud Security Review

#### 4.2.1 Shared Responsibility Model

- AWS is responsible for the security **of** the cloud, including the underlying infrastructure.
- Customers are responsible for security **in** the cloud, including configuring services, managing access control, and protecting data.

#### 4.2.2 Design Principles for Data Security

- Implement a strong identity foundation
- Enable traceability
- Apply security at all layers
- Automate security best practices
- Protect data in transit and at rest
- Keep people away from data
- Prepare for security events

#### 4.2.3 Access Management (Authentication and Authorization)

- **Authentication:** Verifies the identity of users or systems requesting access.
- **Authorization:**  Determines what actions authenticated entities are permitted to perform.
- **Principle of Least Privilege:** Grant only the minimum necessary permissions.

#### 4.2.4 AWS Identity and Access Management (IAM)

- **IAM:** A web service for managing access to AWS resources.
- **Features:** Granular permissions, federated identity management, multi-factor authentication (MFA), auditing.

#### 4.2.5 Data Security (Data at Rest and Data in Transit)

- **Data at Rest:** Data stored in non-volatile storage.
- **Data in Transit:**  Data moving between systems or services.
- **Protection Mechanisms:** Encryption, access control, network security.

#### 4.2.6 AWS Key Management Service (AWS KMS)

- **AWS KMS:** A managed service for creating and managing cryptographic keys.
- **Features:** Hardware security modules (HSMs), integration with AWS services, usage policies, auditing.

#### 4.2.7 Logging and Monitoring (CloudTrail and CloudWatch)

- **AWS CloudTrail:** A service that logs API calls and events within your AWS account, providing an audit trail of actions.
- **Amazon CloudWatch:**  A monitoring and observability service that collects and tracks metrics, logs, and events.

### 4.3 Security of Analytics Workloads

- Classify and Protect Data: Based on sensitivity and compliance requirements.
- Control Data Access:  Implement least privilege access, use IAM roles and policies, control access at the dataset and column level.
- Control Access to Workload Infrastructure:  Secure networks, monitor infrastructure changes, secure audit logs.

### 4.4 Securing the Stream Processing Pipeline

- Apply the security best practices discussed in the previous section to specific components of a stream processing pipeline, such as Amazon Kinesis Data Streams, Amazon S3, and AWS Lambda.

### 4.5 ML Security

#### 4.5.1 AWS Well-Architected Framework: ML Lens

- The ML Lens provides security guidance for each phase of the ML lifecycle:
    - Identify the Business Goal
    - Frame the ML Problem
    - Process Data
    - Train, Tune, and Evaluate
    - Deploy Model
    - Monitor and Evaluate

## 5. Module 6: Ingesting and Preparing Data

### 5.1 Introduction

This module explores the processes involved in ingesting and preparing data for use in analytics pipelines. It covers ETL vs. ELT approaches and the steps involved in data wrangling.

### 5.2 ETL and ELT Comparison

#### 5.2.1 Ingesting Data: Extract, Transform, Load vs. Extract, Load, Transform

- **ETL (Extract, Transform, Load):**  Traditional approach, where data is extracted, transformed into a structured format, and then loaded into a data warehouse.
- **ELT (Extract, Load, Transform):**  Modern approach, where data is extracted, loaded into a data lake in its raw form, and transformed as needed for specific use cases.

#### 5.2.2 Benefits of Each Approach

- **ETL:** Automated routine transformations, filtering sensitive data upfront.
- **ELT:**  Faster ingestion, greater flexibility for data exploration.

### 5.3 Data Wrangling

#### 5.3.1 Steps: Discovery, Structuring, Cleaning, Enriching, Validating, Publishing

- **Discovery:** Understanding the characteristics and structure of data sources.
- **Structuring:** Mapping data into a suitable format for storage and analysis.
- **Cleaning:** Removing inconsistencies, duplicates, and errors.
- **Enriching:**  Adding additional data or calculating new values to enhance the dataset.
- **Validating:**  Ensuring the accuracy and integrity of the prepared data.
- **Publishing:**  Making the prepared data available for analysis or further processing.

#### 5.3.2 Example Scenario and Tasks

- A practical example illustrating the data wrangling process, including tasks performed at each step.

## 6. Module 7: Ingesting by Batch or by Stream

### 6.1 Introduction

This module covers concepts related to ingesting data using batch and stream processing methods.

### 6.2 Comparing Batch and Stream Ingestion

#### 6.2.1 Data Flow and Key Drivers

- **Batch Ingestion:**  Processes data in batches, suitable for periodic or scheduled data loads.
- **Stream Ingestion:**  Processes data continuously in real-time, suitable for high-velocity data sources.
- **Key Drivers:** Data volume, velocity, and the need for real-time analysis influence the choice of ingestion method.

### 6.3 Batch Ingestion Processing

#### 6.3.1 Tasks, Key Characteristics, and Design Considerations

- **Tasks:** Scripting, job creation, workflow orchestration.
- **Key Characteristics:**  Ease of use, data volume and variety, orchestration and monitoring, scaling and cost management.

### 6.4 Purpose-built Ingestion Tools

- **Amazon AppFlow:** Ingesting data from SaaS applications.
- **AWS Database Migration Service (AWS DMS):** Ingesting data from relational databases.
- **AWS DataSync:**  Ingesting data from file systems.
- **AWS Data Exchange:**  Integrating third-party datasets.

### 6.5 AWS Glue for Batch Ingestion Processing

#### 6.5.1 Features: Schema Identification, Data Cataloging, Job Authoring, Serverless Processing, Orchestration, Monitoring

- **AWS Glue:** A serverless data integration service simplifying ETL tasks.
- **Features:**
    - Schema identification and data cataloging using crawlers.
    - Job authoring and management using AWS Glue Studio.
    - Serverless job processing using the AWS Glue Spark runtime engine.
    - ETL orchestration using workflows.
    - Monitoring and troubleshooting using CloudWatch and job run insights.

### 6.6 Scaling Considerations for Batch Processing

#### 6.6.1 Scaling and Cost Management in AWS Glue

- **Performance Goals:** Focus on completion time, budget, or accuracy thresholds.
- **Metrics:**  Use metrics to identify bottlenecks and tune performance.

#### 6.6.2 Horizontal and Vertical Scaling with AWS Glue Workers

- **Horizontal Scaling:** Adding more workers for parallel processing.
- **Vertical Scaling:**  Choosing a larger worker type for more resources per worker.

#### 6.6.3 Trade-offs of File Size and Compression

- Choose file formats and compression codecs that support splitting for efficient parallel processing with AWS Glue.

### 6.7 Kinesis for Stream Processing

#### 6.7.1 Tasks and Key Characteristics

- **Tasks:** Producer applications, stream configuration, consumer applications.
- **Key Characteristics:**  Throughput, loose coupling, parallel consumers, checkpointing and replay.

### 6.8 Purpose-built Kinesis Services

#### 6.8.1 Kinesis Data Streams: Ingestion, Storage, Consumers

- **Kinesis Data Streams:** A service for collecting and processing real-time streaming data.
- **Producers:**  Applications or services that write data to the stream.
- **Consumers:**  Applications or services that read and process data from the stream.

#### 6.8.2 Kinesis Data Firehose: Ingestion, Transformation, Delivery

- **Kinesis Data Firehose:** A service for delivering streaming data to data lakes, data stores, and analytics services.
- **Features:**  Data aggregation, transformation using Lambda functions, format conversion, compression.

### 6.9 Scaling Considerations for Stream Processing

- **Kinesis Data Streams:** Scales automatically based on throughput requirements.
- **Kinesis Data Firehose:**  Scales based on the configured delivery stream settings.

### 6.10 Ingesting IoT Data by Stream

- **AWS IoT Core:** A service for connecting and managing IoT devices.
- **AWS IoT Analytics:**  A service for analyzing IoT data.
- **Integration with Kinesis:** AWS IoT Core can integrate with Kinesis Data Streams for real-time data ingestion and processing.

## 7. Module 8: Storing and Organizing Data

### 7.1 Introduction

This module explores various storage options used in modern data architectures, including data lakes, data warehouses, and purpose-built databases. It also covers securing storage.

### 7.2 Storage in the Modern Data Architecture

- Storage is central to a modern data architecture, typically relying on a combination of data lakes, data warehouses, and purpose-built databases.

### 7.3 Types of Cloud Storage: Block, File, and Object

- **Block Storage:** Dedicated, low-latency storage for individual instances (e.g., Amazon EBS).
- **File Storage:**  Shared storage accessible over a network, often using protocols like NFS or SMB (e.g., Amazon EFS).
- **Object Storage:** Stores data as objects, each with a unique identifier, metadata, and access control (e.g., Amazon S3).

### 7.4 Data Lake Storage

#### 7.4.1 Amazon Simple Storage Service (Amazon S3)

- **Amazon S3:** A highly scalable and durable object storage service, often used as the foundation for data lakes.
- **Features:** 
    - Storage classes for different access patterns and cost optimization.
    - Strong consistency for data integrity.
    - Multipart upload for large objects.

#### 7.4.2 Amazon S3 Storage Classes

- **S3 Standard:** Frequently accessed data.
- **S3 Intelligent-Tiering:** Data with unknown or changing access patterns.
- **S3 Standard-Infrequent Access (S3 Standard-IA):** Less frequently accessed data.
- **S3 One Zone-Infrequent Access (S3 One Zone-IA):**  Less frequently accessed data, stored in a single availability zone.
- **S3 Glacier Instant Retrieval:** Archive data requiring immediate access.
- **S3 Glacier Flexible Retrieval:**  Rarely accessed long-term data.
- **S3 Glacier Deep Archive:**  Long-term archive and digital preservation.
- **S3 Outposts:**  Storing S3 data on-premises.

#### 7.4.3 Example Architecture of a Data Lake

- An example architecture illustrating the integration of Amazon S3 with other services for a data lake solution.

#### 7.4.4 AWS Lake Formation

- **AWS Lake Formation:** A service simplifying data lake management, security, and access control.
- **Features:** 
    - Centralized permissions model.
    - Data cataloging and labeling.
    - Data transformation and deduplication.
    - Storage optimization.
    - Governed tables for transactional consistency.

### 7.5 Data Warehouse Storage

#### 7.5.1 Amazon Redshift

- **Amazon Redshift:** A fully managed, petabyte-scale data warehouse service.
- **Features:** 
    - Cluster-based architecture with different node types for performance optimization.
    - Support for structured and semi-structured data.
    - Integration with other AWS services.

#### 7.5.2 Example Architecture of a Data Warehouse

- An example architecture illustrating the components of a data warehouse using Amazon Redshift.

#### 7.5.3 Amazon Redshift Spectrum

- **Amazon Redshift Spectrum:** Enables querying data directly in Amazon S3 from Amazon Redshift.
- **Benefits:** 
    - Avoids data duplication and movement.
    - Leverages the scalability and cost-effectiveness of Amazon S3.

### 7.6 Purpose-Built Databases

#### 7.6.1 Factors in Choosing a Database

- **Workload:** Transactional, analytical, caching.
- **Data Shape:** Relational, key-value, document, graph.
- **Performance:** Speed, scalability, latency.
- **Operations Burden:** Management, backups, upgrades.
- **Geographic Requirements:**  Data residency, latency.

#### 7.6.2 Workloads: Transactional, Analytical, Caching

- **Transactional:** High volume of short-lived operations, often used for user-facing applications.
- **Analytical:**  Aggregating and summarizing large amounts of data, typically used for reporting and BI.
- **Caching:** Storing frequently accessed data for faster retrieval, reducing load on primary databases.

#### 7.6.3 Data Models: Relational, Key-Value, Document, Graph

- **Relational:** Structured data organized in tables with relationships (e.g., Amazon Aurora, Amazon RDS).
- **Key-Value:**  Data stored as key-value pairs, suitable for high-volume, low-latency access (e.g., Amazon DynamoDB).
- **Document:**  Data stored as JSON-like documents, allowing for flexible schemas (e.g., Amazon DocumentDB).
- **Graph:** Data represented as nodes and relationships, suitable for analyzing connected data (e.g., Amazon Neptune).

#### 7.6.4 Performance, Operations Burden, Geographic Requirements

- **Performance:** Choose a database that meets your application's speed and scalability requirements.
- **Operations Burden:** Consider the level of management, backups, and upgrades required for the database.
- **Geographic Requirements:** Select a database that supports your data residency and latency needs.

#### 7.6.5 Common Use Cases and AWS Services

- Examples of common database use cases and the AWS services that are suitable for each use case.

### 7.7 Storage in Support of the Pipeline

#### 7.7.1 Comparing Storage in ETL and ELT Pipelines

- **ETL:**  Typically uses staging areas or temporary storage for data transformation before loading into a data warehouse.
- **ELT:**  Loads raw data directly into a data lake, leveraging the storage layer for transformation and processing.

#### 7.7.2 Examples: ETL and ELT Architectures

- Illustrative examples of ETL and ELT architectures, highlighting the role of storage in each approach.

### 7.8 Securing Storage

#### 7.8.1 Access Policy Options

- **Resource-Based Policies:** Bucket policies and ACLs for controlling access to S3 buckets and objects.
- **User Policies:**  IAM policies for managing access to AWS services and resources.

#### 7.8.2 Encryption

- **Server-Side Encryption:**  Encrypting data at rest using AWS KMS.
- **Client-Side Encryption:**  Encrypting data before uploading it to Amazon S3, managing keys independently.

## 8. Module 9: Processing Big Data

### 8.1 Introduction

This module focuses on processing big data using frameworks like Apache Hadoop and Apache Spark. It covers Amazon EMR for managing big data clusters.

### 8.2 Big Data Processing Concepts

#### 8.2.1 Batch vs. Streaming Data Processing

- **Batch Data Processing:**  Processing large datasets in batches, typically for infrequent access and deep analysis.
- **Streaming Data Processing:**  Processing continuous data streams in real-time, often for immediate insights and actions.

### 8.3 Frameworks that Support Big Data Processing

- **Apache Hadoop:** A distributed processing framework for batch data.
- **Apache Spark:**  A distributed processing framework for batch, streaming, and interactive data analysis.
- **Apache Flink:** A streaming data flow engine for real-time processing.
- **Apache Hive:**  A SQL-like data warehouse system built on Hadoop.
- **Presto:**  An in-memory SQL query engine for interactive analysis.
- **Apache Pig:**  A high-level data flow language for parallel processing.

### 8.4 Apache Hadoop

#### 8.4.1 Characteristics, Benefits, Challenges

- **Characteristics:** Open-source, distributed processing framework.
- **Benefits:**  Scalability, fault tolerance, cost-effectiveness, ability to handle unstructured data.
- **Challenges:**  Complexity, security concerns, potential stability issues.

#### 8.4.2 Hadoop Distributed File System (HDFS)

- **HDFS:** A distributed file system designed for storing large datasets across a cluster of nodes.
- **Features:** 
    - Data blocks for splitting data across nodes.
    - Replication for fault tolerance.
    - NameNode for metadata management.
    - DataNodes for