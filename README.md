

<details>
<summary><b>Table of Contents</b> (click to open)</summary>
<!-- MarkdownTOC -->

- [Kubernetes Learning Labs:](#kubernetes-learning-labs)
  - [About:](#about)
- [Summary of lab modules:](#summary-of-lab-modules)
- [About this VM:](#about-this-vm)
- [About K3d](#about-k3d)
  - [K3d prerequisites:](#k3d-prerequisites)
  - [K3d installation command:](#k3d-installation-command)

<!-- /MarkdownTOC -->
</details>

# Kubernetes Learning Labs:

About:
---
    NOTE: To read all the documentation in a pretty way, from within Visual Studio Code, press: 
    <ctrl> + <shift> + <v>

The purpose of the lab exercises is to get you up to speed on using Kubernetes (abbreviated as K8s) with the following learning objectives in mind:
- To become familiar with the basics of YAML
- To get introduced to core terminology
- To become familiar with the core concepts
- To understand how to interact with K8s using kubectl
- To understand how to create or deploy your own resources on K8s using YAML and kubectl
- And to understand how to read an interptet the K8s API documentation

# Summary of lab modules:
Each lab module has been designed to provide you with exercises on a general topic related to Kubernetes. Below is a quick summary of the primary topic covered by each lab:
  - Lab 1: YAML fundamentals
  - Lab 2: Working with K3d
  - Lab 3: Getting started with kubectl
  - Lab 4: Managing K8s resources using YAML

If you want to go through the labs in order, click on the button below.
<br>
<a href="./lab1/README.md">
  <img src="resources/btn_StartLab1.svg" width="150" height="100" alt="Start Lab 1">
</a>

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

Please note, K3d is already installed within this VM for your convienance. But if you with to get K3d installed in another VM please read about the below system requirements and the single curl command you can execute to get K3d installed.
## K3d prerequisites:
  - Linux (K3d does not support Windows)
  - Docker
  - Kubectl
## K3d installation command:
    NOTE: K3d is already installed on this VM. If you re-run the command, it's okay, nothing bad will happen.
Installation command to install the latest version, you have the option of using either the `wget` or `curl` command below:
  - wget: `wget -q -O - https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash`
  - curl: `curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash`

Install command for a specific release:
Use the install script to grab a specific release (via TAG environment variable):

  - wget: `wget -q -O - https://raw.githubusercontent.com/rancher/k3d/main/install.sh | TAG=v5.0.0 bash`
  - curl: `curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | TAG=v5.0.0 bash`