def one(a, n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
        print('a equals' + str(a))
  

# one(1, 2) #4, 8
# one(2, 2) #4, 8
# one(3, 2) #4, 8
# one(1, 1) #1
# one(1, 3) # 9, 18, 37
# one(1, 4) # 16, 32, 48, 64
# one(1, 5) # 25, 50, 75,100, 125

