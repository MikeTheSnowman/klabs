

# Exercise Description (Deleting clusters):
The exercise's name is self explanatory. Let's go and delete a cluster or two.


# Exercise Instructions
1. First we'll need to get a list of which clusters are running. Run the following command:
   ```
   k3d cluster list
   ```
   And you should see an output that looks like this:
   ```
   bob@debian1:~/Kubernetes_Labs$ k3d cluster list
   NAME          SERVERS   AGENTS   LOADBALANCER
   my-cluster1   1/1       3/3      true
   my-cluster2   1/1       1/1      true
   ```
2. Next, we'll delete both of the clusters that were listed:
   ```
   k3d cluster delete my-cluster1
   ```
   and
   ```
   k3d cluster delete my-cluster2
   ```
   And that's it! 

---
### Congradulations! 
You've sucessfully completed **Lab-2**!
Next, in **Lab-3** things will start to pick up as you learn how to interact and how to manage kubernetes using a command line tool called `kubectl`.
Click on the button below to navigate to **Lab-3**.
<br><a href="../../lab3/README.md"><img style="margin-bottom:-50px; padding-bottom:3px" src="../../assets/btn_StartLab3.svg" width="150" height="100" alt="Next Exercise"></a>