# Section 5: EC2 - Elastic Compute Cloud

## Table of contents
  - [Amazon EC2](#amazon-ec2)
  - [Amazon EC2 Instance Types](#amazon-ec2-instance-types)
  - [Security Groups & Classic Ports](#security-groups--classic-ports)
  - [SSH Summary](#ssh-summary)
  - [EC2 Instance Launch Types](#ec2-instance-launch-types)
  - [Shared Responsibility Model for EC2](#shared-responsibility-model-for-ec2)
  - [EC2 Summary](#ec2-summary)

## Amazon EC2

![../images/section5/Untitled.png](../images/section5/Untitled.png)

- EC2 sizing & configuration options

    ![../images/section5/Untitled%201.png](../images/section5/Untitled%201.png)

- EC2 instance types → Examples

    ![../images/section5/Untitled%202.png](../images/section5/Untitled%202.png)

## Amazon EC2 Instance Types

![../images/section5/Untitled%203.png](../images/section5/Untitled%203.png)

- General Purpose

    ![../images/section5/Untitled%204.png](../images/section5/Untitled%204.png)

- Compute Optimized

    ![../images/section5/Untitled%205.png](../images/section5/Untitled%205.png)

- Memory Optimized

    ![../images/section5/Untitled%206.png](../images/section5/Untitled%206.png)

- Storage Optimized

    ![../images/section5/Untitled%207.png](../images/section5/Untitled%207.png)

## Security Groups & Classic Ports

- Security Groups

    ![../images/section5/Untitled%208.png](../images/section5/Untitled%208.png)

    - Work as a firewall on EC2

        ![../images/section5/Untitled%209.png](../images/section5/Untitled%209.png)

    - Diagram

        ![../images/section5/Untitled%2010.png](../images/section5/Untitled%2010.png)

    - Classic ports to know

        ![../images/section5/Untitled%2011.png](../images/section5/Untitled%2011.png)

    - Network & security → Security Groups

        ![../images/section5/Untitled%2012.png](../images/section5/Untitled%2012.png)

        - CIDR → 0.0.0.0/0 → Anywhere
        - Security groups → can be attached to multiple instances

## SSH Summary

![../images/section5/Untitled%2013.png](../images/section5/Untitled%2013.png)

- Linux or Mac
    - pem key needed → with chmod

        ![../images/section5/Untitled%2014.png](../images/section5/Untitled%2014.png)

- Windows 10 → ssh
    - Key → owner → set → Disable inheritance → only you should be able to full control

        ![../images/section5/Untitled%2015.png](../images/section5/Untitled%2015.png)

        ![../images/section5/Untitled%2016.png](../images/section5/Untitled%2016.png)

    - And it will work → no unauthorized key problem

        ![../images/section5/Untitled%2017.png](../images/section5/Untitled%2017.png)

    - **Attach roles → EC2 instance**

        ![../images/section5/Untitled%2018.png](../images/section5/Untitled%2018.png)

        ![../images/section5/Untitled%2019.png](../images/section5/Untitled%2019.png)

        - Now aws cli commands inside EC2 instance can work → never do aws configure inside EC2 instance

            ![../images/section5/Untitled%2020.png](../images/section5/Untitled%2020.png)

## EC2 Instance Launch Types

- Purchasing options

    ![../images/section5/Untitled%2021.png](../images/section5/Untitled%2021.png)

    - EC2 on demand

        ![../images/section5/Untitled%2022.png](../images/section5/Untitled%2022.png)

    - EC2 Reserved Instances

        ![../images/section5/Untitled%2023.png](../images/section5/Untitled%2023.png)

    - EC2 Spot Instances

        ![../images/section5/Untitled%2024.png](../images/section5/Untitled%2024.png)

    - EC2 Dedicated Hosts

        ![../images/section5/Untitled%2025.png](../images/section5/Untitled%2025.png)

    - EC2 Dedicated Instances

        ![../images/section5/Untitled%2026.png](../images/section5/Untitled%2026.png)

- Which purchasing option right for me?

    ![../images/section5/Untitled%2027.png](../images/section5/Untitled%2027.png)

- Price Comparison

    ![../images/section5/Untitled%2028.png](../images/section5/Untitled%2028.png)

## Shared Responsibility Model for EC2

![../images/section5/Untitled%2029.png](../images/section5/Untitled%2029.png)

## EC2 Summary

![../images/section5/Untitled%2030.png](../images/section5/Untitled%2030.png)