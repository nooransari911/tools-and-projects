2024-09-06 17:23:24.180956;

# AWS Academy Cloud Architecting

## Module 13: Building Microservices and Serverless Architectures

### 1. Contents

- **Module 13: Building Microservices and Serverless Architectures** 4

### 2. Module Overview

#### 2.1. Sections

1. Architectural Need
2. Introducing Microservices
3. Building Microservice Applications with AWS Container Services
4. Introducing Serverless Architectures
5. Building Serverless Architectures with AWS Lambda
6. Extending Serverless Architectures with Amazon API Gateway
7. Orchestrating Microservices with AWS Step Functions

#### 2.2. Demonstrations

- Creating an AWS Lambda function
- Using AWS Lambda with Amazon S3

#### 2.3. Labs

- **(Optional)** Guided Lab 1: Breaking a Monolithic Node.js Application into Microservices
- Guided Lab 2: Implementing a Serverless Architecture on AWS
- Challenge Lab: Implementing a Serverless Architecture for the Café

#### 2.4. Knowledge Check

This module covers the following topics:

- Architectural need
- Introducing microservices
- Building microservice applications with AWS container services
- Introducing serverless architectures
- Building serverless architectures with AWS Lambda
- Extending serverless architectures with Amazon API Gateway
- Orchestrating microservices with AWS Step Functions

**In addition to the above sections, this module includes:**

- Two AWS Lambda demonstrations
- An optional guided lab where you refactor a monolithic application into microservices
- A guided lab where you implement a serverless architecture on AWS with Amazon S3, AWS Lambda, Amazon DynamoDB, and Amazon SNS
- A challenge lab where you use AWS Lambda and Amazon Simple Notification Service (Amazon SNS) to generate and send a daily sales report for the café.

Finally, you will be asked to complete a knowledge check that will test your understanding of key concepts covered in this module.

### 3. Module Objectives

At the end of this module, you should be able to:

- Indicate the characteristics of microservices
- Refactor a monolithic application into microservices and use Amazon ECS to deploy the containerized microservices
- Explain serverless architecture
- Implement a serverless architecture with AWS Lambda
- Describe a common architecture for Amazon API Gateway
- Describe the types of workflows that AWS Step Functions supports

### 4. Section 1: Architectural Need

#### 4.1. Introducing Section 1: Architectural Need

#### 4.2. Café Business Requirement

The café wants to get daily reports via email about all the orders that were placed on the website. They want this information so they can anticipate demand and bake the correct number of desserts going forward (reducing waste). They also want to identify any patterns in their business (analytics).

Frank and Martha want to get daily reports via email about all the orders that were placed on the website. Frank wants to anticipate demand so he can bake the correct number of desserts going forward (reducing waste). Martha wants to identify any patterns in the café's business (analytics). Currently, Sofía has set up a cron job on the web server instance that sends these daily order report email messages to Frank and Martha. However, the cron job is resource-intensive and reduces web server performance.

Olivia advises Sofía and Nikhil that non-business-critical reporting tasks should be kept separate. Sofía and Nikhil want to further decouple the architecture and move the cron job into a managed, serverless environment that will scale well and reduce costs.

### 5. Section 2: Introducing Microservices

#### 5.1. Introducing Section 2: Introducing Microservices

#### 5.2. What are Microservices?

Applications that are composed of independent services that communicate over well-defined APIs.

Microservices are an architectural and organizational approach to software development where applications are composed of independent services that communicate over well-defined application programming interfaces (APIs). This approach is designed to speed up deployment cycles.

The microservices approach fosters innovation and ownership, and improves the maintainability and scalability of software applications.

#### 5.3. Monolithic versus Microservice Applications

To understand the benefits of microservices, consider first a monolithic application.

In the example on the left, the three processes (users, topics, and messages) of a monolithic forum application are tightly coupled. They run as a single service. If one process of the application experiences a spike in demand, the entire architecture must be scaled. Adding or improving features becomes more complex as the code base grows, which limits experimentation and makes it difficult to implement new ideas. The availability of monolithic applications is also at risk because many dependent and tightly coupled processes increase the impact of a single process failure.

Now, suppose that the same application runs in a microservice architecture. Each process of the application is built as an independent component that runs as a service. The services communicate by using lightweight API operations. Each service performs a single function that can support multiple applications. Because the services run independently, they can be updated, deployed, and scaled to meet the demand for specific functions of an application.

A microservice architecture provides much quicker iteration, automation, and overall agility. Start fast, fail fast, and recover fast.

For an overview of microservices on AWS, see What are Microservices?

#### 5.4. Characteristics of Microservices

Microservices share some common characteristics:

- **Decentralized** – Microservice architectures are distributed systems with decentralized data management. They don't rely on a unifying schema in a central database. Each microservice has its own view about data models. Microservices are also decentralized in the way they are developed, deployed, managed, and operated.
- **Independent** – Each component service in a microservice architecture can be changed, upgraded, or replaced independently without affecting the function of other services. Services do not need to share any of their code or implementation with other services. Similarly, the teams responsible for different microservices can act independently from each other.
- **Specialized** - Each component service is designed for a set of capabilities and focuses on a specific domain. If the code for a particular component service reaches a certain level of complexity, then the service can be split into two or more services.
- **Polyglot** - Microservices don't follow a single approach. Teams have the freedom to choose the best tool for their specific problem. As a consequence, microservice architectures take a heterogeneous approach to operating systems, programming languages, data stores, and tools. This approach is called polyglot persistence and programming.
- **Black boxes** - Individual component services are designed as black boxes, which mean that the details of their complexity are hidden from other components. Any communication between services happens through well-defined APIs to prevent implicit and hidden dependencies.
- **You build it, you run it** – DevOps is a key organizational principle for microservices, where the team responsible for building a service is also responsible for operating and maintaining it in production.

#### 5.5. Section 2 Key Takeaways

Some key takeaways from this section of the module include:

- Microservice applications are composed of independent services that communicate over well-defined APIS
- Microservices share the following characteristics:
    - Decentralized: Microservices are decentralized in the way they are developed, deployed, managed, and operated
    - Independent: Each component service in a microservices architecture can be developed, deployed, operated, and scaled without affecting the function of other services
    - Specialized: Each component service is designed for a set of capabilities and focuses on solving a specific problem
    - Polyglot: Microservice architectures take a heterogeneous approach to operating systems, programming languages, data stores, and tools
    - Black boxes: The details of the complexity of microservice components are hidden from other components
    - You build it, you run it: DevOps is a key organizational principle for microservices

### 6. Section 3: Building Microservice Applications with AWS Container Services

#### 6.1. Introducing Section 3: Building Microservice Applications with AWS Container Services

#### 6.2. What is a Container?

When you build a microservice architecture, you can use containers for the processing power.

Containers are a method of operating system virtualization that enables you to run an application and its dependencies in resource-isolated processes. A container is a lightweight, standalone software package. It contains everything that a software application needs to run, such as the application code, runtime engine, system tools, system libraries, and configurations.

#### 6.3. A Problem that Containers Solve

Containers can help ensure that applications deploy quickly, reliably, and consistently, regardless of deployment environment. Containers also give you more granular control over resources, which improves the efficiency of your infrastructure.

#### 6.4. Container Terminology

A container is created from a read-only template that is called an image. Images are typically built from a Dockerfile, which is a plaintext file that specifies all the components that are included in the container. You can create images from scratch, or you can use images that others created and published to a public or private container registry.

A container image is the snapshot of the file system that is available to the container. For example, you might have the Debian operating system as a container image. When you run this container, a Debian operating system is available to it. You can also package all your code dependencies in the container image and use it as your code artifact.

Container images are stored in a registry. You can download the images from the registry and run them on your cluster. Registries can exist in or outside your AWS infrastructure.

#### 6.5. Amazon ECS

You can run your containers on Amazon Elastic Container Service (Amazon ECS). Amazon ECS is a highly scalable, high-performance, container-management service. It supports Docker containers and enables you to easily run applications on a managed cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances.

Amazon ECS is a scalable cluster service for hosting containers that:

- Can scale up to thousands of Docker containers in seconds
- Monitors container deployment
- Manages the state of the cluster that runs the containers
- Schedules containers by using a built-in scheduler or third-party scheduler (Apache Mesos, Blox)
- Is extensible by using APIs
- Can be launched with either AWS Fargate or Amazon EC2 launch types

You can run ECS clusters at scale by mixing Spot Instances with On-Demand Instances and Reserved Instances.

#### 6.6. Amazon ECS Orchestrates Containers

Amazon ECS is a regional service that simplifies running application containers in a highly available manner across multiple Availability Zones within a Region. You can create ECS clusters in a new or existing virtual private cloud (VPC). A cluster is a logical grouping of resources.

After a cluster is up and running, you can define task definitions and services that specify which Docker container images to run across your clusters.

A task definition is a text file in JavaScript Object Notation (JSON) format. It describes one or more containers, up to a maximum of 10, that form your application. You can think of it as a blueprint for your application. Task definitions specify parameters for your application—for example, which containers and launch type to use. Other parameters include which ports should be opened for your application and what data volumes should be used with the containers in the task.

A service enables you to specify how many copies of your task definition to run and maintain in a cluster. You can optionally use an Elastic Load Balancing load balancer to distribute incoming traffic to containers in your service. Amazon ECS maintains that number of tasks and coordinates task scheduling with the load balancer.

After you create a task definition for your application, you can specify the number of tasks that will run on your cluster. A task is the instantiation of a task definition within a cluster. When you use Amazon ECS to run tasks, you place them in a cluster. Amazon ECS downloads your container images from a registry that you specify, and runs those images within your cluster.

#### 6.7. Amazon ECS Launch Types

Amazon ECS offers two launch types for hosting your containerized applications.

You can use the Fargate launch type to host your cluster on a serverless infrastructure that Amazon ECS manages. You only need to package your application in containers, specify the CPU and memory requirements, define networking and AWS Identity and Access Management (IAM) policies, and launch the application.

Alternatively, if you want more control, you can use the EC2 launch type to host your tasks on a cluster of EC2 container instances that you manage. A container instance is an EC2 instance that is running the Amazon ECS container agent. You can use Amazon ECS to schedule the placement of containers across your cluster based on your resource needs, isolation policies, and availability requirements. For information about different scheduling options, see Scheduling Amazon ECS Tasks. Amazon ECS keeps track of all the CPU, memory, and other resources in your cluster. It also finds the best server for a container to run on based on your specified resource requirements.

For more information about the Fargate and EC2 launch types, see Amazon ECS Launch Types.

#### 6.8. Amazon ECS Cluster Auto Scaling

You can create an Auto Scaling group for an Amazon ECS cluster. The Auto Scaling group contains container instances that you can scale out (and in) by using Amazon CloudWatch alarms. If you configure your Auto Scaling group to remove container instances, any tasks that are running on the removed container instances are stopped. If your tasks are running as part of a service, Amazon ECS restarts those tasks on another instance if the required resources are available. Examples of such required resources include CPU, memory, ports. However, tasks that were started manually are not restarted automatically.

You can also take advantage of Amazon ECS cluster auto scaling, which gives you more control over how you scale tasks in a cluster. It increases the speed and reliability of cluster scale-out. It gives you control over the amount of spare capacity that is maintained in your cluster, and automatically manages instance termination on scale-in.

With cluster auto scaling, you can configure Amazon ECS to scale your Auto Scaling group in and out automatically. Cluster auto scaling relies on capacity providers, which link your ECS cluster to the Auto Scaling groups that you want to use. Each Auto Scaling group is associated with a capacity provider, and each capacity provider has only one Auto Scaling group. However, many capacity providers can be associated with one ECS cluster. To scale the entire cluster automatically, each capacity provider manages the scaling of its associated Auto Scaling group.

For more information about cluster auto scaling, see the Amazon ECS Cluster Auto Scaling AWS News Blog post.

#### 6.9. Decomposing Monoliths – Step 1: Create Container Images

Again, consider the monolithic forum application that you saw earlier where the entire application runs as a single service. To rearchitect this application by using a microservice architecture, you can run each application process as a separate service within its own container. With a microservice architecture, the services can scale and be updated independently of the others.

To deploy the monolithic application as a microservice application, first build and tag an image for each service. Then, register the images with Amazon Elastic Container Registry (Amazon ECR).

#### 6.10. Decomposing Monoliths – Step 2: Create Service Task Definition and Target Groups

Next, choose a launch type and create a new service for each piece of the original monolithic application. Amazon ECS deploys each service into its own container across an ECS cluster. Then, create a target group for each service. The target group tracks the instances and ports of each container that is running for that service.

#### 6.11. Decomposing Monoliths – Step 3: Connect Load Balancer to Services

Finally, create an Application Load Balancer and configure listener rules to connect to the services. The listener checks for incoming connection requests to your load balancer and uses the rules to route traffic appropriately. In the example, the listener for the Application Load Balancer listens for HTTP service requests on Port 80 and routes them to the appropriate service.

#### 6.12. Tools for Building Highly Available Microservice Architectures

AWS Cloud Map and AWS App Mesh are two tools that can help you build highly available microservice architectures.

**AWS Cloud Map**

- Is a fully managed discovery service for cloud resources
- Can be used to define custom names for application resources
- Maintains updated location of dynamically changing resources, which increases application availability

**AWS App Mesh**

- Captures metrics, logs, and traces from all your microservices
- Enables you to export this data to Amazon CloudWatch, AWS X-Ray, and compatible AWS Partner Network (APN) Partner and community tools
- Enables you to control traffic flows between microservices to help ensure that services are highly available

AWS Cloud Map is a fully managed discovery service for cloud resources. You can use it to define custom names for your application resources (such as databases, queues, microservices, and other cloud resources). AWS Cloud Map maintains the updated location of these dynamically changing resources. This location maintenance increases the availability of your application because your web service always discovers the most up-to-date locations of its resources. You can add and register any resource with minimal manual intervention of mappings. AWS Cloud Map assists with service discovery, continuous integration, and health monitoring of your microservices and applications.

For more information about AWS Cloud Map, read this AWS Open Source Blog post. To learn more about how you can use AWS Cloud Map to enable your containerized services to discover and connect with each other, read AWS Fargate, Amazon EKS, and Amazon ECS now integrate with AWS Cloud Map.

When you create your task definitions, you can enable App Mesh integration. AWS App Mesh captures metrics, logs, and traces from all of your microservices. You can export this data to Amazon CloudWatch, AWS X-Ray, and compatible AWS Partner Network (APN) Partner and community tools for monitoring and tracing. AWS App Mesh also enables you to control how traffic flows between your microservices to make sure that every service is highly available during deployments, after failures, and as your application scales.

App Mesh enables you to configure microservices to connect directly to each other via a proxy instead of requiring code within the application or by using a load balancer. App Mesh uses Envoy, an open source service-mesh proxy, which is deployed alongside your microservice containers.

For more information about AWS Cloud Map and AWS App Mesh, see this AWS YouTube video.

#### 6.13. AWS Fargate

- Is a fully managed container service
- Works with Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS)
- Provisions, manages, and scales your container clusters
- Manages runtime environment
- Provides automatic scaling

In this section, you have learned that Amazon ECS offers two launch types: EC2 and Fargate.

AWS Fargate is a fully managed container service that works with both Amazon ECS and Amazon Elastic Kubernetes Service (Amazon EKS). It enables you to run containers without needing to manage servers or clusters. With AWS Fargate, you no longer need to provision, configure, and scale clusters of virtual machines to run containers. As a result, you don't need to choose server types, decide when to scale your clusters, or optimize cluster packing. AWS Fargate reduces the need for you to interact with or think about servers or clusters. Fargate enables you to focus on designing and building your applications instead of managing the infrastructure that runs them.

#### 6.14. Section 3 Key Takeaways

Some key takeaways from this section of the module include:

- Amazon ECS is a highly scalable, high-performance container management service. It supports Docker containers and enables you to easily run applications on a managed cluster of Amazon EC2 instances.
- Cluster auto scaling gives you more control over how you scale tasks within a cluster.
- AWS Cloud Map enables you to define custom names for your application resources. It maintains the updated location of these dynamically changing resources.
- AWS App Mesh is a service mesh that provides application-level networking to make it easy for your services to communicate with each other across multiple types of compute infrastructure.
- AWS Fargate is a fully managed container service that enables you to run containers without needing to manage servers or clusters.

#### 6.15. Module 13 – Guided Lab 1: Breaking a Monolithic Node.js Application into Microservices 

(Optional lab)

You might choose to complete Module 13 – Guided Lab 1: Breaking a Monolithic Node.js Application into Microservices. This lab is optional.

#### 6.16. Guided Lab 1: Tasks

1. Prepare the AWS Cloud9 development environment
2. Run a monolithic application on a basic Node.js server
3. Containerize the monolith for Amazon ECS
4. Deploy the monolith to Amazon ECS
5. Refactor the monolith into containerized microservices

#### 6.17. Guided Lab 1: Final Product

The diagram summarizes what you will have built after you complete the lab.

#### 6.18. Begin Module 13 – Guided Lab 1: Breaking a Monolithic Node.js Application into Microservices

It is now time to start the optional guided lab.

#### 6.19. Guided Lab 1 Debrief: Key Takeaways

Your educator might choose to lead a conversation about the key takeaways from this guided lab after you have completed it.

### 7. Section 4: Introducing Serverless Architectures

#### 7.1. Introducing Section 4: Introducing Serverless Architectures

#### 7.2. What Does Serverless Mean?

A way for you to build and run applications and services without thinking about servers.

So far, you have learned that you can use Amazon ECS to build your microservice applications by using containers. Amazon ECS is a container orchestration service where you manage your application code, data source integrations, security configuration, updates, network configuration, firewall, and management tasks. You also learned that you can use the Fargate launch type to host your cluster on a serverless infrastructure that Amazon ECS manages.

But what does serverless mean?

Serverless is the native architecture of the cloud that enables you to shift more operational responsibilities to AWS, which can increase your agility and innovation. Serverless enables you to build and run applications and services without thinking about servers. Your application still runs on servers. However, AWS does all the server management tasks, such as server or cluster provisioning, patching, operating system maintenance, and capacity provisioning.

#### 7.3. Tenets of Serverless Architectures

The tenets that define serverless as an operational model include:

- No infrastructure to provision or manage (no servers to provision, operate, or patch)
- Automatically scales by unit of consumption (scales by unit of work or consumption rather than by server unit)
- Pay-for-value pricing model (you pay only for the duration that a resource runs, rather than by server unit)
- Built-in availability and fault tolerance (no need to architect for availability because it is built into the service)

For more information about what serverless is, see this AWS website.

#### 7.4. Benefits of Serverless

Serverless enables you to build modern applications with increased agility and lower total cost of ownership (TCO). By using a serverless architecture, you can focus on your core product. You don't need to worry about managing and operating servers or runtimes, either in the cloud or on premises. This reduced overhead enables you to reclaim time and energy, which you can spend on developing products that scale and are reliable. Finally, serverless architectures enable you to build microservice applications.

#### 7.5. AWS Serverless Offerings

AWS has many offerings that you can use to build serverless architectures on AWS. So far in this course, you have already learned about several of them.

The rest of this module focuses on how you can use AWS Lambda, Amazon API Gateway, and AWS Step Functions to build serverless architectures.

#### 7.6. Section 4 Key Takeaways

Some key takeaways from this section of the module include:

- Serverless computing enables you to build and run applications and services without provisioning or managing servers
- Serverless architectures offer the following benefits:
    - Lower TCO
    - You can focus on your application
    - You can use them to build microservice applications

### 8. Section 5: Building Serverless Architectures with AWS Lambda

#### 8.1. Introducing Section 5: Building Serverless Architectures with AWS Lambda

#### 8.2. AWS Lambda

- Is a fully managed compute service
- Runs your code on a schedule or in response to events (for example, changes to an Amazon S3 bucket or an Amazon DynamoDB table)
- Supports Java, Go, PowerShell, Node.js, C#, Python, Ruby, and Runtime API
- Can run at edge locations closer to your users

AWS Lambda is a fully managed compute service that runs your code in response to events and automatically manages the underlying compute resources for you. Lambda runs your code on a high-availability compute infrastructure and performs all administration of the compute resources, including server and operating system maintenance, capacity provisioning, automatic scaling, code monitoring, and logging.

AWS Lambda natively supports Java, Go, PowerShell, Node.js, C#, Python, and Ruby code, and provides a Runtime API that enables you to use any additional programming languages to author your functions.

Lambda@Edge is a feature of Amazon CloudFront that enables you to run code closer to users of your application, which improves performance and reduces latency. Lambda@Edge runs your code in response to events that are generated by the Amazon CloudFront content delivery network (CDN). Lambda@Edge enables you to run Node.js and Python Lambda functions to customize content that Amazon CloudFront delivers. For information about how to add HTTP security response headers, read this AWS Networking & Content Delivery Blog post.

#### 8.3. How AWS Lambda Works

AWS Lambda integrates with other AWS services to invoke Lambda functions. A Lambda function is custom code that you write in one of the languages that Lambda supports. You can configure triggers to invoke a function in response to resource lifecycle events, respond to incoming HTTP requests, consume events from a queue, or run on a schedule.

An event source is the entity that publishes the event to Lambda. Your Lambda function processes the event, and Lambda runs your Lambda function on your behalf.

Lambda functions are stateless, which means that they have no affinity to the underlying infrastructure. Lambda can rapidly launch as many copies of the function as needed to scale to the rate of incoming events.

#### 8.4. Lambda Functions

When you create a Lambda function, you define the permissions for the function and specify which events trigger the function. You also create a deployment package that includes your application code and any dependencies and libraries that are needed to run your code. Finally, you configure runtime parameters such as memory, time out, and concurrency. When your function is invoked, Lambda will run an environment based on the runtime and configuration options that you selected.

#### 8.5. Anatomy of a Lambda Function

When a Lambda function is invoked, the code begins running at the handler. The handler is a specific code method or function that you create and include in your package. You specify the handler when you create a Lambda function. Each supported language has its own requirements for how a function handler can be defined and referenced within the package. After the handler is successfully invoked inside your Lambda function, the runtime environment belongs to the code you wrote.

The handler always takes two objects: the event object and the context object.

The event object provides information about the event that triggered the Lambda function. This event might be a pre-defined object that an AWS service generates, or a custom user-defined object in the form of a serializable string. An example of such a string might be a plain old Java object (POJO) or a JSON stream.

The contents of the event object include all the data and metadata that your Lambda function needs to drive its logic. The contents and structure of the event object vary, depending on which event source created it. For example, an event that is created by API Gateway contains details that are related to the HTTPS request that was made by the API client—such as path, query string, and request body. However, an event that is created by Amazon includes details about the bucket and the new object.

The context object is generated by AWS and provides metadata about the runtime environment. The context object enables your function code to interact with the Lambda runtime environment. The contents and structure of the context object vary based on the language runtime that your Lambda function uses.

However, at a minimum, the context object contains:

- awsRequestId – This property is used to track specific invocations of a Lambda function (important for error reporting or when contacting AWS Support)
- logStreamName – The CloudWatch log stream that your log statements will be sent to
- getRemainingTimeInMillis() – This method returns the number of milliseconds that remain before the running of your function times out

#### 8.6. Lambda Function Configuration and Billing

Memory and timeout are configurations that determine how your Lambda function performs. These configurations affect your billing. With AWS Lambda, you are charged based on the number of requests for your functions (the total number of requests across all your functions) and the duration (the time it takes for your code to run). The price depends on the amount of memory you allocate to your function.

**Memory** - You specify the amount of memory you want to allocate to your Lambda function. Lambda then allocates CPU power that is proportional to the memory. Lambda is priced so that the cost per 1 ms of function duration increases as the memory configuration increases. For example, say that you have a Lambda function with 256 MB of memory, and that it runs for 110 milliseconds. This function will cost twice as much as a Lambda function with 128 MB of memory that runs for the same time.

**Timeout** - You can control the maximum duration of your function by using the timeout configuration. You can set the timeout value for a function to any value up to 15 minutes. When the specified timeout is reached, AWS Lambda stops the running of your Lambda function. Using a timeout can prevent higher costs that come from long-running functions. You must find the right balance between not letting the function run too long and being able to finish under normal circumstances.

Follow these best practices:

- Test the performance of your Lambda function to make sure that you choose the optimum memory size configuration. You can view the memory usage for your function in Amazon CloudWatch Logs.
- Load-test your Lambda function to analyze how long your function runs and determine the best timeout value. This is important when your Lambda function makes network calls to resources that might not be able to handle the scaling of Lambda functions.

See the following resources for information about:

- AWS Lambda limits
- AWS Lambda pricing

#### 8.7. Demonstration: Creating an AWS Lambda Function

Now, the educator might choose to demonstrate how to create an AWS Lambda function.

#### 8.8. AWS Lambda Example: Simulated Slot Machine Browser Game

You can create Lambda functions to perform various tasks. This example uses a browser-based game that simulates a slot machine. The game invokes a Lambda function that generates the random results of each slot pull. The function returns those results as the file names of images that are used to display the result. The images are stored in an Amazon S3 bucket that is configured to function as a static web host for the HTML, CSS, and other assets that are needed to present the application experience.

#### 8.9. Event-Based Lambda Function Example: Order Processing

This example shows how Lambda can be used in a solution for order processing.

In this architecture:

1. A customer uploads a transactions file to an S3 bucket, which triggers the running of a Lambda function.
2. A Lambda function processes the transactions file and updates the Customer and Transactions DynamoDB tables.
3. Changes to the Transactions DynamoDB table trigger a second Lambda function to aggregate the transactions and update the totals in the Transaction total DynamoDB table. It also pushes a message to the HighBalancerAlert SNS topic.
4. The HighBalancerAlert SNS topic sends an email notification to the customer, and updates the CreditCollection and CustomerNotify SQS queues for payment processing.

#### 8.10. Lambda Layers

- Enable functions to share code easily – You can upload a layer one time and reference it in any function
- Promote separation of responsibilities – Developers can iterate faster on writing business logic
- Enable you to keep your deployment packages small
- Limits:
    - Up to five layers
    - 250 MB

When you build serverless applications, it is common to have code that is shared across Lambda functions. It can be custom code that two or more functions use, or a standard library that you add to simplify the implementation of your business logic.

Previously, you packaged and deployed this shared code together with all the functions that used it. Now, you can configure your Lambda function to include additional code and content as layers. A layer is a .zip archive that contains libraries, a custom runtime, or other dependencies.

With Lambda layers, functions can share code. Developers use layers to upload code one time and reuse it multiple times. With layers, you can use libraries in your function without needing to include them in your deployment package.

Sharing code this way can help promote the separation of responsibilities. One person can be responsible for managing the core library. Another person can be responsible for using and building on top of the library code to build application logic.

Layers enable you to keep your deployment package small, which makes development easier.

A function can use up to five layers at a time. The total unzipped size of the function and all layers can't exceed the unzipped deployment package size limit of 250 MB.

For more information about layers, see AWS Lambda Layers.

#### 8.11. Demonstration: Using AWS Lambda with Amazon S3

Now, the educator might choose to demonstrate how to configure an Amazon S3 event to trigger a Lambda function.

#### 8.12. Section 5 Key Takeaways

Some key takeaways from this section of the module include:

- Lambda is a serverless compute service that provides built-in fault tolerance and automatic scaling.
- A Lambda function is custom code that you write that processes events.
- A Lambda function is invoked by a handler, which takes an event object and context object as parameters.
- An event source is an AWS service or developer-created application that triggers a Lambda function to run.
- Lambda layers enable functions to share code and keep deployment packages small.

### 9. Module 13 – Guided Lab 2: Implementing a Serverless Architecture on AWS

You will now complete Module 13 – Guided Lab 2: Implementing a Serverless Architecture on AWS.

#### 9.1. Guided Lab 2: Tasks

1. Create a Lambda function to load data
2. Configure an Amazon S3 event
3. Test the loading process
4. Configure notifications
5. Create a Lambda function to send notifications
6. Test the system

#### 9.2. Guided Lab 2: Final Product

The diagram summarizes what you will have built after you complete the lab.

#### 9.3. Begin Module 13 – Guided Lab 2: Implementing a Serverless Architecture on AWS

It is now time to start the guided lab.

#### 9.4. Guided Lab 2 Debrief: Key Takeaways

Your educator might choose to lead a conversation about the key takeaways from this guided lab after you have completed it.

### 10. Section 6: Extending Serverless Architectures with Amazon API Gateway

#### 10.1. Introducing Section 6: Extending Serverless Architectures with Amazon API Gateway

#### 10.2. Amazon API Gateway

- Enables you to create, publish, maintain, monitor, and secure APIs that act as entry points to backend resources for your applications
- Handles up to hundreds of thousands of concurrent API calls
- Can handle workloads that run on:
    - Amazon EC2
    - Lambda
    - Any web application
    - Real-time communication applications
- Can host and use multiple versions and stages of your APIs

Amazon API Gateway is a fully managed service that enables you to create, publish, maintain, monitor, and secure APIs at any scale. You can use it to create Representational State Transfer (RESTful) and WebSocket APIs that act as an entry point for applications so they can access backend resources. Applications can then access data, business logic, or functionality from your backend services. Such services include applications that run on Amazon EC2, code that runs on Lambda, any web application, or real-time communication applications.

API Gateway handles all the tasks that are involved in accepting and processing up to hundreds of thousands of concurrent API calls. Such calls might include traffic management, authorization and access control, monitoring, and API version management. API Gateway has no minimum fees or startup costs. You pay only for the API calls you receive and the amount of data that is transferred out. With the API Gateway tiered-pricing model, you can reduce your cost as your API usage scales.

You can use API Gateway to host multiple versions and stages of your APIs.

#### 10.3. Amazon API Gateway Security

When you make your APIs publicly available, you are exposed to attackers that try to exploit your services. With Amazon API Gateway, you can protect your APIs in several ways.

With Amazon API Gateway, you can optionally set your API methods to require authorization. When you set up a method to require authorization, you can use AWS Signature Version 4 or Lambda authorizers to support your own bearer token authentication strategy. AWS Signature Version 4 is the process to add authentication information to AWS requests sent through HTTP. For security, most requests to AWS must be signed with an access key, which consists of an access key ID and secret access key. You use these AWS credentials to sign requests to your service and authorize access, like other AWS services. You can retrieve temporary credentials that are associated with a role in your AWS account by using Amazon Cognito. A Lambda authorizer is a Lambda function that authorizes access to APIs by using a bearer token authentication strategy like OAuth.

You can also apply a resource policy to an API to restrict access to a specific Amazon VPC or VPC endpoint. You can give an Amazon VPC or VPC endpoint from a different account access to the private API by using a resource policy.

Amazon API Gateway supports throttling settings for each method or route in your APIs. You can set a standard rate limit and a burst rate limit per second for each method in your REST APIs and each route in WebSocket APIs.

Additionally, you can use AWS WAF to secure your API Gateway APIs. AWS WAF is a web application firewall that helps protect your web applications from common web exploits that could affect availability, compromise security, or consume excessive resources