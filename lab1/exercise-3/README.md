- [Exercise Description (Make two different sequences):](#exercise-description-make-two-different-sequences)
  - [Example 1 (using the "-" character):](#example-1-using-the---character)
  - [Example 2 (using square brackets):](#example-2-using-square-brackets)
  - [Example 3 (sequences of mappings):](#example-3-sequences-of-mappings)
- [Exercise Instructions:](#exercise-instructions)

# Exercise Description (Make two different sequences):
The next primitave YAML data structure that we'll talk about is a **sequence**. One way of explaining what a sequence is, is that a sequence is YAML's way of organizing data in an **array** (or **list** depending on what your preferred programming language is).

Below are a few different way's that you can create a sequence:

## Example 1 (using the "-" character):
```
---
MyHobbies: 
  - hiking
  - fishing
  - swimming

```

## Example 2 (using square brackets):
```
---
MyHobbies: ["hiking", "fishing", "swimming"]

```

## Example 3 (sequences of mappings):
```
---
AboutMe:
  - InfoType: FirstName
    Value: Mike
  - InfoType: Age
    Value: 30
  - InfoType: Hobby
    Value: Hiking
  - InfoType: Hobby
    Value: Fishing
  - InfoType: Hobby
    Value: Swimming

```

# Exercise Instructions:

  1. Open the file `l1_e3.yaml` and supply the appripiate scalar (values) to all the keys.

  2. Open the terminal within VS Code, press the following keys together: ``ctrl + shift + ` ``

  3. Change directory to this exercise folder with the following command: `cd ~/Kubernetes_Labs/lab1/exercise-3`

  4. After supplying all the values, run the following command to check your work: `./check-work`
