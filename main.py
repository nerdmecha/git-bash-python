# 2024 apr 27th thu pm 12:14 utc+09:00

# sum of evens 1 ~ 10
def sum_for(a, b):
    for i in range(1, 10, 1):
        if (i%2==0):
            a=a+i
            b=b+1
    print(a, b)

sum_for(0, 0)

# sum x to 1
def sum_down(x):
    total = 0
    while (x>=1):
        total=total+x
        x=x-1
    print(total)

sum_down(10)

# calculation function
def multi(c, d):
    return c * d

# print function
def show(y):
    print(y)

# function result
e = multi(4, 6)
show(e)

# class using
class prime:
    def secondary(self, k): # sum 1 to k
        j, sum = 0, 0
        while(j < k):
            j += 1
            if (j%2==1):
                continue
            sum += j
        return sum
    def tertiary(self, l): # avg 1 to l
        m, total, avg = 0, 0, 0
        while(m < l+1):
            total += m
            m += 1
            if(m == l):
                avg = total / l+1
        return avg

# class child using
# sum 10(a) under to k
class sub(prime):
    def another(self, k):
        a, sum = 10, 0
        while(k < a):
            a-= 1
            sum += a
            if (a == k):
                break
        return sum

g = prime()
c = sub()
q = c.secondary(10)
now = g.tertiary(10)
result = c.another(5) # 

# using print function
show(q)
show(int(now))
show(result)