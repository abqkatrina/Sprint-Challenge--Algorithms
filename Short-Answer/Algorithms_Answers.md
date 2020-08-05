#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
<!-- a = 0
    while (a < n * n * n):
      a = a + n * n -->
simple operation, repeated while a is less than n^3
number of operations per call increases equally with increase in n but not a

 --> linear O(n)


b)
 <!-- sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1 -->
4:8 (2) --> 5:15 (3) +1(+1)--> 6:18 (4) +1(+1)
with an increase of range, increase runs by equal amount
--> linearithmic O(n log n)


c)
<!-- 
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      return 2 + bunnyEars(bunnies-1) -->
this is recursive, so repeats on itself until bunnies is 0
that means it performs the operation as many times as the number of bunnies and returns one number

--> linear O(n)


## Exercise II

n = total number of floors
f = lowest breaking floor
< f = safe floors

mid = n/2 
    --> if egg breaks, f < mid, else f > mid

l = :mid/2 --> 1/4 of n --> if egg breaks, f < l, else f is between l and mid
r = mid:/2 --> 3/4 of n --> if egg breaks, f is between mid and r, else f > r
rinse and repeat until narrowed down to f

this is like binary search which is O(log n) (logarithmic)
