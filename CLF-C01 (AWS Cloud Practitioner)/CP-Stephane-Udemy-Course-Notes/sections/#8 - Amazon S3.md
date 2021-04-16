# Section 8: S3

## Table of contents
  - [Introduction](#introduction)
  - [S3 Security](#s3-security)
  - [S3 Websites](#s3-websites)
  - [S3 Versioning](#s3-versioning)
  - [S3 Access Logs](#s3-access-logs)
  - [S3 Replication (CRR & SRR)](#s3-replication-crr--srr)
  - [S3 Storage Classes](#s3-storage-classes)
  - [Shared Responsibility Model for S3](#shared-responsibility-model-for-s3)
  - [AWS Snow Family](#aws-snow-family)
  - [AWS Storage Gateway](#aws-storage-gateway)
  - [S3 Summary](#s3-summary)

## Introduction

![../images/section8/Untitled.png](../images/section8/Untitled.png)

- Use cases

    ![../images/section8/Untitled%201.png](../images/section8/Untitled%201.png)

- Buckets

    ![../images/section8/Untitled%202.png](../images/section8/Untitled%202.png)

- Objects

    ![../images/section8/Untitled%203.png](../images/section8/Untitled%203.png)

    ![../images/section8/Untitled%204.png](../images/section8/Untitled%204.png)

- Bucket example

    ![../images/section8/Untitled%205.png](../images/section8/Untitled%205.png)

- Object metadata view

    ![../images/section8/Untitled%206.png](../images/section8/Untitled%206.png)

## S3 Security

![../images/section8/Untitled%207.png](../images/section8/Untitled%207.png)

- Use Bucket Policy → Public Access

    ![../images/section8/Untitled%208.png](../images/section8/Untitled%208.png)

- User Access to S3 - IAM permissions

    ![../images/section8/Untitled%209.png](../images/section8/Untitled%209.png)

- EC2 instance access - use IAM roles

    ![../images/section8/Untitled%2010.png](../images/section8/Untitled%2010.png)

- Cross Account Access - Use Bucket Policy

    ![../images/section8/Untitled%2011.png](../images/section8/Untitled%2011.png)

- S3 Bucket Policies

    ![../images/section8/Untitled%2012.png](../images/section8/Untitled%2012.png)

- Bucket Settings for Block Public Access

    ![../images/section8/Untitled%2013.png](../images/section8/Untitled%2013.png)

## S3 Websites

![../images/section8/Untitled%2014.png](../images/section8/Untitled%2014.png)

- Enable via S3

    ![../images/section8/Untitled%2015.png](../images/section8/Untitled%2015.png)

## S3 Versioning

![../images/section8/Untitled%2016.png](../images/section8/Untitled%2016.png)

![../images/section8/Untitled%2017.png](../images/section8/Untitled%2017.png)

- Files deleted from bucket → can be recovered

    ![../images/section8/Untitled%2018.png](../images/section8/Untitled%2018.png)

    - Delete the delete marker → will restore the object

## S3 Access Logs

![../images/section8/Untitled%2019.png](../images/section8/Untitled%2019.png)

- You can enable this setting → all logs be logged into new another bucket

    ![../images/section8/Untitled%2020.png](../images/section8/Untitled%2020.png)

    - Log example

        ![../images/section8/Untitled%2021.png](../images/section8/Untitled%2021.png)

## S3 Replication (CRR & SRR)

![../images/section8/Untitled%2022.png](../images/section8/Untitled%2022.png)

- Management → Create replication rule

    ![../images/section8/Untitled%2023.png](../images/section8/Untitled%2023.png)

    - Objects before replication are not replicated

## S3 Storage Classes

![../images/section8/Untitled%2024.png](../images/section8/Untitled%2024.png)

- S3 Durability and Availability

    ![../images/section8/Untitled%2025.png](../images/section8/Untitled%2025.png)

- S3 Standard - General Purpose

    ![../images/section8/Untitled%2026.png](../images/section8/Untitled%2026.png)

- S3 Standard - Infrequent Access (IA)

    ![../images/section8/Untitled%2027.png](../images/section8/Untitled%2027.png)

- S3 Intelligent-Tiering

    ![../images/section8/Untitled%2028.png](../images/section8/Untitled%2028.png)

- S3 One Zone - Infrequent Access (IA)

    ![../images/section8/Untitled%2029.png](../images/section8/Untitled%2029.png)

- Amazon Glacier & Glacier Deep Archive

    ![../images/section8/Untitled%2030.png](../images/section8/Untitled%2030.png)

- S3 Storage Classes Comparison

    ![../images/section8/Untitled%2031.png](../images/section8/Untitled%2031.png)

- S3 - Moving between storage classes

    ![../images/section8/Untitled%2032.png](../images/section8/Untitled%2032.png)

- Additional upload options → for object → Storage Classes

    ![../images/section8/Untitled%2033.png](../images/section8/Untitled%2033.png)

    - Storage class can be edited and changed whenever required
- Lifecycle rules → help to optimize cost

    ![../images/section8/Untitled%2034.png](../images/section8/Untitled%2034.png)

- S3 Glacier Vault lock & S3 Object lock

    ![../images/section8/Untitled%2035.png](../images/section8/Untitled%2035.png)

## Shared Responsibility Model for S3

![../images/section8/Untitled%2036.png](../images/section8/Untitled%2036.png)

## AWS Snow Family

![../images/section8/Untitled%2037.png](../images/section8/Untitled%2037.png)

- Data Migrations with AWS Snow Family

    ![../images/section8/Untitled%2038.png](../images/section8/Untitled%2038.png)

- Diagrams

    ![../images/section8/Untitled%2039.png](../images/section8/Untitled%2039.png)

- Snowball Edge (for data transfers)

    ![../images/section8/Untitled%2040.png](../images/section8/Untitled%2040.png)

- AWS Snowcone

    ![../images/section8/Untitled%2041.png](../images/section8/Untitled%2041.png)

- AWS SnowMobile

    ![../images/section8/Untitled%2042.png](../images/section8/Untitled%2042.png)

- Comparison

    ![../images/section8/Untitled%2043.png](../images/section8/Untitled%2043.png)

- Usage Process

    ![../images/section8/Untitled%2044.png](../images/section8/Untitled%2044.png)

- What is Edge Computing?

    ![../images/section8/Untitled%2045.png](../images/section8/Untitled%2045.png)

- Snow Family - Edge Computing

    ![../images/section8/Untitled%2046.png](../images/section8/Untitled%2046.png)

- AWS OpsHub

    ![../images/section8/Untitled%2047.png](../images/section8/Untitled%2047.png)

- Snow Family → Create new job

    ![../images/section8/Untitled%2048.png](../images/section8/Untitled%2048.png)

## AWS Storage Gateway

- Hybrid Cloud for Storage

    ![../images/section8/Untitled%2049.png](../images/section8/Untitled%2049.png)

- AWS Storage Cloud Native Options

    ![../images/section8/Untitled%2050.png](../images/section8/Untitled%2050.png)

- AWS Storage Gateway

    ![../images/section8/Untitled%2051.png](../images/section8/Untitled%2051.png)

## S3 Summary

![../images/section8/Untitled%2052.png](../images/section8/Untitled%2052.png)