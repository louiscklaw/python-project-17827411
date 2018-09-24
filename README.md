### Question
1. Define function that asks user for his/her name and displays it.

2. Define function that takes a name as a parameter and displays the name

3. Define function “smallest” that returns the smallest number from a given list.

4. The following code has an error. Please fix the error and make the code display both listA and listaB.

```
def ask5num():

    l=[]

    for i in range(1,6):

        number = input("please provide a number: ")

        l.append(number)

        listA = ask5num()

        print("listaA is: ",listA)

        listB = listA +[1]

        print("listaB is: ",listB)
```

5. Please write two functions.

Function one to create a local variable called “a” that equals the sum of a global variable called “glob” plus 10.

Function two to create a variable “b” that is the sum of the same “glob” variable plus 100.

Please display the global variable and both local variables. Set your global variable to 1000.

### to test
`python3 test_freelancer_python.py`

### ref:
[https://www.freelancer.com/projects/software-architecture/python-project-17827411/](https://www.freelancer.com/projects/software-architecture/python-project-17827411/)
