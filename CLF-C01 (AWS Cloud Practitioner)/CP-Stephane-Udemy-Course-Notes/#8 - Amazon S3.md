# Section 8: S3

## Introduction

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled.png)

- Use cases

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%201.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%201.png)

- Buckets

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%202.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%202.png)

- Objects

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%203.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%203.png)

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%204.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%204.png)

- Bucket example

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%205.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%205.png)

- Object metadata view

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%206.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%206.png)

## S3 Security

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%207.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%207.png)

- Use Bucket Policy → Public Access

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%208.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%208.png)

- User Access to S3 - IAM permissions

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%209.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%209.png)

- EC2 instance access - use IAM roles

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2010.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2010.png)

- Cross Account Access - Use Bucket Policy

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2011.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2011.png)

- S3 Bucket Policies

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2012.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2012.png)

- Bucket Settings for Block Public Access

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2013.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2013.png)

## S3 Websites

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2014.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2014.png)

- Enable via S3

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2015.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2015.png)

## S3 Versioning

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2016.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2016.png)

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2017.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2017.png)

- Files deleted from bucket → can be recovered

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2018.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2018.png)

    - Delete the delete marker → will restore the object

## S3 Access Logs

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2019.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2019.png)

- You can enable this setting → all logs be logged into new another bucket

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2020.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2020.png)

    - Log example

        ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2021.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2021.png)

## S3 Replication (CRR & SRR)

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2022.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2022.png)

- Management → Create replication rule

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2023.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2023.png)

    - Objects before replication are not replicated

## S3 Storage Classes

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2024.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2024.png)

- S3 Durability and Availability

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2025.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2025.png)

- S3 Standard - General Purpose

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2026.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2026.png)

- S3 Standard - Infrequent Access (IA)

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2027.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2027.png)

- S3 Intelligent-Tiering

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2028.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2028.png)

- S3 One Zone - Infrequent Access (IA)

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2029.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2029.png)

- Amazon Glacier & Glacier Deep Archive

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2030.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2030.png)

- S3 Storage Classes Comparison

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2031.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2031.png)

- S3 - Moving between storage classes

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2032.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2032.png)

- Additional upload options → for object → Storage Classes

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2033.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2033.png)

    - Storage class can be edited and changed whenever required
- Lifecycle rules → help to optimize cost

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2034.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2034.png)

- S3 Glacier Vault lock & S3 Object lock

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2035.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2035.png)

## Shared Responsibility Model for S3

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2036.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2036.png)

## AWS Snow Family

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2037.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2037.png)

- Data Migrations with AWS Snow Family

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2038.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2038.png)

- Diagrams

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2039.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2039.png)

- Snowball Edge (for data transfers)

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2040.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2040.png)

- AWS Snowcone

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2041.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2041.png)

- AWS SnowMobile

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2042.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2042.png)

- Comparison

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2043.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2043.png)

- Usage Process

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2044.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2044.png)

- What is Edge Computing?

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2045.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2045.png)

- Snow Family - Edge Computing

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2046.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2046.png)

- AWS OpsHub

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2047.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2047.png)

- Snow Family → Create new job

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2048.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2048.png)

## AWS Storage Gateway

- Hybrid Cloud for Storage

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2049.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2049.png)

- AWS Storage Cloud Native Options

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2050.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2050.png)

- AWS Storage Gateway

    ![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2051.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2051.png)

## S3 Summary

![Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2052.png](Section%208%20S3%2012199d86933242339fd2d87bb65e6ba7/Untitled%2052.png)