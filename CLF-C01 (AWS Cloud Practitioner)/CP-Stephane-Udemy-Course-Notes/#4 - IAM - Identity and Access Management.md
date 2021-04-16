# Section 4: IAM - Identity and Access Management

## IAM Introduction

- Users & groups

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled.png)

- Permissions → Policies

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%201.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%201.png)

## **IAM demo**

- Dashboard → root user will create users, groups and policies

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%202.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%202.png)

    - Users → Add User

        ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%203.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%203.png)

        - Set permissions

            ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%204.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%204.png)

            - Groups will add/attach policy to all the users in the group
        - Add tags (optional)

            ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%205.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%205.png)

    - IAM users sign-in link can be customized

        ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%206.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%206.png)

    - Direct login page → Choose IAM user

        ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%207.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%207.png)

- @ sign → IAM user and no @ sign → root user

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%208.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%208.png)

- If you don't have valid permissions/policy for the user

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%209.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%209.png)

- Policies

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2010.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2010.png)

    - Administrator access → JSON

        ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2011.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2011.png)

- Create your own custom policy

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2012.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2012.png)

## IAM MFA Overview

- Password policy → can be assigned to a group of users

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2013.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2013.png)

- Second defense mechanism → MFA

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2014.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2014.png)

    - MFA device option

        ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2015.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2015.png)

        ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2016.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2016.png)

        - IAM screen

            ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2017.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2017.png)

## Access AWS

- How can users access AWS?

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2018.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2018.png)

- Example Access keys

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2019.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2019.png)

### AWS CLI

- Download and install AWS CLI → python-based

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2020.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2020.png)

- Create access keys → IAM dashboard

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2021.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2021.png)

- Configure aws cli

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2022.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2022.png)

- Now run commands → `aws iam list-users`

### AWS CloudShell

- CLI in the cloud

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2023.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2023.png)

- Run commands

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2024.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2024.png)

## IAM Roles

- IAM roles for services

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2025.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2025.png)

    - Example → Role → attach permissions/policies

        ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2026.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2026.png)

## IAM Security Tools

![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2027.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2027.png)

- Generate credentials report

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2028.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2028.png)

- Access Advisor → user-specific

    ![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2029.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2029.png)

## IAM Guidelines & Best Practices

![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2030.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2030.png)

## Shared Responsibility Model for IAM

![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2031.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2031.png)

## IAM Summary

![Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2032.png](Section%204%20IAM%20-%20Identity%20and%20Access%20Management%20136cccd7668742d3a5adefe0013f030b/Untitled%2032.png)