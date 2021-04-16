# AWS - Cloud Practitioner Partner Training

## Table of Contents
  - [Goals](#goals)
  - [**Course Modules**](#course-modules)
  - [Module 1: Introduction to the AWS cloud](#module-1-introduction-to-the-aws-cloud)
  - [Module 2: Getting started with the cloud](#module-2-getting-started-with-the-cloud)
  - [Module 3: Building in the Cloud](#module-3-building-in-the-cloud)
  - [Module 4: Secure your cloud application and data](#module-4-secure-your-cloud-application-and-data)
  - [Module 5: AWS Pricing and Support Models](#module-5-aws-pricing-and-support-models)
  - [Module 6: Architecture and Outcome](#module-6-architecture-and-outcome)
  - [Conclusion](#conclusion)

## Goals

- Prepare for the cloud practitioner certification examination
- Be able to talk confidently → customer executives
- Web application hosting example

    ![images/Untitled.png](images/Untitled.png)

    - Understanding what each component does

## **Course Modules**

![images/Untitled%201.png](images/Untitled%201.png)

## Module 1: Introduction to the AWS cloud

![images/Untitled%202.png](images/Untitled%202.png)

- **Cloud deployment models**

![images/Untitled%203.png](images/Untitled%203.png)

Hybrid

- Applicable for customers → need to move to cloud + have on-premise also

- **What are the benefits of moving to the cloud?**
- Trade capital expense for variable expense

    ![images/Untitled%204.png](images/Untitled%204.png)

- Increase speed and agility

    ![images/Untitled%205.png](images/Untitled%205.png)

- Streamline and enhance infrastructure decisions

    ![images/Untitled%206.png](images/Untitled%206.png)

- Reduce expenses

    ![images/Untitled%207.png](images/Untitled%207.png)

    ![images/Untitled%208.png](images/Untitled%208.png)

- Scale globally - data center in 25 different regions → 200 countries globally

    ![images/Untitled%209.png](images/Untitled%209.png)

- Increase innovation - pre-built ML/AI platforms

    ![images/Untitled%2010.png](images/Untitled%2010.png)

    - 200+ services
    - Computer, database, Networking, Storage, Security → today's target

- AWS Global Infrastructure
    - Infrastructure Map

        ![images/Untitled%2011.png](images/Untitled%2011.png)

        - yellow → upcoming regions
    - Selecting a region

        ![images/Untitled%2012.png](images/Untitled%2012.png)

        - Put data as close to the customer as possible
    - Availability Zones
        - Isolated self containers of data centers

            ![images/Untitled%2013.png](images/Untitled%2013.png)

        - Provided within each regions
        - Important for mission critical workloads
        - Why?

            ![images/Untitled%2014.png](images/Untitled%2014.png)

        - Edge locations

            ![images/Untitled%2015.png](images/Untitled%2015.png)

    - Amazon CloudFront Service
        - Uses edge location infrastructure
        - delivers content to users globally (Same as Azure CDN)
        - Edge location → caching services

            ![images/Untitled%2016.png](images/Untitled%2016.png)

        - Checks if the content is available or not → if not take it from the origin and cache it → faster access + decrease latency

- AWS Management Infrastructure
    - 3 ways to interact with AWS

        ![images/Untitled%2017.png](images/Untitled%2017.png)

    - AWS management console

        ![images/Untitled%2018.png](images/Untitled%2018.png)

- Key Takeaways

![images/Untitled%2019.png](images/Untitled%2019.png)

## Module 2: Getting started with the cloud

- Component terms

    ![images/Untitled%2020.png](images/Untitled%2020.png)

    - Lambda → Developer → not caring about the infrastructure
- Benefits of Amazon EC2
    - Elasticity

        ![images/Untitled%2021.png](images/Untitled%2021.png)

    - Pay only as you go

        ![images/Untitled%2022.png](images/Untitled%2022.png)

    - Control

        ![images/Untitled%2023.png](images/Untitled%2023.png)

    - Flexibility

        ![images/Untitled%2024.png](images/Untitled%2024.png)

    - Integrated

        ![images/Untitled%2025.png](images/Untitled%2025.png)

    - Reliable
    - Secure
    - Inexpensive
    - Easy

        ![images/Untitled%2026.png](images/Untitled%2026.png)

- Creating a new EC2 compute instance
    - Region?
    - Software platform?
        - OS?
        - AMI - Amazon Machine Image?
    - Instance type?
        - Memory, vCPU's, network bandwidth, hardware accelerators
    - Tweak security needs
    - Launch
- Modernising instances

    ![images/Untitled%2027.png](images/Untitled%2027.png)

    - Modernising Linux → AWS Graviton

        ![images/Untitled%2028.png](images/Untitled%2028.png)

- Object vs Block Storage
    - Amazon S3 Object Store

        ![images/Untitled%2029.png](images/Untitled%2029.png)

        - Good for storing documents
    - Amazon EBS Block Store

        ![images/Untitled%2030.png](images/Untitled%2030.png)

- Storage

    ![images/Untitled%2031.png](images/Untitled%2031.png)

- Amazon Elastic Block Store (EBS)
    - Persistent block storage for instances
    - Protected through replication
    - Different drive types - SSD/HDD
    - Scale up in minutes
    - Snapshot functionality

        ![images/Untitled%2032.png](images/Untitled%2032.png)

    - Encryption available
- Amazon S3

    ![images/Untitled%2033.png](images/Untitled%2033.png)

    - Backup and storage
    - Application hosting
    - Media hosting
    - Software delivery

    ![images/Untitled%2034.png](images/Untitled%2034.png)

    - Amazon S3 glacier → Archiving data

        ![images/Untitled%2035.png](images/Untitled%2035.png)

        - Use-cases

        ![images/Untitled%2036.png](images/Untitled%2036.png)

    - Cost analysis

        ![images/Untitled%2037.png](images/Untitled%2037.png)

    ### Design a simple web server

    - Requirements

        ![images/Untitled%2038.png](images/Untitled%2038.png)

    - Architecture

        ![images/Untitled%2039.png](images/Untitled%2039.png)

    - Secure a web app

        ![images/Untitled%2040.png](images/Untitled%2040.png)

    - Amazon VPC (Virtual Private Cloud)

        ![images/Untitled%2041.png](images/Untitled%2041.png)

        - Security groups

            ![images/Untitled%2042.png](images/Untitled%2042.png)

            - 10.0.1.0/24 → [10.0.1.0 - 10.0.1.255] access allowed

            ![images/Untitled%2043.png](images/Untitled%2043.png)

    - Security Group implementation

        ![images/Untitled%2044.png](images/Untitled%2044.png)

        - Only web servers → can talk to app tier on the port 6455
        - DB servers can only access by the app servers → port 3306
        - Corp → 10.0.16.0/24 can access all tiers using SSH (port 22)
    - Demo: AWS EC2 Dashboard

        ![images/Untitled%2045.png](images/Untitled%2045.png)

    - Access can be restricted as per the regions
    - Service health

        ![images/Untitled%2046.png](images/Untitled%2046.png)

        - Availability zones → 3 zones
    - Create EC2 instances
        - Step 1: Choose AMI

            ![images/Untitled%2047.png](images/Untitled%2047.png)

            - Multiple AMI supported like Deep Learning AMI → it will spin up with pytorch, tensorflow and other stuff
            - AWS Marketplace can also be selected for EC2 spin-up

                ![images/Untitled%2048.png](images/Untitled%2048.png)

                - Custom images → for preinstalling tools
        - Step 2: Choose Instance type

            ![images/Untitled%2049.png](images/Untitled%2049.png)

            - Can be launched here also
        - Step 3: Configure instance

            ![images/Untitled%2050.png](images/Untitled%2050.png)

            - Network + subnet can be controlled here
            - Enable termination protection
            - Enable monitoring → Enable CloudWatch detailed monitoring
            - Amazon CloudWatch → service that capture events and log everything (Kind of same as Application Insights)
        - Step 4: Add Storage

            ![images/Untitled%2051.png](images/Untitled%2051.png)

            - SSD IOPS and throughput can be controlled here
        - Step 5: Add tags

            ![images/Untitled%2052.png](images/Untitled%2052.png)

            - Tags can be used to automate how things are running
            - Pull out reports and stuff based on filtering using tags
        - Step 6: Configure Security Group
        - Step 7: Configure SSH keys
        - Launch
    - Monitoring

        ![images/Untitled%2053.png](images/Untitled%2053.png)

    - Change instance type → stop instance and then change it

        ![images/Untitled%2054.png](images/Untitled%2054.png)

    - Provisioned server → connected with a VPC + attached HDD

## Module 3: Building in the Cloud

- Agenda

    ![images/Untitled%2055.png](images/Untitled%2055.png)

- **Amazon CloudWatch**
    - Monitor AWS resources
    - How CloudWatch works?

        ![images/Untitled%2056.png](images/Untitled%2056.png)

        - Collect metrics → from different sources
        - Raise alerts

- **Manage demand efficiently**

    ![images/Untitled%2057.png](images/Untitled%2057.png)

    - When/Where should we provision more servers?
    - Auto-scaling → spin-up more instances and then distribute load using load balancer

        ![images/Untitled%2058.png](images/Untitled%2058.png)

        - **DNS service** (like Azure traffic manager) → direct traffic across regions
    - **Amazon EC2 Auto Scaling**

        ![images/Untitled%2059.png](images/Untitled%2059.png)

        - Uses CloudWatch Alarms → to add more/less instances
        - For Sunday

            ![images/Untitled%2060.png](images/Untitled%2060.png)

        - For Monday

            ![images/Untitled%2061.png](images/Untitled%2061.png)

        - For wednesday

            ![images/Untitled%2062.png](images/Untitled%2062.png)

            - Putting a cap makes sense → what if load unnecessary increases leading to crazy amount of EC2 scaling
    - **Elastic load balancing**

        ![images/Untitled%2063.png](images/Untitled%2063.png)

        - Load Balancer Example

            ![images/Untitled%2064.png](images/Untitled%2064.png)

            - Load balancer can direct traffic based on the APIs → can also use API gateway

- **Deploy database services**

    ![images/Untitled%2065.png](images/Untitled%2065.png)

    - Both IaaS and PaaS service available
    - **Amazon RDS (Relational Database Services)**

        ![images/Untitled%2066.png](images/Untitled%2066.png)

        - Amazon Aurora

            ![images/Untitled%2067.png](images/Untitled%2067.png)

        - Relational vs key-value databases

            ![images/Untitled%2068.png](images/Untitled%2068.png)

        - Amazon DynamoDB

            ![images/Untitled%2069.png](images/Untitled%2069.png)

            - Use-cases

            ![images/Untitled%2070.png](images/Untitled%2070.png)

        - Other databases

            ![images/Untitled%2071.png](images/Untitled%2071.png)

        - AWS database migration service

            ![images/Untitled%2072.png](images/Untitled%2072.png)

    - **Automate Deployment**

        ![images/Untitled%2073.png](images/Untitled%2073.png)

        - AWS CloudFormation

            ![images/Untitled%2074.png](images/Untitled%2074.png)

            - Example

                ![images/Untitled%2075.png](images/Untitled%2075.png)

            - Almost like Ansible → automating cloud infrastructure deployment process

    - **Putting it all together**
        - 1/4

            ![images/Untitled%2076.png](images/Untitled%2076.png)

        - 2/4

            ![images/Untitled%2077.png](images/Untitled%2077.png)

        - 3/4

            ![images/Untitled%2078.png](images/Untitled%2078.png)

        - 4/4

            ![images/Untitled%2079.png](images/Untitled%2079.png)

    - **Connect and share data**
        - Challenge: hybrid cloud

            ![images/Untitled%2080.png](images/Untitled%2080.png)

        - AWS Direct Connect → Same as Azure ExpressRoute

            ![images/Untitled%2081.png](images/Untitled%2081.png)

            - Example

                ![images/Untitled%2082.png](images/Untitled%2082.png)

        - Amazon Route 53 → DNS web service

            ![images/Untitled%2083.png](images/Untitled%2083.png)

            - Knows how to route traffic → can load balance across regions
            - Routing traffic example

                ![images/Untitled%2084.png](images/Untitled%2084.png)

                - Route traffic to one of the load balancers/nearest edge locations
        - Amazon Elastic File System (EFS)
            - It is a block store → which can be shared across VMs
            - EBS volume connects mostly to 1 instance
            - S3 can be shared across VMs → but not high performance

            ![images/Untitled%2085.png](images/Untitled%2085.png)

        - Putting it all together

            ![images/Untitled%2086.png](images/Untitled%2086.png)

    - **Deliver content faster**
        - **AWS Elastic Beanstalk**

            ![images/Untitled%2087.png](images/Untitled%2087.png)

            - Only .NET
            - Just write the code and upload it
            - Abstracts whole platform from the developer
            - Features

                ![images/Untitled%2088.png](images/Untitled%2088.png)

        - **AWS Lambda**

            ![images/Untitled%2089.png](images/Untitled%2089.png)

            - Run code without servers
            - Lambda functions can be connected to CloudWatch events
            - Supports all other languages
            - Benefits

                ![images/Untitled%2090.png](images/Untitled%2090.png)

            - Example → create thumbnails

                ![images/Untitled%2091.png](images/Untitled%2091.png)

        - *Does AWS lambda also supports .NET? If so, why do you need beanstalk?*
        - **Amazon Simple Notification Service (Amazon SNS)**

            ![images/Untitled%2092.png](images/Untitled%2092.png)

            - Probably same as Azure Service Bus/Azure Queue Storage
            - Overview

                ![images/Untitled%2093.png](images/Untitled%2093.png)

        - **Amazon ElastiCache**

            ![images/Untitled%2094.png](images/Untitled%2094.png)

            - In-memory data store → Redis/Memcached
            - Challenge: 2 billion interactions every day → tinder example

                ![images/Untitled%2095.png](images/Untitled%2095.png)

- Key Takeaways

![images/Untitled%2096.png](images/Untitled%2096.png)

## Module 4: Secure your cloud application and data

- Security of the cloud

    ![images/Untitled%2097.png](images/Untitled%2097.png)

- Security in the cloud

    ![images/Untitled%2098.png](images/Untitled%2098.png)

- Shared responsibility model

    ![images/Untitled%2099.png](images/Untitled%2099.png)

- Who's responsible for what?

    ![images/Untitled%20100.png](images/Untitled%20100.png)

- Security, identity and compliance products/services

    ![images/Untitled%20101.png](images/Untitled%20101.png)

    - AWS IAM
    - AWS Inspector
    - AWS Shield
- AWS IAM
    - Basic security system

    ![images/Untitled%20102.png](images/Untitled%20102.png)

    - Manages → Authentication + Authorization
    - Authentication

        ![images/Untitled%20103.png](images/Untitled%20103.png)

    - Authorization

        ![images/Untitled%20104.png](images/Untitled%20104.png)

    - IAM roles + policies

        ![images/Untitled%20105.png](images/Untitled%20105.png)

    - AWS account root user

        ![images/Untitled%20106.png](images/Untitled%20106.png)

        - Never use root account → day to day activities
        - Always recommend → use root account to create other IAM roles and accounts
    - Best practices

        ![images/Untitled%20107.png](images/Untitled%20107.png)

    - **Security assessment and compliance**
        - **Amazon Inspector**

            ![images/Untitled%20108.png](images/Untitled%20108.png)

            - Findings

                ![images/Untitled%20109.png](images/Untitled%20109.png)

            - Remediation recommendation

                ![images/Untitled%20110.png](images/Untitled%20110.png)

    - **Protect cloud from DDoS**

        ![images/Untitled%20111.png](images/Untitled%20111.png)

        - If Auto-scaling is turned on → you may start spinning up EC2 instances leading to huge cost
        - Challenges

            ![images/Untitled%20112.png](images/Untitled%20112.png)

        - **AWS Shield**

            ![images/Untitled%20113.png](images/Untitled%20113.png)

            - Always-on
            - Can deflect most of the attacks
            - If auto-scaling turned on and you haven't put max → then it might still blow up
            - Offerings

                ![images/Untitled%20114.png](images/Untitled%20114.png)

    - AWS security compliance

        ![images/Untitled%20115.png](images/Untitled%20115.png)

        - Security of the cloud → compliance
    - Achieve compliance?

        ![images/Untitled%20116.png](images/Untitled%20116.png)

    - Customer responsibility

        ![images/Untitled%20117.png](images/Untitled%20117.png)

    - Knowledge Check

        ![images/Untitled%20118.png](images/Untitled%20118.png)

    - Key takeaways

        ![images/Untitled%20119.png](images/Untitled%20119.png)

    - Amazon Inspector Demo
        - Dashboard

            ![images/Untitled%20120.png](images/Untitled%20120.png)

        - Findings

            ![images/Untitled%20121.png](images/Untitled%20121.png)

        - Recommendation

            ![images/Untitled%20122.png](images/Untitled%20122.png)

    - Security Hub

        ![images/Untitled%20123.png](images/Untitled%20123.png)

## Module 5: AWS Pricing and Support Models

- Fundamentals of Pricing

    ![images/Untitled%20124.png](images/Untitled%20124.png)

- Use more, pay less

    ![images/Untitled%20125.png](images/Untitled%20125.png)

- Pricing concepts

    ![images/Untitled%20126.png](images/Untitled%20126.png)

- Amazon EC2 - 4 purchase types

    ![images/Untitled%20127.png](images/Untitled%20127.png)

- Well-optimised compute model → customer example

    ![images/Untitled%20128.png](images/Untitled%20128.png)

- Amazon EC2 data transfer

    ![images/Untitled%20129.png](images/Untitled%20129.png)

- Amazon EBS pricing model

    ![images/Untitled%20130.png](images/Untitled%20130.png)

- AWS services → no additional charge → only resource it uses

    ![images/Untitled%20131.png](images/Untitled%20131.png)

- AWS Calculator

    ![images/Untitled%20132.png](images/Untitled%20132.png)

- AWS Cost Explorer

    ![images/Untitled%20133.png](images/Untitled%20133.png)

- Trusted Advisor

    ![images/Untitled%20134.png](images/Untitled%20134.png)

- Cost Explorer Demo

    ![images/Untitled%20135.png](images/Untitled%20135.png)

    - Filtered based on services

        ![images/Untitled%20136.png](images/Untitled%20136.png)

- AWS Support Plans

    ![images/Untitled%20137.png](images/Untitled%20137.png)

- Support documentation

    ![images/Untitled%20138.png](images/Untitled%20138.png)

- Key takeaways

    ![images/Untitled%20139.png](images/Untitled%20139.png)

## Module 6: Architecture and Outcome

- Operational excellence

    ![images/Untitled%20140.png](images/Untitled%20140.png)

- Security

    ![images/Untitled%20141.png](images/Untitled%20141.png)

- Reliability

    ![images/Untitled%20142.png](images/Untitled%20142.png)

- Cost optimization

    ![images/Untitled%20143.png](images/Untitled%20143.png)

- Reference architectures

    ![images/Untitled%20144.png](images/Untitled%20144.png)

- Example: Web Application hosting
    - Amazon CloudFront → content delivery caching service
        - Static workload → fetch
        - Dynamic workload → probably use elastic load balancing

    ![images/Untitled%20145.png](images/Untitled%20145.png)

- AWS quick starts → for more complex understanding
- Key takeaways

    ![images/Untitled%20146.png](images/Untitled%20146.png)

## Conclusion

https://bit.ly/CPEassess

![images/Untitled%20147.png](images/Untitled%20147.png)