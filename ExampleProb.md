# Users guide

We will give a broad overview of how to use matiquepro. For an example, we will use [Codeforces Problem 702A](https://codeforces.com/problemset/problem/702/A)

# DP Space and Data space.

To solve your dp problem, begin by defining the "dp space" that your program will interact with. In this case we imagine the function f(i), defined as the size of the longest increasing subarray ending at index i
of the array. The "dp space" therefore has dimension 1. The bounds of the dp space can be gleaned from the problem statement, in this case we can use the bound
of 100000. You will next be prompted to define the "data space," which will store the input data that your program interacts with. In this case, the data space has
the same dimensionality and bounds as the "dp space", so instead of repeating the previous input, you can type "sm" as a shortcut to copy the size of the dp space 
for the data space. 

# Defining the function

We now need to define the function f(i) that we previously stated. When prompted for the input rule, enter "sw" to begin creating a switch statement to evaluate f.
You can now succesively enter the boolean conditions and the evaluation rule for each case, like so:

x1==0

1

a[x1-1] < a[x1]

f(x1-1)+1

el 

1

Notice that the final, catchall case of the sw statement is invoked with the command "el". This switch statement is formed in the underlying C++ code as a series of 
if...else if statements, so only as many booleans as it takes to find a true one will be evaluated. For this reason, the boolean a[x1-1] will not cause an error, because the
case x1==0 was covered earlier in the sequence. a is used to refer to the underlying data array, and f is used as a recursive call to this same function. Notice also that the
variables x1,x2,x...,xn are the arguments of the function f(). Convince yourself of the logical correctness of this definition: the longest increasing subarray ending at index 0 can clearly have length 1, and for further indices, the length of the
longest increasing subarray depends on whether the previous element is less than the current one. 

# Input and Output

Next, you will be prompted for your input and output methods. In this case, we want to fill the data array a with data from the standard input, so enter the command
"st" or "standard" to automatically fill the array with data from cin. For output, we need to consider the answer to our question. We want the maximum subarray
ending at any point of the array, so what we want is the maximum of the function f() over our dp space. For this case, enter the command "mx" which will automatically
find and print the maximum value of f() over our dp space. 

