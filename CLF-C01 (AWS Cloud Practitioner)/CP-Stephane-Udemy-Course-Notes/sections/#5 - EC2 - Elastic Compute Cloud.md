# Section 5: EC2 - Elastic Compute Cloud

## Amazon EC2

![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled.png)

- EC2 sizing & configuration options

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%201.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%201.png)

- EC2 instance types → Examples

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%202.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%202.png)

## Amazon EC2 Instance Types

![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%203.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%203.png)

- General Purpose

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%204.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%204.png)

- Compute Optimized

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%205.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%205.png)

- Memory Optimized

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%206.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%206.png)

- Storage Optimized

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%207.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%207.png)

## Security Groups & Classic Ports

- Security Groups

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%208.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%208.png)

    - Work as a firewall on EC2

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%209.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%209.png)

    - Diagram

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2010.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2010.png)

    - Classic ports to know

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2011.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2011.png)

    - Network & security → Security Groups

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2012.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2012.png)

        - CIDR → 0.0.0.0/0 → Anywhere
        - Security groups → can be attached to multiple instances

## SSH Summary

![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2013.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2013.png)

- Linux or Mac
    - pem key needed → with chmod

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2014.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2014.png)

- Windows 10 → ssh
    - Key → owner → set → Disable inheritance → only you should be able to full control

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2015.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2015.png)

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2016.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2016.png)

    - And it will work → no unauthorized key problem

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2017.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2017.png)

    - **Attach roles → EC2 instance**

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2018.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2018.png)

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2019.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2019.png)

        - Now aws cli commands inside EC2 instance can work → never do aws configure inside EC2 instance

            ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2020.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2020.png)

## EC2 Instance Launch Types

- Purchasing options

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2021.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2021.png)

    - EC2 on demand

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2022.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2022.png)

    - EC2 Reserved Instances

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2023.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2023.png)

    - EC2 Spot Instances

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2024.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2024.png)

    - EC2 Dedicated Hosts

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2025.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2025.png)

    - EC2 Dedicated Instances

        ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2026.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2026.png)

- Which purchasing option right for me?

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2027.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2027.png)

- Price Comparison

    ![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2028.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2028.png)

## Shared Responsibility Model for EC2

![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2029.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2029.png)

## EC2 Summary

![Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2030.png](Section%205%20EC2%20-%20Elastic%20Compute%20Cloud%2088ca94dda7db4270bf04152d4dbe871e/Untitled%2030.png)