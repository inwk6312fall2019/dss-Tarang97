# Memoize the Ackermann function from Exercise 6.2 and see if memorization makes it
# possible to evaluate the function with bigger arguments.

def ackermann(m,n):
    if m == 0:
        return (n + 1)
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1,ackermann(m,n - 1))
print(ackermann(13,14))

# If we use larger values for m and n as an argument, then we'll get an 'RecrusionError'
# about maximum recursion depth exceeded in comparison. The reason why because when the value of
# m with 13 iterations and n with 14 iterations goes to '0' then what happens is, the first condition
# satisfies and increase the value of n by 1 then it move forward to third condition where m increase by 1
# then after returning third condition it again decreases m by -1 and increase the value of n by 1.
# The Point is line 8 and line 10 is recursively changing the value of m and n by itself and that
# leads to 'RecrusionError' where recursion depth is exceeded in comparison.
# Ackermann function illustrates that not all total computable functions are primitive recursive.