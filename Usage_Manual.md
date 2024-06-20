# Usage Manual

All the results from the test will be expressed in either milliseconds (ms), seconds (s) or minutes (m). 
Anything higher than this will be denoted as NRT (not reasonable time) 
and anything that consumes too much RAM will be denoted as NRM (not reasonable memory)

The code is organised in multiple functions, each representing all the algorithms we have analysed until now, 
and a function tests(alg, n), which takes two inputs:
alg - the algorithm that is run,
n - the number of elements the tests mentioned above account for.

By running the function tests(), and changing the variables n to be the number of elements you want to test 
and alg to be which algorithm you want to test for, readers can test and get results of their own.

For the conduction of my experiments (i.e the results in the paper) I have used the following hardware:
Macbook Air M2

!NOTE: In order to ensure that the algorithms will run, please install the Numpy module using the command:
```pip install numpy``` or ```pip3 install numpy``` in the terminal.
