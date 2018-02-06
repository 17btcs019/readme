Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /home/cs2017a118/amulya/program_list1.py =============
>>> a=[1,2,3]
>>> b=a+[4,5,6]
>>> print(b)
[1, 2, 3, 4, 5, 6]
>>> a*2
[1, 2, 3, 1, 2, 3]
>>> a/2
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a/2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> a-b
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> print(a+b)
[1, 2, 3, 1, 2, 3, 4, 5, 6]
>>> 
