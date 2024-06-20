# Usage Manual

All the results from the test will be expressed in either milliseconds (ms), seconds (s) or minutes (m). Anything higher than this will be denoted as NRT (not reasonable time) and anything that consumes too much RAM will be denoted as NRM (not reasonable memory)

All the algorithms have implementations in Python which can be found at \href{github.link}{\texttt{github.link}}. The code is organised in multiple functions, each representing all the algorithms we have analysed until now, and a function tests($alg, n$), which takes two inputs:
\begin{itemize}
    \item $alg$ - the algorithm that is run,
    \item $n$ - the number of elements the tests mentioned above account for.
\end{itemize}

By running the function tests(), and changing the variables $n$ to be the number of elements you want to test and $alg$ to be which algorithm you want to test for, readers can test and get results of their own.
