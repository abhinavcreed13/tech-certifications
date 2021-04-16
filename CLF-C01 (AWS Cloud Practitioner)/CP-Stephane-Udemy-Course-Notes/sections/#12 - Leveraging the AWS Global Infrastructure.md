# Section 12: Leveraging the AWS Global Infrastructure

## Why Global Applications?

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled.png)

- Global Applications in AWS

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%201.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%201.png)

## Amazon Route 53

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%202.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%202.png)

- Diagram for a record

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%203.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%203.png)

    - Route 53 Routing Policies

        ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%204.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%204.png)

        ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%205.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%205.png)

- AWS console → Route 53

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%206.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%206.png)

    - Domain registration → buy domain for your URLs
    - Set Routing Policy → Latency for the domain

        ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%207.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%207.png)

## AWS CloudFront

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%208.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%208.png)

- CloudFront - Origins

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%209.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%209.png)

- CloudFront at a high level

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2010.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2010.png)

- CloudFront - S3 as an Origin

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2011.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2011.png)

- CloudFront vs S3 Cross Region Replication

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2012.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2012.png)

- AWS Console → CloudFront Interface

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2013.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2013.png)

## S3 Transfer Acceleration

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2014.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2014.png)

## AWS Global Accelerator

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2015.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2015.png)

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2016.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2016.png)

- AWS Global Accelerator vs CloudFront

    ![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2017.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2017.png)

## AWS Outposts

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2018.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2018.png)

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2019.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2019.png)

## Global Applications in AWS - Summary

![Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2020.png](Section%2012%20Leveraging%20the%20AWS%20Global%20Infrastructur%20dc2942dcec4c4e04b9f0616c6d9af836/Untitled%2020.png)