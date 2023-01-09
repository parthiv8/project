#!/usr/bin/env python
# coding: utf-8

# In[46]:


def is_natural_number(n):
    if isinstance(n, int) and n > 0:
        return True
        return False

# Get input from the user
n = int(input("Enter a number: "))

if is_natural_number(n):
      print(f"{n} is a natural number.")
else:
      print(f"{n} is not a natural number.")
    


# In[36]:


import math
import numpy


# In[47]:


mylist = ['tree', 'apple', 'mango', 'melon']
urlist = ['wood','knife','axe']
mylist + urlist


# In[48]:


num = int(input("Enter the number:    "))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# In[ ]:





# In[10]:


class Palindrome:
    def __init__(self, word):
        self.word = word

    def is_palindrome(self):
        reverse = self.word[::-1]
        if self.word == reverse:
            return True
        else:
            return False


def main():
    word = input("Enter a word: ")
    p = Palindrome(word)
    if p.is_palindrome():
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")


if __name__ == "__main__":
    main()


# In[14]:





# In[ ]:





# In[15]:


import tkinter as tk


root = tk.Tk()
selected = tk.StringVar()
option1 = tk.Radiobutton(root, text="Option 1", variable=selected, value="Option 1")
option2 = tk.Radiobutton(root, text="Option 2", variable=selected, value="Option 2")
option1.pack()
option2.pack()

root.mainloop()


# In[27]:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(p1, p2):
        try:
            distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
            return distance
        except ValueError:
            return "Invalid input."
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(distance(p1, p2))


# In[28]:


with open("hello.txt", "w") as f:
      f.write("hello world")

print("Text written to file.")


# In[29]:


name = "Guvi python"
words = name.split()
python = words[1]

print(python)


# In[30]:


import re

x = " 89e9jcd^o38829@3%3,/mkl$w1"

numbers = re.findall(r"\d", x)
result = "".join(numbers)

print(result)


# In[31]:


def create_equation(a, b, c):
      return (a+b+c) * (a-b-c) * a * b + a**2 + b**2 + (a*b*c)**3

print(create_equation(1, 2, 3))


# In[ ]:




