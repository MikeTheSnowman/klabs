
# Lab 2: K3d Tutorial
---
## Lab Objective
In order for you to proceed with the rest of the labs in this Kubernetes training course, it is the objective of this lab to give you a tutorial in how to effectively use K3d.

Before we get into using Kubernetes directly there is a very important tool, for educational & testing purposes, that we will learn about first.
That tool is called K3d, and we will be using it in order to easily, and quickly create, modify, and destroy Kubernetes clusters.

You hay have heard of other tools like MiniKube, KINDS, MicroK8s, and many more. K3d was chosen, instead of one of the other potential options, because it's very small, easy to install, super easy to use, and the K8s clusters that it can create are very lightweight while still being fully featured. With that said I believe that K3d is the perfect tool to use if you're trying to learn how to use Kubernetes or if you need to quickly setup a K8s cluster with as many (reasonable number of) worker and master nodes as you need.


## Learning outcomes:
For this lab, your learning goals are the following:
  - Become familiar with the installation pre-requisites
  - Become familiar with how to install K3d
  - Understand how it is that K3d creates K8s clusters
  - Learn how to use K3d to create a new cluster
  - Learn how to modify an existing cluster by adding additional nodes
  - Learn how to destroy clusters


## Exercise summary:
  - Exercise 1: Installing K3d
  - Exercise 2: Creating your first Kubernetes cluster with K3d
  - Exercise 3: Creating a second cluster & switching cluster contexts
  - Exercise 4: Modifying an existing cluster
  - Exercise 5: Deleting clusters