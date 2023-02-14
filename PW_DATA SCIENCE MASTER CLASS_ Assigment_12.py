#!/usr/bin/env python
# coding: utf-8

# # Assignment_13-02-2023

# ## 1. Explain why we have to use the exception class while creating a custom exception.
# 
# ### Ans:-
#     Using the exception class while creating a custom exception allows us to create a new type of exception that can be 
#     easily recognized and handled in a specific way by the program. By subclassing the built-in exception class, we can 
#     define our own exception type with custom attributes and behavior that makes it distinct from other exceptions.
#     Additionally, using the exception class ensures that our custom exception is compatible with existing exception
#     handling mechanisms, making it easier to catch and handle in our code.
# 

# ## 2. Write a python program to point Exception Hierarchy.
# 
# ### Ans:-
# 

# In[1]:


## Python program that demonstrates the Exception Hierarchy:
try:
    # code that may raise an exception
    raise NotImplementedError()
except Exception as e:
    # prints the exception hierarchy
    print(type(e).__name__)
    while e.__cause__:
        e = e.__cause__
        print(f'Caused by: {type(e).__name__}')


# ### 
#     This program raises a NotImplementedError exception and then prints the hierarchy of exceptions that are caught by the
#     except block. The type(e).__name__ statement returns the name of the exception class, while the e.__cause__ statement 
#     returns the next exception in the hierarchy (if there is one).
#     
#     Since NotImplementedError is a built-in exception class and does not have a cause, the program only prints the name of 
#     the exception class once.

# ## What errors are defined in the Arithmetic Error class? Example two with an example.
# 
# ### Ans:-
#     The ArithmeticError class is a built-in exception class in Python that represents errors that occur during arithmetic
#     operations. It is the parent class for more specific arithmetic-related exceptions like 
#     
#     1.ZeroDivisionError, 
#     
#     2.OverflowError,
#     
#     3.FloatingPointError, and others.
# 

# In[2]:


## ZeroDivisionError: This exception is raised when attempting to divide a number by zero.

try:
    result =10/0
except ZeroDivisionError:
    print("Division by Zero")


# In[3]:


""" OverflowError: This exception is raised when a calculation exceeds the maximum 
value that can be represented by the data type"""

import sys

try:
    result = sys.maxsize*2
except OverflowError as r:
    print(r)


# In[4]:


import sys
try:
    result = sys.maxsize * 2
except OverflowError:
    print("Error: Result is too large to represent")


# ## 4. Why Lookup error class in used? Explain with an example key error and index error
# 
# ### Ans:-
#     The LookupError class is a built-in exception class in Python that represents errors that occur when a requested item 
#     cannot be found in a collection, such as a dictionary or list. It is the parent class for more specific lookup-related
#     exceptions like IndexError and KeyError.
#     
#     1.Here are two examples of errors that are subclasses of LookupError:
# 

# In[5]:


## 1.KeyError: This exception is raised when a key is not found in a dictionary.
try:
    dict={'a':1,'b':2,'c':3}
    value = dict['d']
except KeyError:
    print("key not found")


# In[6]:


## 2.IndexError: This exception is raised when trying to access an index that is out of range of a list or other sequence.
try:
    lst=[1,2,3]
    value=lst[4]
except IndexError:
    print("Index out of Range")


# ### 
#     In this example, the code tries to access the item at index 3 in the list my_list, but since the list has only three 
#     items (indexed from 0 to 2), an IndexError is raised. By catching the IndexError exception, we can handle the error
#     gracefully and take appropriate actions.
# 
#     In both examples, the LookupError class is not used directly, but the more specific exceptions KeyError and IndexError 
#     are used instead to indicate the specific type of lookup-related error that occurred.
#                             

# ## 5. Explain Import Error.What is moduleNotFound Error?
# 
# ### Ans:-
#     ImportError is a built-in exception class in Python that is raised when an import statement fails to find and load 
#     a module. This can happen if the module is not installed, the file path is incorrect, or the module is not in 
#     the search path.
#     
#     ModuleNotFoundError is a subclass of ImportError that was added in Python 3.6 to provide a more specific error message
#     when a module cannot be found. Prior to Python 3.6, ImportError was used for all import-related errors, including 
#     module not found errors.
# 

# In[7]:


## example of how ImportError can be raised:
try:
    import my_module
except ImportError:
    print("Module not Found")


# ## List down some best practices for exception handling in python.
# 
# ### Ans:-
#     Here are some best practices for exception handling in Python:
#     
#     1. Use try-except blocks to catch and handle exceptions: Wrap code that may raise an exception inside a try block and
#     catch the exception with an except block. This way, you can handle the error and prevent your program from crashing.
# 
#     2.Catch only the specific exception you expect: Catch only the exceptions that you expect and handle them appropriately.
#     Avoid catching and ignoring all exceptions, as this can hide important errors and make debugging difficult.
#     
#     3.Use finally blocks to clean up resources: Use a finally block to perform cleanup tasks, such as closing files or 
#     releasing network connections, regardless of whether an exception was raised or not.
#     
#     4.Don't catch exceptions silently: Avoid catching exceptions silently and not handling them in any way. This can lead
#     to hard-to-diagnose errors and make debugging difficult.
#     
#     5.Raise exceptions when appropriate: Raise exceptions when you encounter an error that you cannot handle. This allows 
#     the calling code to handle the error or propagate it to a higher level.
#     
#     6.Provide informative error messages: Provide informative error messages that explain what went wrong and how to fix 
#     the problem. This makes debugging easier and can help users troubleshoot issues.
#     
#     7.Follow the "Easier to ask for forgiveness than permission" (EAFP) approach: In Python, it's often easier to ask for
#     forgiveness than to check for permission. This means that you should assume that an operation will succeed and handle 
#     exceptions if it fails, rather than checking for possible errors before performing the operation.
#     
#     8.Be consistent with exception handling: Use consistent exception handling throughout your codebase to make it easier 
#     to read and maintain. Use the same exception types for similar errors and provide consistent error messages.
# 
# 
# 

# In[ ]:




