Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 23
type(a)
<class 'int'>
a = 0
type(a)
<class 'int'>
b = 23.56
type(b)
<class 'float'>
c = "Python"
type(c)
<class 'str'>
c = 'Language'
type(c)
<class 'str'>
d = '''My name is Sundari. I am 23 years old'''
type(d)
<class 'str'>
e = 3j+32
type(e)
<class 'complex'>
f = 55+2j
type(f)
<class 'complex'>
g = 3j
>>> type(g)
<class 'complex'>
>>> f = i
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    f = i
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> d = True
>>> type(d)
<class 'bool'>
>>> f = False
>>> type(f)
<class 'bool'>
>>> d = true
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> e = -34
>>> type(e)
<class 'int'>
>>> f = -45.67
>>> type(f)
<class 'float'>
>>> g = 34-6j
>>> type(g)
<class 'complex'>
>>> f = j
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f = j
NameError: name 'j' is not defined
>>> g = 234+45j
>>> type(g)
<class 'complex'>
>>> gd =
SyntaxError: invalid syntax
>>> gd = "Geetha"
>>> type(gd)
<class 'str'>
