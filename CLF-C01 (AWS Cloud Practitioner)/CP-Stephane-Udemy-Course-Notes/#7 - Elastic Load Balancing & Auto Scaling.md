# Section 7: Elastic Load Balancing & Auto Scaling Groups

## Scalability & High Availability

![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled.png)

- High Availability

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%201.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%201.png)

- For EC2

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%202.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%202.png)

- Scalability vs Elasticity (vs Agility)

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%203.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%203.png)

## Elastic Load Balance (ELB)

- What is load balancing?

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%204.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%204.png)

    - Why use a load balancer?

        ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%205.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%205.png)

    - Why use an ELB?

        ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%206.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%206.png)

- Load Balancer → Choose while creating

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%207.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%207.png)

    - Then configure it
    - Create target groups → register EC2 instances

        ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%208.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%208.png)

## Auto Scaling Groups (ASG)

![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%209.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%209.png)

- In AWS → minimum size, desired capacity, maximum size

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2010.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2010.png)

- With ALB

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2011.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2011.png)

- Create auto-scaling group → process

    ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2012.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2012.png)

    - How it scales?

        ![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2013.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2013.png)

## ELB & ASG Summary

![Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2014.png](Section%207%20Elastic%20Load%20Balancing%20&%20Auto%20Scaling%20Gr%2018d85902d82a474b8ef1ec1c3f7e6491/Untitled%2014.png)