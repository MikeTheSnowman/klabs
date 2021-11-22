# Exercise-1: Creating pods

# Exercise Objectives
- To understand what a **pod** is.
- And learn how to deploy one on Kubernetes.

# Exercise Description
In the world of Kubernetes there are generally 8 broad categories of ***resources*** that you can create.
- Workload Resources
- Service Resources 
- Config and Storage Resources
- Authentication Resources
- Authorization Resources
- Policy Resources
- Extend Resources
- and Cluster Resources

For this exercise, you will be introduced to probably the most important ***workload resource*** resource that you will work with called a ***pod***.
A pod is probably the smallest, most fundamental *thing* that you can deploy and work with in Kubernetes because, it's the responsibility of a pod to run your container in addition to a few other things.

<details>
<summary><b>Important Note</b></summary>

<div class="warning" style='border: 2px solid white; border-radius: 6px; padding:0.5em; background-color:#7E909A; color:#FFFFFF'>
Just so you know, you do have the ability to deploy more than 1 container within a pod. <br/><b>However</b> it's highly recommended that you do <b>not</b> do this unless you have a good reason to do so. In most situations, you will only want to deploy one container per pod. For more information, there's a pretty good explanation in this article that will introduce you to a more advanced topic called the <b>sidecar deployment pattern</b> at the following <b><a href="https://medium.com/bb-tutorials-and-thoughts/kubernetes-learn-sidecar-container-pattern-6d8c21f873d">link</a></b>.
</div>
</details>

---
# Exercise Instructions:
1. Open a terminal. If you want to open from withing Visual Studio Code, you can use the following keyboard shortcut: ``ctrl + shift + ` ``

2. Using the `kubectl` command, we'll first take a look at the help information:
   ```
   kubectl -h
   ```
   <details>
   <summary>Example of help output</summary>

   ```
    bob@debian1:~/Kubernetes_Labs$ kubectl -h
    kubectl controls the Kubernetes cluster manager.

    Find more information at: https://kubernetes.io/docs/reference/kubectl/overview/

    Basic Commands (Beginner):
    create        Create a resource from a file or from stdin
    expose        Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
    run           Run a particular image on the cluster
    set           Set specific features on objects
    
    ...
    ```
   </details>

   <br/>


3. Closer to the top o the help output, we can see that there is a command called `run` that looks like it can do what we want. Let's look at the help information for the `run` command:
    ```
    kubectl run -h
    ```

   <details>
   <summary>Example of help output</summary>

   ```
    bob@debian1:~/Kubernetes_Labs$ kubectl run -h
    Create and run a particular image in a pod.

    Examples:
    # Start a nginx pod
    kubectl run nginx --image=nginx
    
    # Start a hazelcast pod and let the container expose port 5701
    kubectl run hazelcast --image=hazelcast/hazelcast --port=5701

    ...
    ```
   </details>
   <br/> 
   The `run` command looks like exactly what we need! And they even provided us with an example command to execute. Let's take that example, but apply a few small modifications so that later on we can test some things.
   <br/><br/>

4. Run the following command:
   ```
   kubectl run my-nginx --restart=Never --image=nginx --port=80
   ```

   Here's short explanation of the different options that we are passing to the `kubectl run` command:
   - `my-nginx` : This is the name that we're giving to the pod.
   - `--restart=Never` : If for some reason the containers in the pod *exits*, setting this option to `Never` tells Kubernetes to **not** attempt trying to restart the pod or the containers.
   - `--image=nginx` : Specifies which container image (Docker container image) that we want running in the pod.
   - `--port=80` : Specified which port the container is expecting to receive network connections on.

   <details>
   <summary>Example of expected output</summary>

   ```
   bob@debian1:~/Kubernetes_Labs$ kubectl run my-nginx --restart=Never --image=nginx --port=80
   pod/my-nginx created
   ```
   </details>
   <br/> 

5. Finally, let's take a look at the running status of our newly created pod with the following command:
    ```
    kubectl get pods
    ```
    And you should see an output that looks something like this:
    ```
    bob@debian1:~/Kubernetes_Labs$ kubectl get pods
    NAME       READY   STATUS    RESTARTS   AGE
    my-nginx   1/1     Running   0          3m23s
    ```
    If your output looks like the above example and under the `READY` column, you see `1/1`, then congradulations! You've sucessfully created your first pod on Kubernetes!

Please proceed to **Exercise-2**.