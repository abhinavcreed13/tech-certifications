# Section 7: Elastic Load Balancing & Auto Scaling Groups

## Table of contents
  - [Scalability & High Availability](#scalability--high-availability)
  - [Elastic Load Balance (ELB)](#elastic-load-balance-elb)
  - [Auto Scaling Groups (ASG)](#auto-scaling-groups-asg)
  - [ELB & ASG Summary](#elb--asg-summary)

## Scalability & High Availability

![../images/section7/Untitled.png](../images/section7/Untitled.png)

- High Availability

    ![../images/section7/Untitled%201.png](../images/section7/Untitled%201.png)

- For EC2

    ![../images/section7/Untitled%202.png](../images/section7/Untitled%202.png)

- Scalability vs Elasticity (vs Agility)

    ![../images/section7/Untitled%203.png](../images/section7/Untitled%203.png)

## Elastic Load Balance (ELB)

- What is load balancing?

    ![../images/section7/Untitled%204.png](../images/section7/Untitled%204.png)

    - Why use a load balancer?

        ![../images/section7/Untitled%205.png](../images/section7/Untitled%205.png)

    - Why use an ELB?

        ![../images/section7/Untitled%206.png](../images/section7/Untitled%206.png)

- Load Balancer → Choose while creating

    ![../images/section7/Untitled%207.png](../images/section7/Untitled%207.png)

    - Then configure it
    - Create target groups → register EC2 instances

        ![../images/section7/Untitled%208.png](../images/section7/Untitled%208.png)

## Auto Scaling Groups (ASG)

![../images/section7/Untitled%209.png](../images/section7/Untitled%209.png)

- In AWS → minimum size, desired capacity, maximum size

    ![../images/section7/Untitled%2010.png](../images/section7/Untitled%2010.png)

- With ALB

    ![../images/section7/Untitled%2011.png](../images/section7/Untitled%2011.png)

- Create auto-scaling group → process

    ![../images/section7/Untitled%2012.png](../images/section7/Untitled%2012.png)

    - How it scales?

        ![../images/section7/Untitled%2013.png](../images/section7/Untitled%2013.png)

## ELB & ASG Summary

![../images/section7/Untitled%2014.png](../images/section7/Untitled%2014.png)