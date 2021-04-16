# Section 6: EC2 Instance Storage

## Table of Contents
  - [Elastic Block Storage (EBS)](#elastic-block-storage-ebs)
  - [EBS Snapshots](#ebs-snapshots)
  - [AMI Overview](#ami-overview)
  - [EC2 Image Builder](#ec2-image-builder)
  - [EC2 Instance Store](#ec2-instance-store)
  - [EFS - Elastic File System](#efs---elastic-file-system)
  - [EBS vs EFS](#ebs-vs-efs)
  - [Shared Responsibility Model for EC2 Storage](#shared-responsibility-model-for-ec2-storage)
  - [EC2 Storage Summary](#ec2-storage-summary)

## Elastic Block Storage (EBS)

![../images/section6/Untitled.png](../images/section6/Untitled.png)

- EBS Volume

    ![../images/section6/Untitled%201.png](../images/section6/Untitled%201.png)

    - If we have a snapshot, then we can move drives across AZ
- EBS Volume Example

    ![../images/section6/Untitled%202.png](../images/section6/Untitled%202.png)

    - 1 EBS Volume → attached to only 1 instance
- EC2 instance → attached to EBS

    ![../images/section6/Untitled%203.png](../images/section6/Untitled%203.png)

    - EC2 → Volumes → Create Volume → then attach it to EC2

        ![../images/section6/Untitled%204.png](../images/section6/Untitled%204.png)

- EC2 terminate → may or may not terminate/delete EBS

    ![../images/section6/Untitled%205.png](../images/section6/Untitled%205.png)

## EBS Snapshots

![../images/section6/Untitled%206.png](../images/section6/Untitled%206.png)

- Actions → Create snapshot

    ![../images/section6/Untitled%207.png](../images/section6/Untitled%207.png)

- Snapshot provide multiple actions → Create volume to restore into another AZ or region

    ![../images/section6/Untitled%208.png](../images/section6/Untitled%208.png)

## AMI Overview

![../images/section6/Untitled%209.png](../images/section6/Untitled%209.png)

- AMI Process (from an EC2 instance)

    ![../images/section6/Untitled%2010.png](../images/section6/Untitled%2010.png)

    - Instance → right-click → options → create image for creating AMI

        ![../images/section6/Untitled%2011.png](../images/section6/Untitled%2011.png)

        - Now custom AMI available to launch new instance

            ![../images/section6/Untitled%2012.png](../images/section6/Untitled%2012.png)

## EC2 Image Builder

![../images/section6/Untitled%2013.png](../images/section6/Untitled%2013.png)

- EC2 Image builder → process

    ![../images/section6/Untitled%2014.png](../images/section6/Untitled%2014.png)

    - After pipeline completed → Run → Build instance created

        ![../images/section6/Untitled%2015.png](../images/section6/Untitled%2015.png)

        - It will then terminate build instance → then testing will happen → and it will be terminated once done

            ![../images/section6/Untitled%2016.png](../images/section6/Untitled%2016.png)

        - Then image will be available

            ![../images/section6/Untitled%2017.png](../images/section6/Untitled%2017.png)

## EC2 Instance Store

![../images/section6/Untitled%2018.png](../images/section6/Untitled%2018.png)

- Local EC2 Instance Store

    ![../images/section6/Untitled%2019.png](../images/section6/Untitled%2019.png)

## EFS - Elastic File System

![../images/section6/Untitled%2020.png](../images/section6/Untitled%2020.png)

## EBS vs EFS

![../images/section6/Untitled%2021.png](../images/section6/Untitled%2021.png)

## Shared Responsibility Model for EC2 Storage

![../images/section6/Untitled%2022.png](../images/section6/Untitled%2022.png)

## EC2 Storage Summary

![../images/section6/Untitled%2023.png](../images/section6/Untitled%2023.png)