- [Exercise Description (Creating a second cluster & switching cluster contexts):](#exercise-description-creating-a-second-cluster--switching-cluster-contexts)
- [Exercise Instructions](#exercise-instructions)

# Exercise Description (Creating a second cluster & switching cluster contexts):
K3D allows you to create more than one Kubernetes cluster and it also provides you the ability to easily change which cluster that kubectl can communicate with.

In this exercise, we will create a second Kubernetes cluster and have you change cluster contexts.

# Exercise Instructions

1. Use K3D to create a new cluster that has `one worker node` and `one manager` with the name `my-cluster2`:
   ```
   k3d cluster create my-cluster2 -a 1 -s 1
   ``` 

2. Use K3D to list all of your clusters and you should see something like the output below where you have `my-cluster1` and `my-cluster2`:
   ```
   bob@debian1:~/Kubernetes_Labs$ k3d cluster list
   NAME          SERVERS   AGENTS   LOADBALANCER
   my-cluster1   1/1       2/2      true
   my-cluster2   1/1       1/1      true
   ```
   **`IMPORTANT NOTE:`** When you successfully run the `k3d cluster create` command, K3D will automatically update the `~/.kube/config` file so that kubectl can immediately start talking to your new cluster. You can confirm this by running the `kubectl get nodes` command and you should see ther terminal output look something like below and take note that you only have two nodes with the names starting with *"k3d-my-cluster2"*:
   ```
   bob@debian1:~/Kubernetes_Labs$ kubectl  get nodes
   NAME                       STATUS   ROLES                  AGE   VERSION
   k3d-my-cluster2-agent-0    Ready    <none>                 21s   v1.21.5+k3s2
   k3d-my-cluster2-server-0   Ready    control-plane,master   32s   v1.21.5+k3s2
   ```
3. To change context so that *kubectl* will communicate with *my-cluster1*, you can run the following command:
   ```
   k3d kubeconfig merge my-cluster1 -s -o ~/.kube/config
   ```
   You can verify that *kubectl* can communicate with the *my-cluster1* cluster by running the following command and seeing the following output:
   ```
   bob@debian1:~/Kubernetes_Labs$ kubectl get nodes
   NAME                       STATUS   ROLES                  AGE   VERSION
   k3d-my-cluster1-server-0   Ready    control-plane,master   16m   v1.21.5+k3s2
   k3d-my-cluster1-agent-1    Ready    <none>                 16m   v1.21.5+k3s2
   k3d-my-cluster1-agent-0    Ready    <none>                 16m   v1.21.5+k3s2
   ```

**You can now proceed to the next exercise!**