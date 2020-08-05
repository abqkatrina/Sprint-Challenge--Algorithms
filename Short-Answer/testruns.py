# def one(a, n):
#     a = 0
#     while (a < n * n * n):
#         a = a + n * n
#         print('a equals' + str(a))
  

# one(1, 2) #4, 8
# one(2, 2) #4, 8
# one(3, 2) #4, 8
# one(1, 1) #1
# one(1, 3) # 9, 18, 37
# one(1, 4) # 16, 32, 48, 64
# one(1, 5) # 25, 50, 75,100, 125

def two(n):
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1
            print(sum)
# two(4) adds to sum 8x -- +1 but x2
# two(5) adds to sum 15x -- +1 but x3
# two(6) adds to sum 18x -- +1 but x4

# def bunnyEars(bunnies):
#     if bunnies == 0:
#         return 0   
#     print(bunnies)
#     return 2 + bunnyEars(bunnies-1)

# print(bunnyEars(0)) prints bunnies: 0
# print(bunnyEars(1)) prints bunnies: 1, 2
# print(bunnyEars(2)) prints bunnies: 2..1, 4
# print(bunnyEars(5)) prints bunnies: 5...1, 10
# print(bunnyEars(8)) prints bunnies: 8 ...1, 16
# print(bunnyEars(100)) prints bunnies: 100 ... 1, 200