Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arithematic operator
a = 8
b = 3
print(a+b)
11
print(a-b)
5
a = 5
b = 4
print(a*b)
20
print(a/b)
1.25
print(a//b)
1
print(a**b)
625
print(a%b)
1
a = 24
b = 18
print(a/b)
1.3333333333333333
print(a%b)
6
print(a//b)
1

#Assignment operator
a = 6
b = 3
a+=b
a
9
b+=a
b
12
b-=a
b
3
b*=5
b
15
b/=3
b
5.0
b//=2
b
2.0
b**=10
b
1024.0
b%=6
b
4.0
a+=5
a
14
a-=4
a
10
a*=5
a
50
a/=2
a
25.0
a//=3
a
8.0
a%=1
a
0.0

#comparison operator
a = 8
b = 6
a > b
True
b > a
False
a < b
False
a >= b
True
b >= a
False
a <= b
False
a != b
True
a == b
False

#logical operator
a = 8
b = 4
a > b and a < b
False
a > b and b < a
True
a >= b and b <= a
True
a >=b and a <= b
False
a != b and a == b
False
a>b or b>a
True
a<b or b>a
False
a>=b or b>=a
True
a!=b or a==b
True

not True
False
not False
True

#Identity operator
a = 20
b = 15
type(a) is int
True
type(a) is  not int
False
type(a) is float
False
b = "Hello"
type(b) is str
True
type(b) is not str
False
type(b) is not complex
True
b = True
type(b) is not bool
False
type(b) is bool
True
type(a) is str
False
type(a) is not complex
True

#membership operator
a = 3,7,9,23,78,111
78 not in a
False
111 in a
True
12 in a
False
2 not in a
True
b = ()
4 in b
False
0 in b
False
89 not in b
True
>>> 7 in b
False
>>> 
>>> #Bitwise operator
>>> a = 8
>>> b = 2
>>> a&b
0
>>> bin 8
SyntaxError: invalid syntax
>>> bin a
SyntaxError: invalid syntax
>>> bin(a)
'0b1000'
>>> bin(b)
'0b10'
>>> a = 5
>>> b = 4
>>> a&b
4
>>> bin(a)
'0b101'
>>> bin(b)
'0b100'
>>> a|b
5
>>> 
>>> b = 6
>>> ~b
-7
>>> a = -8
>>> ~a
7
>>> c = 0
>>> ~c
-1
