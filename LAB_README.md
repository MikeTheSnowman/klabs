# Summary:

The purpose of the lab exercises is to get you up to speed on using Kubernetes (abbreviated as K8s) with the following learning objectives in mind:
- To get introduced to core terminology
- To become familiar with the core concepts
- To understand how to interact with K8s using kubectl
- To become familiar with the basics of YAML
- To understand how to create or deploy your own resources on K8s using YAML and kubectl
- And to understand how to read an interptet the K8s API documentation

# About this VM:
In order to help you along your K8s learning path, this VM has been designed to be as lightweight aspossible and with collection of software pre-installed to make your learning experience much easier so you can focus on just using kubernetes.

The core software that you'll be interacting with in order to learn K8s are:
- Visual Studio Code with the following extensions:
  - YAML (from Red Hat)
  - Kubernetes (from Microsoft)
  - Markdown (from Yu Zhang)
- Docker Community Edition for Linux
- K3d

VS Code and Docker are popular pieces of software that I'm just going to assume that you already know about, so I won't explain what they are for, but what about K3d?

# About K3d
K3d, is probably a new name that you haven't heard of before. Basically K3d is a tool developed by Rancher (now owned by Suse) that makes it **super** easy to create single-node or multi-node kubernetes clusters on your local machine. In our case, K3d will be used to help us to easily create and destroy K8s clusters on this VM.

K3d accomplishes this in a few ways:
  1. K3d provides you a very easy to use command line interface that you can use to create, delete, and manage your Kubernetes cluster.
  2. When you create a cluster using K3d, all Kubernetes nodes that K3d creates are running inside of a Docker container.
  3. The containers that act as K8s nodes all have a very lightweight container runtime which uses containerd, runc, and cri.
  4. When you create pods (containers) to run on your K8s cluster, you're essentially creating that container, in another container.