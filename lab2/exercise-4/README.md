

# Exercise Description:
There might be a situation where you realize that your Kubernetes cluster needs more worker/manager nodes or maybe you have too many and you want to scale down. To handle these situations, K3D allows you to add or remove additional nodes from your cluster.

In this exercise, we will add, then remove a worker node from our K8s cluster.


# Exercise Instructions
1. Run the following commands to make sure that we're in the right context
   ```
   bob@debian1:~/Kubernetes_Labs$ k3d kubeconfig merge my-cluster1 -s -o ~/.kube/config 

   bob@debian1:~/Kubernetes_Labs$ kubectl get nodes
   NAME                       STATUS   ROLES                  AGE   VERSION
   k3d-my-cluster1-agent-0    Ready    <none>                 80m   v1.21.5+k3s2
   k3d-my-cluster1-agent-1    Ready    <none>                 80m   v1.21.5+k3s2
   k3d-my-cluster1-server-0   Ready    control-plane,master   81m   v1.21.5+k3s2
   ```
   If you see the terminal output showing 2 agent nodes and one server/manager node as shown above, then move on th the next step.

2. First we will add a additional `agent/worker` node to `my-cluster1` with a starting name of `extra-agent`. To do that, run the following command:
   ```
   k3d node create extra-agent -c my-cluster1 --role agent
   ```
   And you whould see output similar to the following:
   ```
   bob@debian1:~/Kubernetes_Labs$ k3d node create extra-agent -c my-cluster1 --role agent
   INFO[0000] Adding 1 node(s) to the runtime local cluster 'my-cluster1'...
   INFO[0000] Starting Node 'k3d-extra-agent-0'           
   INFO[0008] Successfully created 1 node(s)!
   ```
    Also, to ensure that Kubernetes sees the addtional agent/worker node, we chan check with the `kubectl get nodes` command where you should see the following output:
    ```
    bob@debian1:~/Kubernetes_Labs$ kubectl get nodes
    NAME                       STATUS     ROLES                  AGE     VERSION
    k3d-extra-agent-0          Ready      <none>                 4m34s   v1.21.5+k3s2
    k3d-my-cluster1-agent-0    Ready      <none>                 99m     v1.21.5+k3s2
    k3d-my-cluster1-agent-1    Ready      <none>                 99m     v1.21.5+k3s2
    k3d-my-cluster1-server-0   Ready      control-plane,master   99m     v1.21.5+k3s2
    ```
    If you see the entry for `k3d-extra-agent-0` then awesome! You've successfully added an additional node to your kubernetes cluster!

---
After completing the this exercise, please click on the button below to go to the next exercise where you'll learn about **how to use K3D to delete your cluster**.
<br><a href="../exercise-5/README.md"><img style="margin-bottom:-50px; padding-bottom:3px" src="../../assets/btn_Exercise5.svg" width="150" height="100" alt="Next Exercise"></a>