# factory
Simple Python snippet to factorize numbers by cuadratic sieve.

# Useful commands

```
~$ python factor.py 1234
~$ cat file_with_one_number_per_line.lst | python factor.py
~$ echo 1234 | python factor.py
~$ seq 1 100 | python factor.py
~$ time [insert here any command of the above]
```
# Hints

Please note that this programm will work relatively fast with numbers 
made up with 3 factors or more. For bigger numbers with less than 3 factors
it will take its time.

# Why

Since I like this kind of veeery useful stuff and 'factor' command from Unix
terminals has a "too large" number restriction I created this simple and 
inefficient snippet to supersede the native command. Please, don't hesitate in
reporting new issues, bugs or enhancements.
