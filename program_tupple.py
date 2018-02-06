Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /home/cs2017a118/amulya/program_tupple.py =============
Traceback (most recent call last):
  File "/home/cs2017a118/amulya/program_tupple.py", line 2, in <module>
    a[2]
NameError: name 'a' is not defined
>>> t=(1,2,3,4,5)
>>> t[2]
3
>>> t[2]=10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t[2]=10
TypeError: 'tuple' object does not support item assignment
>>> t[0:6]
(1, 2, 3, 4, 5)
>>> 
