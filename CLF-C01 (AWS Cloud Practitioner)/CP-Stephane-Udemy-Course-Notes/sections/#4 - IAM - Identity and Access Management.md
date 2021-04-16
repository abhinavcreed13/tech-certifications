# Section 4: IAM - Identity and Access Management

## Table of Contents
  - [IAM Introduction](#iam-introduction)
  - [**IAM demo**](#iam-demo)
  - [IAM MFA Overview](#iam-mfa-overview)
  - [Access AWS](#access-aws)
    - [AWS CLI](#aws-cli)
    - [AWS CloudShell](#aws-cloudshell)
  - [IAM Roles](#iam-roles)
  - [IAM Security Tools](#iam-security-tools)
  - [IAM Guidelines & Best Practices](#iam-guidelines--best-practices)
  - [Shared Responsibility Model for IAM](#shared-responsibility-model-for-iam)
  - [IAM Summary](#iam-summary)

## IAM Introduction

- Users & groups

    ![../images/section4/Untitled.png](../images/section4/Untitled.png)

- Permissions → Policies

    ![../images/section4/Untitled%201.png](../images/section4/Untitled%201.png)

## **IAM demo**

- Dashboard → root user will create users, groups and policies

    ![../images/section4/Untitled%202.png](../images/section4/Untitled%202.png)

    - Users → Add User

        ![../images/section4/Untitled%203.png](../images/section4/Untitled%203.png)

        - Set permissions

            ![../images/section4/Untitled%204.png](../images/section4/Untitled%204.png)

            - Groups will add/attach policy to all the users in the group
        - Add tags (optional)

            ![../images/section4/Untitled%205.png](../images/section4/Untitled%205.png)

    - IAM users sign-in link can be customized

        ![../images/section4/Untitled%206.png](../images/section4/Untitled%206.png)

    - Direct login page → Choose IAM user

        ![../images/section4/Untitled%207.png](../images/section4/Untitled%207.png)

- @ sign → IAM user and no @ sign → root user

    ![../images/section4/Untitled%208.png](../images/section4/Untitled%208.png)

- If you don't have valid permissions/policy for the user

    ![../images/section4/Untitled%209.png](../images/section4/Untitled%209.png)

- Policies

    ![../images/section4/Untitled%2010.png](../images/section4/Untitled%2010.png)

    - Administrator access → JSON

        ![../images/section4/Untitled%2011.png](../images/section4/Untitled%2011.png)

- Create your own custom policy

    ![../images/section4/Untitled%2012.png](../images/section4/Untitled%2012.png)

## IAM MFA Overview

- Password policy → can be assigned to a group of users

    ![../images/section4/Untitled%2013.png](../images/section4/Untitled%2013.png)

- Second defense mechanism → MFA

    ![../images/section4/Untitled%2014.png](../images/section4/Untitled%2014.png)

    - MFA device option

        ![../images/section4/Untitled%2015.png](../images/section4/Untitled%2015.png)

        ![../images/section4/Untitled%2016.png](../images/section4/Untitled%2016.png)

        - IAM screen

            ![../images/section4/Untitled%2017.png](../images/section4/Untitled%2017.png)

## Access AWS

- How can users access AWS?

    ![../images/section4/Untitled%2018.png](../images/section4/Untitled%2018.png)

- Example Access keys

    ![../images/section4/Untitled%2019.png](../images/section4/Untitled%2019.png)

### AWS CLI

- Download and install AWS CLI → python-based

    ![../images/section4/Untitled%2020.png](../images/section4/Untitled%2020.png)

- Create access keys → IAM dashboard

    ![../images/section4/Untitled%2021.png](../images/section4/Untitled%2021.png)

- Configure aws cli

    ![../images/section4/Untitled%2022.png](../images/section4/Untitled%2022.png)

- Now run commands → `aws iam list-users`

### AWS CloudShell

- CLI in the cloud

    ![../images/section4/Untitled%2023.png](../images/section4/Untitled%2023.png)

- Run commands

    ![../images/section4/Untitled%2024.png](../images/section4/Untitled%2024.png)

## IAM Roles

- IAM roles for services

    ![../images/section4/Untitled%2025.png](../images/section4/Untitled%2025.png)

    - Example → Role → attach permissions/policies

        ![../images/section4/Untitled%2026.png](../images/section4/Untitled%2026.png)

## IAM Security Tools

![../images/section4/Untitled%2027.png](../images/section4/Untitled%2027.png)

- Generate credentials report

    ![../images/section4/Untitled%2028.png](../images/section4/Untitled%2028.png)

- Access Advisor → user-specific

    ![../images/section4/Untitled%2029.png](../images/section4/Untitled%2029.png)

## IAM Guidelines & Best Practices

![../images/section4/Untitled%2030.png](../images/section4/Untitled%2030.png)

## Shared Responsibility Model for IAM

![../images/section4/Untitled%2031.png](../images/section4/Untitled%2031.png)

## IAM Summary

![../images/section4/Untitled%2032.png](../images/section4/Untitled%2032.png)