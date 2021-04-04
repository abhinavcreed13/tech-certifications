# #7 More on Azure Core Services - Part 2

## Monitoring in Azure

- Monitoring tab inside virtual machine
    - Azure monitoring service → Monitor

        ![images/section7/Untitled.png](images/section7/Untitled.png)

    - Monitor Metrics for different resources can be viewed → metrics can be added for multiple comparison → different charts can be added and can be pinned into dashboard

        ![images/section7/Untitled%201.png](images/section7/Untitled%201.png)

    - Monitor can also be used to view logs → Activity logs
    - Alerts can be used to place different alert rules based on different criteria/action
        - Add scope → which machine/target to be used
        - Alert can be based on metrics

            ![images/section7/Untitled%202.png](images/section7/Untitled%202.png)

        - Alert can also be based on Activity log

            ![images/section7/Untitled%203.png](images/section7/Untitled%203.png)

        - Set alert logic → define conditions → define corresponding action based on the alert
        - Action → require an action group
            - Notifications can be used to get alerts

                ![images/section7/Untitled%204.png](images/section7/Untitled%204.png)

        - Alert rule will have some monthly cost
        - Alerts which are fired → can be seen on the alert dashboard

            ![images/section7/Untitled%205.png](images/section7/Untitled%205.png)

## Log Analytics workspace

- environment can be used to store log data
- collect log data from various data sources
- can also be collected from on-premise systems
- or can be collected from diagnostics or log data from Azure storage
- LAB → connect VM to log analytics workspace
    - Create workspace

        ![images/section7/Untitled%206.png](images/section7/Untitled%206.png)

    - Workspace doesn't need to be in the same region as your machine/resource
    - Go to workspace data sources to connect different sources
        - Connect data source to workspace → only connect to 1 at a time

            ![images/section7/Untitled%207.png](images/section7/Untitled%207.png)

        - Once connected → workspace will install log daemon on the VM for logging data
        - You can download windows/linux agent and install on the machines which are on-premise

            ![images/section7/Untitled%208.png](images/section7/Untitled%208.png)

        - Can choose what data to be collected

            ![images/section7/Untitled%209.png](images/section7/Untitled%209.png)

        - Now after collection → logs can be queried

            ![images/section7/Untitled%2010.png](images/section7/Untitled%2010.png)

## Azure Kubernetes Service (AKS)