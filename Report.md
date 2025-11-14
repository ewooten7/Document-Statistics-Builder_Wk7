# Report 


1. When you fail to add a base case in recursion, you will return a error value (crashing your program). What is the error value? If you don't know, try running the following code...
```python
def factorial(n):
    return n * factorial(n-1)
```
2. Describe a base case in your own words. What is the base case needed for the code above?
   
3. Thinking about for-in loops, they all work on sequential data, so based on that, what is each "item" for each of these sequential data types. Separate each item by a comma after the => symbol. 
    * Example: range(1, 3) => 1, 2
    * ('aloha', 'world') => 
    * ['aloha', 'world'] =>
    * 'aloha world' =>

4. For this for-in loop, write an equivalent while loop. 
```python
for i in range(1, 10, 2):
    print(i)
```
```python
# your code here

```

## Deeper Thinking

The fibonacci sequence is a very famous sequence found in nature. It is defined as the sum of the previous two numbers in the sequence. The first two numbers are 0 and 1. So the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc. If you do a quick search online, you will find that it can be written both recursively and iteratively.

For this deeper thinking, you will work on an experiment. Write a recursive fibonacci function and an iterative fibonacci function. Then, time how long it takes to run each function for the first 30 fibonacci numbers. You can use the following code to time your functions. 


```python

import time

def fibonacci_iterative(n):
    # your code here
    pass

def fibonacci_recursive(n):
    # your code here
    pass


def time_function(func, *args):
  # Get the start time
  start = time.time()
  # Call the function with the given arguments
  result = func(*args)
  # Get the end time
  end = time.time()
  # Calculate the elapsed time
  elapsed = end - start
  # Return the result and the elapsed time
  return result, elapsed

def main():

    print("Fibonacci(10) =", time_function(fibonacci_iterative, 10))
    print("Fibonacci(20) =", time_function(fibonacci_iterative, 20))
    print("Fibonacci(30) =", time_function(fibonacci_iterative, 30))

    print("Fibonacci(10) =", time_function(fibonacci_recursive, 10))
    print("Fibonacci(20) =", time_function(fibonacci_recursive, 20))
    print("Fibonacci(30) =", time_function(fibonacci_recursive, 30))

if __name__ == "__main__":
    main()

```

Report on your results here:



Which one takes longer? Why do you think that is? 
