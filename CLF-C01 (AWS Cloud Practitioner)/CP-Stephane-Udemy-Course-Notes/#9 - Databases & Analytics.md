# Section 9: Databases & Analytics

## Introduction

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled.png)

- Relational Databases

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%201.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%201.png)

- NoSQL databases

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%202.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%202.png)

    - Example

        ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%203.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%203.png)

    - Databases & Shared Responsibility on AWS

        ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%204.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%204.png)

## AWS RDS & Aurora Overview

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%205.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%205.png)

- Advantage over using RDS vs deploying DB on EC2

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%206.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%206.png)

- RDS Solution Architecture

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%207.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%207.png)

- Amazon Aurora

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%208.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%208.png)

- Create database → AWS console → managed service

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%209.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%209.png)

- RDS AWS Console

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2010.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2010.png)

## RDS Deployments

- Read Replicas, Multi-AZ

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2011.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2011.png)

- Multi-region (Read Replicas)

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2012.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2012.png)

## Amazon ElasticCache Overview

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2013.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2013.png)

- Solution Architecture - Cache

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2014.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2014.png)

## Amazon DynamoDB

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2015.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2015.png)

- Type of data

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2016.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2016.png)

- DynamoDB Accelerator - DAX

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2017.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2017.png)

- Create DynamoDB Table

    ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2018.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2018.png)

    - No question of what server → serverless
    - Create data

        ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2019.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2019.png)

    - Sample data

        ![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2020.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2020.png)

## AWS Redshift

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2021.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2021.png)

## Amazon EMR (Elastic MapReduce)

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2022.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2022.png)

## AWS Athena

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2023.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2023.png)

## Amazon QuickSight

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2024.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2024.png)

## DocumentDB

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2025.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2025.png)

## Amazon Neptune

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2026.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2026.png)

## Amazon QLDB

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2027.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2027.png)

## Amazon Managed Blockchain

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2028.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2028.png)

## DMS - Database Migration Service

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2029.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2029.png)

## AWS Glue

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2030.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2030.png)

## Databases & Analytics Summary in AWS

![Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2031.png](Section%209%20Databases%20&%20Analytics%205ec8457c42b945c8aa9a57e6da159408/Untitled%2031.png)