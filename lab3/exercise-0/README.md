
# Exercise 0: Prep work

# Exercise Objectives
- To get a kubernetes cluster running for our future exercises.

# Exercise Description
This exercise is just to setup the kubernetes cluster that we will be using for the remaining exercises in this lab.

# Exercise Instructions
1. Use K3D to create a cluster with 3 agents/workers and 1 manager/server.
    <details>
    <summary>Click to see the answer</summary>

    ```
    k3d cluster create -a 3 -s 1
    ```
    
    <details>
    <summary>Example of expected output</summary>
       
        bob@debian1:~/Kubernetes_Labs$ k3d cluster create -a 3 -s 1
        INFO[0000] Prep: Network                                
        INFO[0000] Created network 'k3d-k3s-default'            
        INFO[0000] Created volume 'k3d-k3s-default-images'      
        INFO[0000] Starting new tools node...                   
        INFO[0000] Starting Node 'k3d-k3s-default-tools'        
        INFO[0001] Creating node 'k3d-k3s-default-server-0'     
        INFO[0001] Creating node 'k3d-k3s-default-agent-0'      
        INFO[0001] Creating node 'k3d-k3s-default-agent-1'      
        INFO[0001] Creating node 'k3d-k3s-default-agent-2'      
        INFO[0001] Creating LoadBalancer 'k3d-k3s-default-serverlb' 
        INFO[0001] Using the k3d-tools node to gather environment information 
        INFO[0001] HostIP: using network gateway...             
        INFO[0001] Starting cluster 'k3s-default'               
        INFO[0001] Starting servers...                          
        INFO[0001] Starting Node 'k3d-k3s-default-server-0'     
        INFO[0002] Deleted k3d-k3s-default-tools                
        INFO[0009] Starting agents...                           
        INFO[0009] Starting Node 'k3d-k3s-default-agent-1'      
        INFO[0009] Starting Node 'k3d-k3s-default-agent-2'      
        INFO[0009] Starting Node 'k3d-k3s-default-agent-0'      
        INFO[0024] Starting helpers...                          
        INFO[0024] Starting Node 'k3d-k3s-default-serverlb'     
        INFO[0032] Injecting '172.24.0.1 host.k3d.internal' into /etc/hosts of all nodes... 
        INFO[0032] Injecting records for host.k3d.internal and for 5 network members into CoreDNS configmap... 
        INFO[0033] Cluster 'k3s-default' created successfully!  
        INFO[0033] You can now use it like this:                
        kubectl cluster-info

    </details>

    </details>

2. After sucessfully creating your cluster, move on to **Exercise-1**.