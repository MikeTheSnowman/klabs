# Exercise 1 - Make scalars or different data types

<!-- MarkdownTOC -->

  - [Exercise Description](#exercise-description)
    - [Example 1: scalar as value to a key](#example-1-scalar-as-value-to-a-key)
    - [Example 2: scalar as an element of a list of strings](#example-2-scalar-as-an-element-of-a-list-of-strings)
    - [Example 3: scalar as an element of a list of numbers](#example-3-scalar-as-an-element-of-a-list-of-numbers)
  - [Exercise Instructions](#exercise-instructions)

<!-- /MarkdownTOC -->
# Exercise Description
For this exercise, you will learn about the different data types that you can supply as a value to a key. 
In the world of YAML, they have this thing called a "**scalar**". A **scalar** is simply either a string of **characters** or **numbers** that are supplied as a value to a key, or as an element of a list.

For example, consider the three YAML examples below. All of them are showing **scalars** in slightly different ways:

## Example 1 (scalar as value to a key):
```
---
person:
  name: Bob   # The value "Bob" is a scalar and the data type of this scalar is a "string"
  age: 45     # The value "45" is also a scalar and the data type of this scalar is a "number" (or "integer" if you want to be technical)
```

## Example 2 (scalar as an element of a list of strings):
```
---
my_inventory:
  - tomatoes    # Please note that each element of a list is prefixed with '- ' with each value.
  - beef        # Each value in this list/array is a scalar with a data type of "string"
  - apples
```

## Example 3 (scalar as an element of a list of numbers):
```
---
employee_ages:
  - 32.2    # Please note that each element of a list is prefixed with '- ' with each value.
  - 44.1    # Each value in this list/array is a scalar with a data type of "float"
  - 28.9
```

# Exercise Instructions

  - Open the file `l1_e1.yaml` and supply the appripiate scalar (values) to all the keys.

  - After supplying all the values, run the following command to check your work:

`./check-work`

  - You can run the above command from within Visual Studio Code using the built in terminal. To open the terminal within VS Code, press the following keys together:
  
``ctrl + shift + ` ``

---
After completing the this exercise, please click on the button below to go to the next exercise where you'll learn about **mappings**.
<br><a href="../exercise-2/README.md"><img style="margin-bottom:-50px; padding-bottom:3px" src="../../assets/btn_Exercise2.svg" width="150" height="100" alt="Next Exercise"></a>