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

The task itself required to perfom the Collantz conjecture so I consequently called this function *collatz*. The contents of the function then had follow and the calculation cycle requested to divide by two if the number promped by the user was even or multiply it by three and add one if the input was odd in a loop.Finally, as this cycle had to be repeated until the final amount was 1, a return statement had to follow. In fact, **return statements** are necessary whenever it is required to control the flow of a program as in this case.

For a very informative and detailed explanation on how to define and call function, please refer to [Realpython.com](https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/)

Since the *collatz* calculation had to be repeated something over and over until the result was equal to 1, I have then implemented a **loop** that iterated the task until this condition was satisfied. A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as a specific outcome is obtained. The two steps to execute included to check whether the number number provided was even or odd and,then, to apply the operations consequently. Therefore, as this calculation had to be performed as long as a condition was true (n>1), I have decided to shape this *collatz* function using a **while loop**.
 
In python, a **while loop** is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed. The **else** clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won’t be executed.  
My main point of reference in this case has been [geeksforgeeks.org](https://www.geeksforgeeks.org/loops-in-python/).
</dd>

# <p align="center"> Weekday.py#
</p>

**Week.py says whether current day is a weekday or a weekend.**
<p align="justify">

The only way I could run it was necessary to import a module as no built-in Python function could accomplish such a task. For a comprehensive list of Python bulit in functions please refer to [w3school](https://www.w3schools.com/python/python_ref_functions.asp).  

On the other hand, we can check all the installed Python modules and get a list of them using the following command inside our Python shell:  
**>> help('modules')**  
When we press the enter key after writing the above-given command, the Python shell will start loading the names of all the locally installed Python modules in our system and retrieve all their related information.  

A module is a file which can perform any kind of task. In fact, any Python file can be referenced as a module that consist of Python code. A Python file called *hello.py* has the module name of *hello* that can be imported into other Python files or used on the Python command line interpreter. When Python imports a module, the interpreter will first search for a built-in module and if a built-in module is not found, the Python interpreter will then search for a file named *hello.py* in a list of directories that it receives from the **sys.path** variable.  

We can import a module in Python by using **the import statement** along with the specific module name. An import statement is made up of the import keyword along with the name of the module. When you are importing a built-in module, your interpreter should complete the task with no feedback returning to the prompt. This means nothing more is needed to start using the  module. In case the module sought for is not installed, the system will receive error message.  

For an updated and comprehensive list of all inner Python modules, please refer to [realpython.com](https://docs.python.org/3/py-modindex.htm).  

When we import a module, we are making it available to us in our current program as a separate namespace. This means that we will have to refer to the function in dot notation, as in [module].[function]. Therefore, in program **weekday.py**, I have declared my variable ("*weekno*") storing the current date as follows:
**datetime.datetime.today().weekday()**  
Where *today* and *weekday* are the two functions inside the module that we want to use and the empty round brackets represent the data to be extracted. All properties and methods of a specified module which can be found through the built-in Python function **dir ()** along with the name of the module.  
To learn how to import modules, I have followed a very instructive and easily understadable tutorial found in [digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3).  

After having created a variable calling the current day, the two conditions required by the task, namely the two different answers to be give in case of a weekday or in a weekend, had to be created through an **if** and **else** statement structure. In this array, the *if statement* evaluates condition. In case, this is true the code inside **if** is executed and the code inside **else** is skipped. On the contrary, if the condition evaluated in the **if** clause results to be false, the code inside **else** is executed and the code inside **if** is skipped.<dd>



# <p align="center"> SquareRoot.py
</p>

**This program receives any number and returns its square root using the Newman method.**
<p align="justify">

The script **squareroot.py** utilizes Newton's method to find the square root of a number through a numerical algorithm. Generally, in complex equations the roots cannot be solved for explicitly, so they must be approximated; that’s where the Newton method comes into play. The first step of the method takes an *initial guess* and uses the function and function derivative to calculate a *next guess*. Then, this *guess* is used in a similar fashion to calculate the *next guess*, and so on, until a tolerance or iteration limit is met. 

To implement this cycle, I have implemented a **square_root()** function that takes a number as an input, sets a level of accuracy for the approximation, assigns the input number to a variable *k*, and initializes an initial *guess* for the square root to be half of the input number.The function then utilizes a *while loop* to iteratively enhance the estimate until it reaches the required accuracy level. In fact, a *while loop* differs from a *for* in that it repeats as long as the condition is true instead of having a set number of iterations. Here the condition is for as long as the error is greater than 0.1.  

The general syntax and structure of my array are:

- *Initial*
- **while** *logic-condition*
- *statements*  
- **end**

▪ **Initial** is a value with the sole purpose of starting the loop by making the condition true.  
▪ **logic-condition** is a logical expression that is either true or false.  
▪ **statements** are the commands to be repeated. One should be an update for the value tested in the condition.

The program, in its basic structure, prompts the user to enter a positive number, then calls the **"square_root"** function with the input value as an argument, and ultimately displays the input number and its estimated square root with one decimal point precision.
</dd>

# <p align="center"> Es.py
</p>

**this program open a file called "Anne Of Green Gable" and reads the text calculating the number of letter 'e' contained.**
<p align="justify">

The main problems presented by the task were accessing a file, reading it and performing a character counting. I have then decided to solve the first issue by importing the **sys module** which let us access system-specific parameters and functions. This module provides functions which are used to manipulate different parts of the Python Runtime Environment and one of these is the **argv** function that returns a list of command line arguments passed to a Python script. In the output, the name of the script is always the item at index 0, and the rest of the arguments are stored at subsequent indices.  

Therefore, this is how I took the filename from the command line arguments:

- **Anne_of_Green_Gable = sys.argv[1]**

**Command line arguments** are those values that are passed during calling of program along with the calling statement. The **sys.argv** takes the command line arguments in the form of a list and the first element of the **sys argv** is the name of the Python file. The second element onwards contains the command line arguments.  
Once the name of the file was found, the next step was to open that same file for reading which I have performed using a with **open statement** as follows:

- **with open(Anne_of_Green_Gable, 'r') as f:**

In Python, you can access a file by using the **open()** method and create a context using the **with Open** statement. This function returns a file object, which has methods and attributes for getting information about and manipulating the opened file. Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once its opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. There are 6 access modes in Python:

- **Read Only (‘r’)**: Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises the I/O error. This is also the default mode in which a file is opened.
+ **Read and Write (‘r+’)**: Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.
* **Write Only (‘w’)**: Open the file for writing. For the existing files, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
- **Write and Read (‘w+’)**: Open the file for reading and writing. For an existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
+ **Append Only (‘a’)**: Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
* **Append and Read (‘a+’)**: Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

My main point of reference here was [geeksforgeeks.org](https://www.geeksforgeeks.org/reading-writing-text-files-python/).  

Since the only operation required was to read the information the file contained, I have performed the opening in a **"r"** mode and then , in order to perform the vowel "e" counter, stored the same file in the variable "*f*". In relation to the **UTF-8 encoding system**, it was added here to translate any Unicode character to a matching unique binary string. The counter was subsequently initialized using the Python built-in **e_count** function that could return the count of a designeted element in the text.

- **e_count = 0**

In the case of a string, the counting begins from the start (**0**) of the string till the end. It is also possible to specify the start and end index from where you want the search to begin The count() method returns an integer value. Since the counting was to be performed line by line, I have then implemented a **for loop** array to parse every single line and where I have also specified the character I wanted to search in them.

To run this code, the terminal command must contain the name the text file whose characters must be counted after the program name itself.
</dd>

# <p align="center"> Plottask.py
</p>
<p align="justify">

**This code generates a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2.**

This assignment consisted in representing a series of data according to the given parameters.The image that had to be generated by the program had, therefore, to map the relationships among the data values provided and describe their connections. When dealing with plots and charts, the most used and comprehensive Python module is certainly **Matplotlib** which allows creating static, animated, and interactive visualizations.Once you import this module, it is possible to create publication quality plots, make interactive figures that can zoom, pan, update, customize visual style and layout, export to many file formats and embed in JupyterLab and Graphical User Interfaces.  

The most common types of layouts that can be implelented with this package are *bar graphs*, *histogram*, *scatterplot*, *area plot*, *pie plot* for viewing the data.

1. The *bar graphs* are used in data comparison where we can measure the changes over a period of time. It can be represented horizontally or vertically. Longer the bar it has the greater the value it contains. This plot is called with the **plt.bar** command that returns an image like the following:

![image.png](https://dz2cdn1.dzone.com/storage/temp/13805530-bar.png)

2. The *histogram plot* is used where the data is been distributed while bar graph is used in comparing the two entities. *Histograms* are preferred during the arrays or data containing the long list. The command to be used in this case is **plt.hist** and here an example of this kind of plot:

![image1.png](https://dz2cdn1.dzone.com/storage/temp/13805531-histogram.png)

3. The *scatter plots* are preferred while comparing the data variables to determine the relationship between dependant and independent variables. The data is displayed as a collection of points, each having the value of one variable which determines the position on the horizontal axis and the value of other variable determines the position on the vertical axis. The command that calls this layout is **plt.scatter**. The following instance is an example of this plot:

![image2.png](https://dz2cdn1.dzone.com/storage/temp/13805532-scatter.png)

4. The *area plots* were also called as *stack plots*. It is quite similar to the line plots and are generated by the **plt.stackplot** command. Area plots are used in tracking the changes over time for two or more related groups that make one whole category. Here an example:

![image3.png](https://dz2cdn1.dzone.com/storage/temp/13805533-area.png)

5. A *pie chart* is a circular graph which is divided into segments or slices of pie. It is used to represent the percentage or proportional data where each slice of pie represents a category and are implemented with the **plt.pie** command. Example code:

![image4.png](https://dz2cdn1.dzone.com/storage/temp/13805534-pie.png)

Once established how to design an *histogram* through the **Matplotlib** module, the second part of the task consisted in implementing the function on which the graph structure had to be built on. For this purpose I have imported the third party package **NumPy** that used to perform a wide variety of mathematical operations on arrays. It adds powerful data structures to Python that guarantee efficient calculations with arrays and matrices and it supplies an enormous library of high-level mathematical functions that operate on these arrays and matrices.

To complete this general pverview on the graph creation in Python, it is worth noticing that both the two above mentioned modules where accessed through **dot (.) notation**. **The dot (.) notation** is a way to access the attribute and methods of each method of instances of different object classes. It is usually preceded by the object instance, in this case **plt** for **Matplotlib** and **np** for **NumPy** while the right end of the dot notation contains the attributes and methods.  

As already pointed out, when creating a plot with **Matplotlib** the first step is to *import* this same module with the following method:

**import matplotlib.pyplot as plt**

 - Define the x-axis and corresponding y-axis values as lists.

# x axis values
**x = [1,2,3]**
# corresponding y axis values
**y = [2,4,1]**

+ Plot them on canvas using .plot() function.

# plotting the points 
**plt.plot(x, y)**

* Give a name to x-axis and y-axis using .xlabel() and .ylabel() functions.

# naming the x axis
**plt.xlabel('x - axis')**
# naming the y axis
**plt.ylabel('y - axis')**

- Give a title to your plot using **.title()** function.

**Plt.title('My first graph!')**
  
+ Finally, to view your plot, we use **.show()** function.

# function to show the plot
**plt.show()**

This structure represents the base on which this module allows us building an incredible amount of sophisticated features. For instance, we can legend and plot more lines on the same graph:

# plotting the line 1 points 
**plt.plot(x1, y1, label = "line 1")**

# plotting the line 2 points 
**plt.plot(x2, y2, label = "line 2")**

We can also create a small rectangular box to explain the types of line and their color using **.legend()** function that will output the information stored in the **label** variable.
  
# show a legend on the plot
**plt.legend()**

The lines  can be customised in many ways establishing their colour, style, width, marker, and adding markers. For instance:

**plt.plot(x, y, color='green', linestyle='dashed', linewidth = ** marker='o', markerfacecolor='blue', markersize=12)**
  
Finally, in order to apply a particular math ratio, we can shape the curves of the plots we are representing applying the functions contained in the **NumPy** module. 

**import numpy as np**

In the following example, we are using **Numpy** to pass a *range*( first two arguments) and an *increment h* (third argument) to the x line as:

**# setting the x - coordinates**
**x = np.arange(0, 2*(np.pi), 0.1)**

Proceeding with this example, to get the corresponding y-axis values, we can simply use the predefined **np.sin()** method on the **NumPy** array.

**# setting the corresponding y - coordinates**
**y = np.sin(x)**
  
The x and y arrays are then developed according to the above parameters implementing **the plt.plot()** function.

**plt.plot(x, y)**

For a better understanding on how to develop a graph, please refer to [Geeksforgeeks.org](https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/) .

Returning to the weekly task we were assigned, my histogram was to be planned on a **normal distribution** of a 1000 values with a **mean** of 5 and **standard deviation** of 2. The method for finding the **normal distribution** of the data with **NumPy** is **random.normal()** which has  three parameters:

•	**loc** – (average) where the top of the bell is located.
•	**Scale** – (standard deviation) how uniform you want the graph to be distributed.
•	**size** – Shape of the returning array

The **mean** value is the average value, while the standard deviation the **scale**, with the **normal distribution** corresponding to the **size**. Therefore,  according to the required array the value of 2 was attributed to the parameter **loc**, the value of 5 to the parameter **scale** and 1000 to the parameter **scalesize**. Once again, the source of my assumptions come from [Geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/) All these three values were then passed to the histogram function **plt.hist()** through a variable called **values**. 

The task then asked me to plot a specific function and create a range of x and y values that corresponded to a given range. I have then proceeded as follows:

1.	Function definition
2.	Creation of a range of continuous x-values and map their corresponding y-values


My function then mirrored the syntax of **h(x)=x3** as requested.

**def h(x)**
**return x**3**

After that this function was created I have defined the x-range and y-range and, in order to do this, I have used the **NumPy** **linspace** function, which creates a range of evenly-spaced numbers.

**X = np.linspace (0, 10, num=100)**

Once we run the plottask.py program the following graph generated is:

![Figure_1.png](Figure_1.png)
</p>