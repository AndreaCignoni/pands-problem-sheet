# pands-problem-sheet
# <p align="center">Helloworld.py
</p>

**This program says "Hello World!"**
</p>

<p align="justify">A “Hello world!” program is traditionally used to introduce novice programmers to a programming language. This sentence is a string, which generally is a sequence of characters but, even a single character, can be considered a string. In Python, strings are "immutable" which means they cannot be changed after they are created and, if you try to modify any value in a string, it will throw an error. In order to incorporate the changes, you must create a new string.

In practice, to generate a string, you need to wrap a character or a sequence of characters in quotation marks. There can be multiple ways of doing this:

- Single quotes that allow you to embed "double" quotes in your string.'
* Double quotes that allow you to embed 'single' quotes in your string.
+ Triple quotes that allow to embed "double quotes" as well as 'single quotes' in your string. 

Strings can also span across multiple lines.
</dd>


# <p align="center"> Bank.py 
</p>

**Bank.py sums 2 amounts in cent and convert them into Euro.**

<p align="justify">This code is created generating two variables whose objects is attributed by a user, a sum of the two integers promped that returns a floating number with two decimals and a final output that provide an answer concatenating a string with the result of the addition. These steps are detailed as follows:

- *Input function and two variable generation.*

In this task, the user is prompted to insert two numbers through the input function (input). This function is in built in Python and you call it to tell the program to stop and wait for the user to key in the data. These inputs provided by the user are here assigned as the objects to the variables number1 and and number2 respectively. Variables are defined as such by the equal sign which establishes the connection between the two elements and the numbers typed by the user. In fact, a Python variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name.

For further information on variables and its usage, please refer to this article in [realpython. com](https://realpython.com/python-variables/#:~:text=A%20Python%20variable%20is%20a,the%20object%20by%20that%20name).

* *Sum of the two integers: use of integer and floating numbers.*

Calculations in Python operate the same way they do in real life. As if with any calculator,numbers can be added, subtracted multiplied and divided using +, -, * and / symbols respectively. In Python, data types define what type of data or values variables can hold. Numbers have three data points in Python. These are:  

**Int**: Integers or whole numbers. Can range from 0 to any number imaginable. Can also contain negative numbers within the same range.  

**Float**: Floating-point numbers or numbers that contain decimal points. Floats can contain negative numbers as well as positive numbers so long as they have a decimal point in them. Unlike integers, floating-point numbers do have a maximum size, at which point they become inf or -inf (in the case of negative numbers), which stands for infinity – even though it isn’t technically infinite.  

**Complex numbers**: Complex numbers are used for data science scientific notation, and high-level math.

In the addition performed in the present program, the main issues were to sum two positive integers, convert them in to cents and returninga result with a decimal point between the euro and cent of the amount.I have overcome this problem dividing the added amounts by 100 and formatting the result with the float() function.

+ *Outputing an answer including the addition result.*

The last step to complete this assignment consisted in outputing an intelegible answer to the user providing the result of the addition of the two numbers. This implied printing a concatenation of two strings: the answer to provide and the result in Euros. In Python, there are a few ways to concatenate or combine strings. In order to merge two strings into a single object, you may use the + operator. However, since in this instance the concatenation included a string and a non-string type variable, namely the amount to provide, it was necessary to cast this last element into a string through the str() function.

My main point of reference here was [digitalocean.com](https://www.digitalocean.com/community/tutorials/python-concatenate-string-and-int)
</dd>

# <p align="center">Accounts.py
</p>

**This program returns a masked account number with X showing the last 4 digits only**

<p align="justify">Here, I have put into practice three basic methods: inputing, concatenating strings and outputing slices of code. The input function was replicated as per the Bank.py program previously illustrated in the present Readme file.

My main point of reference for learning how to request an input from a user was [W3School](https://www.w3schools.com/python/python_user_input.asp)

The main challenge in this task was to output an answer where only the last 4 characters of the bank account were displayed and while the other 6 digits were replaced with Xs. Again, as in the previous code, the possible solution to perform such an output was to concatenate a series of Xs corresponding to the numbers of integers inserted by the user minus the last four digits and add a slice of the 4 last digits corresponding to the actual account number given. This last non string element had to be, therefore, output with the slicing function giving the last 4 numbers from the end.

Generally speaking, a slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item. In this case, the action requested was to get the characters from position 4, and all the way to the end. To perform this method, I followed all the instructions illustrated in [w2school](https://www.w3schools.com/python/python_strings_slicing.asp).
</dd>

# <p align="center"> Collatz.py
</p>

**This array triggers the collatz calculation and stops with the final 4-1-0 loop.**

<p align="justify">The Collatz Conjecture is the simplest math problem no one can solve. The rules of the sequence depend on the parity of the number itself. If the number is even, then the rule returns half the original number. If the number is odd, then we multiply the number by three, and add one. The conjecture asks whether repeating these two simple arithmetic operations will eventually transform every positive integer into 1.In fact, as shown with the program, the whole always reaches 1, no matter which positive integer is chosen to start the sequence.  
In order to perform this task, it was necessary to create a **function** not in-built in Python and a loop to repeat the consequent calculation until the cycle is completed.  
A **function** is a reusable block of code that can perform a basic task and it used to avoid rewriting the same logic or code again and again in a program. In practice, a **function** in Python is defined with the **def** keyword, followed by the **function** names, zero or more argument names contained in parenthesis **()**, and a colon **:** to indicate the start of the function.  
The task itself required to perfom the Collantz conjecture so I consequently called this function"collantz". The contents of the function then had follow and the calculation cycle requested to divide by two if the number promped by the user was even or multiply it by three and add one if the input was odd in a loop.Finally, as this cycle had to be repeated until the final amount was 1, a return statement had to follow. In fact, **return statements** are necessary whenever it is required to control the flow of a program as in this case.  
For a very informative and detailed explanation on how to define and call function, please refer to [Realpython.com](https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/)  
Since the collantz calculation had to be repeated something over and over until the result was equal to 1, I have then implemented a **loop** that iterated the task until this condition was satisfied. A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as a specific outcome is obtained. The two steps to execute included to check whether the number number provided was even or odd and,then, to apply the operations consequently. Therefore, as this calculation had to be performed as long as a condition was true (n>1), I have decided to shape this collantz function using a **while loop**.  
In python, a **while loop** is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed. The **else** clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won’t be executed.  
My main point of reference in this case has been [geeksforgeeks.org](https://www.geeksforgeeks.org/loops-in-python/).</dd>

# <p align="center"> Weekday.py#
</p>

**Week.py says whether current day is a weekday or a weekend.**

# <p align="center"> SquareRoot.py
</p>

**This program receives any number and returns its square root using the Newman method.**

<p align="justify">The square_root() function takes a number as an input, sets a level of accuracy for the approximation, assigns the input number to a variable k, and initializes an initial guess for the square root to be half the input number.
</dd>

# <p align="center"> Es.py
</p>

**this program open a file called "Anne Of Green Gable" and reads the text calculating the number of letter 'e' contained.**

# <p align="center"> Plottask.py
</p>

**This code generates a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2.**