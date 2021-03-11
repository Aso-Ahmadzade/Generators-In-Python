from time import time


# Generators


"""

Generators are a sequence of values over time.

For example range() is a generator. A generator is a special type of thing in Python that allows us to use a special keyword called yield. And yeild can pause and resume functions.

When we use range versus something like list. For exmple like bottom:

range(100)
list(range(100))

We convert our range to a list. And a list what it does is actually create a giant list of 100 (In our example) item in memory versus a range that creates them one by one. 

We create a function (make_list) and when we make a list like we just did here (Line 16), we're essentially doing this (make_list function in Line 31). We're using range to create a list and return result which will live in memory.

Now if we make a list with input of 100, and then print that list, we get our list and this list lives in our memory. my_list is pointing to a location in memory. So this is taking up space.

But range is a generator and a generator is a little bit different, because this is not being held in memory. When we do this for loop (Line 33), this range doesn't create on its own a giant list of 0 to 99. And then is it starts iterating? No. It says, with the for loop as a range, I'm going to give you first the number 0 (for i in 0), then I'm going to give you the number 1 (for i in 1), and then 2 and so on all the way to a hundred. So in memory it never ever creates this list (my_list) like we had with make_lsit function.

And notice that this can get pretty hectic. Because when we want to create a giant list with input of 1000000 and then click run, we see that's a lot of memory that we're using up and once it's done, only then we can use this list and it's going to access that list in memory and then we're able to use it. But a more efficient way is to use a generator and actually generate this without taking space in memory. 

"""


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)

print(my_list)

li = make_list(1000000)

print(li)


print("*******************************")


def fib(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


def fib2(number):
    a, b = 0, 1
    li = []
    for i in range(number):
        li.append(a)
        temp = a
        a = b
        b = temp + b
    return li


# for item in fib(21):
#     print(item)


# print(fib2(21))
