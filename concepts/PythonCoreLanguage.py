# Drill 3
#
# Create dictionary from two lists.
#
# keys = ["name","age","city"]
# values = ["Manoj",23,"Denton"]
#
# Output
#
# {'name':'Manoj','age':23,'city':'Denton'}
#
# Use zip.


# keys = ["name","age","city"]
# values = ["Manoj",23,"Denton"]
#
# dic={}
# for k,v in zip(keys,values):
#     dic[k]=v
#
# print(dic)


# nums = [2,4,6]
# compr=[n*n for n in nums]
# print(compr)


# nums = [1,2,3,4,5,6]
# compr=[n for n in nums if n%2!=0]
# print(compr)


# words = ["python","ai","code"]
# compr=[len(n) for n in words]
# print(compr)

# nums = [3,-1,5,-2,7]
# compr=[0 if n<0 else n for n in nums]
# print(compr)


# //////////////////
# lambda
# square= lambda x:x*x
# print(square(5))

# words = ["apple","kiwi","banana"]
#
# words.sort(key=lambda x:len(x))
# print(words)

# drill-3
# cube= lambda x:x*x*x
# print(cube(3))

# nums = [1,2,3,4]
# num= list(map(lambda x:x+x,nums))
# print(num)

# nums = [5,12,7,18,3]
# num= list(filter(lambda x:x>10,nums))
# print(num)

# *args and **kwargs

# def multiply(*nums):
#     mul=1
#     for i in nums:
#         mul*=i
#     return mul
# print(multiply(2,3,4))

#

# def student(**info):
#     print(info)
#
# student(name="Manoj", age=23, city="Denton")


# Generator
# def generate_squares(n):
#     for i in range(1, n+1):
#         yield i*i
# for num in generate_squares(5):
#     print(num)
# print(list(generate_squares(5)))

def generate_cubes(n):
    for i in range(1, n+1):
        yield i**3
print(list(generate_cubes(4)))