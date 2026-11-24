Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
print(a)
10
 a = 10
 
SyntaxError: unexpected indent
a = "Hello"
print(a)
Hello
a_ = 10
print(a_)
10
2a = 3
SyntaxError: invalid decimal literal
6 = 5
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
x = 35
print(X)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
a,b,c = 12,34,87
print(a,b,c)
12 34 87
a=b=c=2
print(a,b,c)
2 2 2
a,b = 2,8,69,87
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a,b = 2,8,69,87
ValueError: too many values to unpack (expected 2, got 4)
f name = "Nikki"
SyntaxError: invalid syntax
f_name = "Python"
print(f_name)
Python
>>> f_name = "Python is"
>>> l_name = "Language"
>>> print(f_name,l_name)
Python is Language
>>> print(f_name+" "+l_name)
Python is Language
>>> a=4,b=6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=7;b=89
>>> print(a,b)
7 89
>>> NAME = "Siri"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'NAME'?
>>> print(NAME)
Siri
>>> print("Name")
Name
>>> @ = 90
SyntaxError: invalid syntax
>>> b = 57
>>> print(b)
57
>>> del b
>>> print(b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
>>> a = 7,39,98,23
>>> print(a)
(7, 39, 98, 23)
>>> a,y = 9,0,44,78,98
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a,y = 9,0,44,78,98
ValueError: too many values to unpack (expected 2, got 5)
