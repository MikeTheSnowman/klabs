- [Exercise Description (Creating your first Kubernetes cluster with K3D):](#exercise-description-creating-your-first-kubernetes-cluster-with-k3d)
- [Exercise Instructions](#exercise-instructions)

# Exercise Description (Creating your first Kubernetes cluster with K3D):
In this exercise you will create your first cluster. Your first cluster, at the end of the exercise, should consist of 2 worker nodes and 1 manager (or master or whatever you prefered nomenclature is). That's all there is to it!

# Exercise Instructions
For the  beginning part of the exercise, I'm not going to give you the answer immediately. I would like to take the opportunity to introduce you to some of the help information that the K3D command line utility can provide. Using the help information, we'll build out the command necessary to create our first cluster.

1. Open a terminal and run the following command:
   ```
   k3d -h
   ```
   And you should see some help information that looke like this:
   ```
   https://k3d.io/
   k3d is a wrapper CLI that helps you to easily create k3s clusters inside docker.
   Nodes of a k3d cluster are docker containers running a k3s image.
   All Nodes of a k3d cluster are part of the same docker network.

   Usage:
   k3d [flags]
   k3d [command]

   Available Commands:
   cluster      Manage cluster(s)
   completion   Generate completion scripts for [bash, zsh, fish, powershell | psh]
   config       Work with config file(s)
   help         Help about any command
   image        Handle container images.
   kubeconfig   Manage kubeconfig(s)
   node         Manage node(s)
   registry     Manage registry/registries
   version      Show k3d and default k3s version

   Flags:
   -h, --help         help for k3d
       --timestamps   Enable Log timestamps
       --trace        Enable super verbose output (trace logging)
       --verbose      Enable verbose output (debug logging)
       --version      Show k3d and default k3s version

   Use "k3d [command] --help" for more information about a command.
   ```
2. If you read the help output, you notice that there is a sub-command called `cluster` that's responsible for managing clusters. Let's look at the help information for that command to figure out what to do next:
   ```
   k3d cluster -h
   ```
   And now you should see that the help information will look something like this:
   ```
   Manage cluster(s)

   Usage:
   k3d cluster [flags]
   k3d cluster [command]

   Available Commands:
   create      Create a new cluster
   delete      Delete cluster(s).
   edit        [EXPERIMENTAL] Edit cluster(s).
   list        List cluster(s)
   start       Start existing k3d cluster(s)
   stop        Stop existing k3d cluster(s)

   Flags:
   -h, --help   help for cluster

   Global Flags:
       --timestamps   Enable Log timestamps
       --trace        Enable super verbose output (trace logging)
       --verbose      Enable verbose output (debug logging)

   Use "k3d cluster [command] --help" for more information about a command.
   ```
3. From the previous help information we see that `cluster` has a sub-command called `create`. This looks like exactly the command we need, so let's see what kinds of options are available with the `create` sub-command.
   ```
   k3d cluster create -h
   ```
   The resulting help output will look, a little crazy, like:
   ```
   Create a new k3s cluster with containerized nodes (k3s in docker).
   Every cluster will consist of one or more containers:
        - 1 (or more) server node container (k3s)
        - (optionally) 1 loadbalancer container as the entrypoint to the cluster (nginx)
        - (optionally) 1 (or more) agent node containers (k3s)

   Usage:
     k3d cluster create NAME [flags]

   Flags:
     -a, --agents int                                                     Specify how many agents you want to create
         --agents-memory string                                           Memory limit imposed on the agents nodes [From docker]
         --api-port [HOST:]HOSTPORT                                       Specify the Kubernetes API server port exposed on the LoadBalancer (Format: [HOST:]HOSTPORT)
                                                                        - Example: `k3d cluster create --servers 3 --api-port 0.0.0.0:6550`
     -c, --config string                                                  Path of a config file to use
     -e, --env KEY[=VALUE][@NODEFILTER[;NODEFILTER...]]                   Add environment variables to nodes (Format: KEY[=VALUE][@NODEFILTER[;NODEFILTER...]]
                                                                        - Example: `k3d cluster create --agents 2 -e "HTTP_PROXY=my.proxy.com@server:0" -e "SOME_KEY=SOME_VAL@server:0"`
         --gpus string                                                    GPU devices to add to the cluster node containers ('all' to pass all GPUs) [From docker]
     -h, --help                                                           help for create
     -i, --image string                                                   Specify k3s image that you want to use for the nodes
         --k3s-arg ARG@NODEFILTER[;@NODEFILTER]                           Additional args passed to k3s command (Format: ARG@NODEFILTER[;@NODEFILTER])
                                                                        - Example: `k3d cluster create --k3s-arg "--disable=traefik@server:0"
         --k3s-node-label KEY[=VALUE][@NODEFILTER[;NODEFILTER...]]        Add label to k3s node (Format: KEY[=VALUE][@NODEFILTER[;NODEFILTER...]]
                                                                        - Example: `k3d cluster create --agents 2 --k3s-node-label "my.label@agent:0,1" --k3s-node-label "other.label=somevalue@server:0"`
         --kubeconfig-switch-context                                      Directly switch the default kubeconfig's current-context to the new cluster's context (requires --kubeconfig-update-default) (default true)
         --kubeconfig-update-default                                      Directly update the default kubeconfig with the new cluster's context (default true)
         --lb-config-override strings                                     Use dotted YAML path syntax to override nginx loadbalancer settings
            --network string                                                 Join an existing network
         --no-image-volume                                                Disable the creation of a volume for importing images
         --no-lb                                                          Disable the creation of a LoadBalancer in front of the server nodes
         --no-rollback                                                    Disable the automatic rollback actions, if anything goes wrong
     -p, --port [HOST:][HOSTPORT:]CONTAINERPORT[/PROTOCOL][@NODEFILTER]   Map ports from the node containers (via the serverlb) to the host (Format: [HOST:][HOSTPORT:]CONTAINERPORT[/PROTOCOL][@NODEFILTER])
                                                                        - Example: `k3d cluster create --agents 2 -p 8080:80@agent:0 -p 8081@agent:1`
         --registry-config string                                         Specify path to an extra registries.yaml file
         --registry-create NAME[:HOST][:HOSTPORT]                         Create a k3d-managed registry and connect it to the cluster (Format: NAME[:HOST][:HOSTPORT]
                                                                        - Example: `k3d cluster create --registry-create mycluster-registry:0.0.0.0:5432`
         --registry-use stringArray                                       Connect to one or more k3d-managed registries running locally
         --runtime-label KEY[=VALUE][@NODEFILTER[;NODEFILTER...]]         Add label to container runtime (Format: KEY[=VALUE][@NODEFILTER[;NODEFILTER...]]
                                                                        - Example: `k3d cluster create --agents 2 --runtime-label "my.label@agent:0,1" --runtime-label "other.label=somevalue@server:0"`
     -s, --servers int                                                    Specify how many servers you want to create
   ...
   ```
4. Okay, the help output this time is a little overwhelming. But to help you out, there are three Things of particular interest to us:
   ```
   Usage:
     k3d cluster create NAME [flags]

   -a, --agents int          Specify how many agents you want to create
   -s, --servers int         Specify how many servers you want to create

   ``` 
   Based on this information we can extrapolate three things we want to pass to our command `k3d cluster create` :
   1. We can specify a `NAME` for our cluster
   2. We can control how many `agents` get created. (`agents` are the worker nodes). 
   3. And we can control how many `servers` get created. (`servers` are the `manager/master` nodes)
5. If you remember for the lab description, we will want to create a cluster with 2 workers nodes and 1 manager node. Also for now, we will use the name `my-cluster1` as the name of the cluster. With this information, the final command that we need to make execute to finally create our cluster is:
   ```
   k3d cluster create my-cluster1 -a 2 -s 1
   ```
   Go ahead and execute this in the terminal.
6. To verify that our cluster was created sucessfully, there will be two additional commands that we execute very quick. The first one being a k3d command to list our clusters:
   ```
   k3d cluster list
   ```
   If your terminal output looks like the below example, then awesome! That's a positive sign:
   ```
   NAME          SERVERS   AGENTS   LOADBALANCER
   my-cluster1   1/1       2/2      true
   ```
7. The final command to execute, just to perform a final check that everything looks good is actually a kubectl command. We'll learn how to use kubectl later, but for now, run the following command:
   ```
   kubectl cluster-info
   ```
   And if your terminal output looks like the example below, then CONGRADULATIONS! You've sucessfully created your first Kubernetes cluster!
   ```
   bob@debian1:~/Kubernetes_Labs$ kubectl cluster-info
   Kubernetes control plane is running at https://0.0.0.0:38289
   CoreDNS is running at https://0.0.0.0:38289/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
   Metrics-server is running at https://0.0.0.0:38289/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
   ```

You can now proceed to the next exercise.