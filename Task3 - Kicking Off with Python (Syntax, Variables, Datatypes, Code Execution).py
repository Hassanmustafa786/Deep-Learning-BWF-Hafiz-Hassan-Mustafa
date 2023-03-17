#!/usr/bin/env python
# coding: utf-8

# # Syntax
# In Python, syntax refers to the set of rules that define how the code must be structured and formatted. Proper syntax is essential for the Python interpreter to understand the code and execute it correctly.
# 
# Here are some important rules of Python syntax:
# 
# **Indentation:** Python uses indentation to denote blocks of code. Indentation refers to the number of spaces or tabs at the beginning of a line. Blocks of code that are at the same level of indentation belong to the same block. This is different from other programming languages that use curly braces to denote blocks of code.
# 
# **Statements:** In Python, statements are the individual instructions that make up a program. A statement typically ends with a newline character, but you can use a semicolon (;) to separate multiple statements on the same line.
# 
# **Comments:** Comments are used to document your code and make it easier to understand. In Python, comments start with the hash symbol (#) and continue to the end of the line. Comments are ignored by the interpreter and do not affect the code's execution.
# 
# These are just a few of the key elements of Python syntax. Python is a highly readable language, and it's designed to be easy to learn and use. By following the rules of Python syntax, you can write clear, concise code that is easy to understand and maintain.

# In[9]:


print("Hello, Hafiz Hassan Mustafa")   #String data
print(100.5)                           #Float data
print(123,"456")                       #Integer & String data


# # Variables
# In Python, variables are created by assigning a value to a name using the equals sign (=). Variable names must follow certain rules, such as starting with a letter or underscore and not using reserved keywords.

# In[12]:


a = "Hafiz Hassan Mustafa"
b = 100.5
c = 45
print(a)
print(b)
print(c)


# # Datatypes
# Python has several built-in datatypes, including:
# 1) Integers
# 2) Floating-point numbers
# 3) Strings
# 4) Lists
# 5) Tuples
# 6) Sets
# 7) Dictionaries
# 8) Booleans

# In[30]:


a = "Hafiz Hassan Mustafa"
b = 100.5
c = 45
d = [1,2,3]
e = (1,2,3)
f = {1,2,3}
g = {"Name" : "Hafiz Hassan Mustafa", "Age":23}
h = True


# In[31]:


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))


# # Code Execution
# When you run a Python program or script, the code is executed by the Python interpreter. The interpreter reads the code line by line and executes each line as it goes. Here's a basic overview of the steps involved in executing Python code:
# 
# 1) Lexical analysis: The interpreter first breaks down the code into smaller units called tokens. These tokens can be keywords, operators, identifiers, or literals.
# 2) Syntax analysis: The interpreter then checks the code for syntax errors. It ensures that the code follows the rules of the Python programming language.
# 3) Compilation: The interpreter then compiles the code into byte code, which is a lower-level representation of the code that can be executed more quickly than the original source code.
# 4) Execution: The interpreter then executes the byte code. As it runs, it reads input from the user and generates output, such as text on the screen or data saved to a file.
# 5) Termination: Finally, the program terminates when it reaches the end of the code or encounters an error.
# 
# Python also allows for the use of modules and packages, which are pre-written code that can be imported and used within your program. These modules and packages can be written in Python or other languages, and they allow for the reuse of code across multiple programs.
