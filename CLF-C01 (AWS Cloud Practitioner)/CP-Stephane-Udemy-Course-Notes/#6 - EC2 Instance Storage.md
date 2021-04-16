# Section 6: EC2 Instance Storage

## Elastic Block Storage (EBS)

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled.png)

- EBS Volume

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%201.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%201.png)

    - If we have a snapshot, then we can move drives across AZ
- EBS Volume Example

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%202.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%202.png)

    - 1 EBS Volume → attached to only 1 instance
- EC2 instance → attached to EBS

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%203.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%203.png)

    - EC2 → Volumes → Create Volume → then attach it to EC2

        ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%204.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%204.png)

- EC2 terminate → may or may not terminate/delete EBS

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%205.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%205.png)

## EBS Snapshots

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%206.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%206.png)

- Actions → Create snapshot

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%207.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%207.png)

- Snapshot provide multiple actions → Create volume to restore into another AZ or region

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%208.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%208.png)

## AMI Overview

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%209.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%209.png)

- AMI Process (from an EC2 instance)

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2010.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2010.png)

    - Instance → right-click → options → create image for creating AMI

        ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2011.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2011.png)

        - Now custom AMI available to launch new instance

            ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2012.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2012.png)

## EC2 Image Builder

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2013.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2013.png)

- EC2 Image builder → process

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2014.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2014.png)

    - After pipeline completed → Run → Build instance created

        ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2015.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2015.png)

        - It will then terminate build instance → then testing will happen → and it will be terminated once done

            ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2016.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2016.png)

        - Then image will be available

            ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2017.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2017.png)

## EC2 Instance Store

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2018.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2018.png)

- Local EC2 Instance Store

    ![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2019.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2019.png)

## EFS - Elastic File System

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2020.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2020.png)

## EBS vs EFS

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2021.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2021.png)

## Shared Responsibility Model for EC2 Storage

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2022.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2022.png)

## EC2 Storage Summary

![Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2023.png](Section%206%20EC2%20Instance%20Storage%2059605f0000634a7fa632a244e9e76978/Untitled%2023.png)