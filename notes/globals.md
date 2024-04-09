#bAvoid Globals in Functions

In Python, and in many other programming languages, variables have a property called "scope." The scope of a variable is the parts of the programming that the variable can be accessed from. For example, let's say I have the following function:

```python
def my_cool_function(x: int) -> int:
	y = 3
	return x + y

print(my_cool_function(2))

# `5`
```

The variable `y` is in the scope of the function. It can only be used inside the function. If I try to access `y` outside the function, Python will give me an error.

However the opposite is not generally true. For example:

```python
# file my_cool_script.py
y = 3
def my_function(x: int) -> int:
	return x + y

print(my_function(2))

>> 5
```

This will work without an error. The variable `y` is in the global scope. It can be accessed from anywhere in the script. This is known as a "global variable."

Global variables make it very hard to track the logic in your code. I can change the value from anywhere in the script (or even from another script entirely!) and the function will behave differently. This makes it very difficult to debug code and is generally considered bad practice. You should always pass variables to functions as arguments:

```python
# file my_cool_script.py
def my_function(x: int, y: int) -> int:
	return x + y

y = 3 
print(my_function(2, y))

>> 5
```

Note that `y` is used both inside the function as an argument, and outside the function as a variable. This is because the variable `y` is an argument to the function, and python is smart enough to understand to use the argument `y` in instead of the global variable `y`. However, it might be a good idea to rename the argument or the variable to avoid confusion.

As with any rule, there are a few exceptions. However there are *no* cases where using global variables is the *only* solution, so I would recommend avoiding them entirely unless you're sure you know what you're doing.
