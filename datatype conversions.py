Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
int(46)
46
int(90.5)
90
int("Siri")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("Siri")
ValueError: invalid literal for int() with base 10: 'Siri'
int(4+5j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(4+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#FLOAT
float(87)
87.0
float(77.9)
77.9
float("Python")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float("Python")
ValueError: could not convert string to float: 'Python'
float(34j+7)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(34j+7)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#String
str(34)
'34'
str(13.7)
'13.7'
str("Hello Python")
'Hello Python'
str(5j)
'5j'
str(False)
'False'
str(True)
'True'
>>> str(0)
'0'
>>> str(-23)
'-23'
>>> str(20j+6)
'(6+20j)'
>>> #Complex
>>> complex(0)
0j
>>> complex(-43)
(-43+0j)
>>> complex(-7.2)
(-7.2+0j)
>>> complex("Real")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex("Real")
ValueError: complex() arg is a malformed string
>>> complex(2j+7)
(7+2j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #Boolean
>>> bool(0)
False
>>> bool(-23)
True
>>> bool(-3.7)
True
>>> bool("Hii")
True
>>> bool(3j+234)
True
>>> bool(True)
True
>>> bool(False)
False
