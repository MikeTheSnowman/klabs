# About
Here is a quick reference document to provide examples of some commonly used commands with K3d.

# Example Commands

## Creating stuff
### Creating a single node cluster with a default cluster name:
`k3d cluster create`

### Creating a single node cluster with a custom cluster name:
`k3d cluster create myCluster1`

### Creating a multi node cluster with 2 masters and 2 workers:
`k3d cluster create -s 2 -a 2`

### Adding 2 additional worker nodes to an existing cluster:
`k3d node create myAgent --role agent --replicas 2 -c myCluster1`

### Adding a master node to an existing cluster:
`k3d node create myMaster --role server -c myCluster1`

### Creating a private container image registry:
`k3d reg create myReg1`

---
## Getting information
### Listing your clusters:
`k3d cluster list`

### Listing your registries:
`k3d reg list`

---
## Deleting stuff
### Deleting a single node cluster with a default cluster name:
`k3d cluster delete`

### Deleting a single node cluster with a custom cluster name:
`k3d cluster delete myCluster1`

### Creating a private container image registry:
`k3d reg delete myReg1`