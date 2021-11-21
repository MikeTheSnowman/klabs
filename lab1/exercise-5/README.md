<!-- MarkdownTOC -->

- [Exercise Description (Referencing other data within a YAML document):](#exercise-description-referencing-other-data-within-a-yaml-document)
  - [Example 1 (Anchor and Alias):](#example-1-anchor-and-alias)
  - [Important Caveat:](#important-caveat)
- [Exercise Instructions:](#exercise-instructions)

<!-- /MarkdownTOC -->
# Exercise Description (Referencing other data within a YAML document):
In this exercise, we will talk about how you can reuse values (scalars, mappings, & sequences) by using a feature of YAML called **anchors** and **aliases**.

In a nutshell, you can think of an **anchor** as a way of assigning data to a variable, and an **alias** is a way of referencing that variable to access the assigned data.

- The syntax to create an **anchor** is to use the "&" character followed immediately by some arbitrary name for the anchor. For example: `&anchor321`

- The syntax to create an **alias** is to use the "*" character followed immediately by name of one of your previously defined anchors. `*anchor321`

Below is an example of using an anchor and an alias:

## Example 1 (Anchor and Alias):
```
---
Employees:
  - FirstName: &fName mike  # Here we create an anchor called "fName" with a scalar value of "mike"
    Age: 31
    EmailPrefix: *fName # Here we use an alias to reference the data assigned to the anchor named fName. This means that the scalar value assigned to EmailPrefix is "mike".
```

## Important Caveat:
Please note that there is a very important caveat you need to remember when using **aliases**. The main issue is that you will **not** be able concatenate or combine the data, provided by an **alias** with any other string, number, or boolean. But, you can use an alias within a list or another mapping. 

# Exercise Instructions:

  1. Open the file `l1_e5.yaml` and create an "anchor" and "alias" as described in the YAML document comments.

  2. Open the terminal within VS Code, press the following keys together: ``ctrl + shift + ` ``

  3. Change directory to this exercise folder with the following command: `cd ~/Kubernetes_Labs/lab1/exercise-5`

  4. After supplying all the values, run the following command to check your work: `./check-work`
