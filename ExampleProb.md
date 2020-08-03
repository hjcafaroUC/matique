# Example

We will give a broad overview of the syntax of matique. For an example, we will use [Codeforces Problem 702A](https://codeforces.com/problemset/problem/702/A)

# How to Use

Matique can be used both in a REPL format, where the program will interactively prompt you for information, and in a compiler format, where a text file of instructions is automatically compiled by the parser. Upon running mainprog.py, you will be prompted to choose one of these options, and specify a file to compile from. You will also be prompted whether output should be sent to a .cpp file or copied to standard console output. For this tutorial, we will assume you are compiling from a file. 

# Problem Solution

This is a simple problem, but a naive approach of calculating every subarray and checking if it is increasing is hopelessly inefficient. For an O(n) solution, we define the function f(i) as the length of the longest increasing subarray that ends at index i. This can be efficiently calculated if we know the value of f(i-1). If there is an increasing subarray of length n ending at index i-1, and a\[i] > a\[i-1], then we can append a\[i] to that subarray to get a sequence of length n+1. Otherwise, f(i) must equal 1. Our final answer will just be the max of f(i) over all valid i: the maximum length of an increasing subarray ending at any index. 


# DP-Space and Data-Space

We must begin by defining the DP-Space and the Data-Space that we're dealing with. The DP-Space is just the space over which we want to call our function f(i); it therefore has dimension 1, since f is a function of 1 variable. It is bounded by 100000, since this is the maximum array size (a constraint of the problem). So our matique code must begin as:

~~~
;dp
1
100000
~~~

Notice the semicolon beginning the first line-this means this line is a comment, and will be ignored by the parser. The code would still be valid without the comment, but it is proper style to include it for clarity.The Data-Space is the underlying data we want to interact with, our array. In this case the dimensions and bounds of our data are the same as our DP-Space, but this is not true in general. We could type

~~~
;data
1
100000
~~~

to size our data, but we can also use the shortcut command `sm`

~~~
;data
sm
~~~

The next input is the number of constants c1,c2,etc. that the program will need. In this case we don't need any constants, so we can enter 0.

~~~
;dp
1
100000
;data
sm
;constants
0
~~~

Remember again that any commented lines are ignored, and the code is still valid without them. 

# Defining the function

We now need to define the function f(i) that we previously stated. The function definition must begin with the command `sw` to form a switch statement, and will then be a series of boolean conditions and rules for function evaluation. The first case we need to consider is i==0; in this case, our function must return 1.

~~~
;f
sw
i=0
1
~~~

"i=0" is parsed to the C++ code "x1==0". The smart input parser automatically makes the transformations "i -> x1, j -> x2, k-> x3," replaces "=" with "==" and a few other substitutions for user ease. The next case we need to consider is when a\[i-1] is less than a\[i]. We know that since we already handled the case i=0, we don't have to worry about accessing array elements out of bounds, so we type:

~~~
ai-1 < ai
fi-1 + 1
~~~

Again, this is smart-parsed to the C++ 

```
if(a[i-1] < a[i]){
 return f(i-1)+1;
}
```

Now, in our final case, we want to just return 1. We use the command el to end the switch statement:

```
el
1
```
`el` is required to complete the function definition. 
~~~
;f
sw
i=0
1
ai-1 < ai
fi-1 + 1
el
1
~~~
# Input and Output

Finally, we need to define the system of our input and output. For this problem, we need to read the contents of an array into memory. This is a common case, so we just use the command `st` for standard. The answer is going to be the maximum of our function f over the entire DP-space: another common case, so we use the command `mx`

```
;dp
1
100000
;data
sm
;constants
0
;f
sw
i=0
1
ai-1 < ai
fi-1 + 1
el
1
;io
st
mx
;end
```

