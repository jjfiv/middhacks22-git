"""
This is a python file for you to play with. 

For fun, it is also runnable:
python3 johnf.py

Author: johnf@middlebury.edu
Keeping an author in a file in git like this is redundant.
"""

def hello():
    return "Hello Git! Again."

def print_triangle(n, rev=False):
    if rev:
        for i in reversed(range(n)):
            print("." * i)
    else:
        for i in range(n):
            print("." * i)


# Yes, the example file is in Python.
if __name__ == '__main__':
  print_triangle(10)
  print(hello())
