# Section 11: Deployments & Managing Infrastructure at Scale

## AWS CloudFormation

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled.png)

- Benefits of AWS CloudFormation

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%201.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%201.png)

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%202.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%202.png)

- CloudFormation Stack Designer

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%203.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%203.png)

- AWS CloudFormation → Create Stack

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%204.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%204.png)

    - Example template → View in Designer

        ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%205.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%205.png)

        ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%206.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%206.png)

## AWS Beanstalk

- Typical architecture

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%207.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%207.png)

- Developer problems on AWS

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%208.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%208.png)

- AWS Elastic Beanstalk

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%209.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%209.png)

    - Elastic Beanstalk

        ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2010.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2010.png)

        ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2011.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2011.png)

    - Beanstalk - Health Monitoring

        ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2012.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2012.png)

    - Elastic Beanstalk → Choose Platform

        ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2013.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2013.png)

        - Uses cloudformation as the backend to deploy the stack

        ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2014.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2014.png)

## AWS CodeDeploy

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2015.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2015.png)

## AWS CodeCommit

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2016.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2016.png)

## AWS CodeBuild

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2017.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2017.png)

## AWS CodePipeline

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2018.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2018.png)

## AWS CodeArtifact

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2019.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2019.png)

## AWS CodeStar

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2020.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2020.png)

## AWS Cloud9

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2021.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2021.png)

## Demo - CodeStar

- CodeCommit

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2022.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2022.png)

- CodeStar

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2023.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2023.png)

- Cloud9

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2024.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2024.png)

## AWS Systems Manager (SSM)

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2025.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2025.png)

- How Systems Manager works?

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2026.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2026.png)

## AWS OpsWorks

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2027.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2027.png)

- OpsWorks Architecture

    ![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2028.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2028.png)

## Deployment Summary

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2029.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2029.png)

## Developer Services Summary

![Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2030.png](Section%2011%20Deployments%20&%20Managing%20Infrastructure%20a%20dab52b1d8c644a2cb9df4e4bf12db7d3/Untitled%2030.png)