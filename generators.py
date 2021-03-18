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

And notice that this can get pretty hectic. Because when we want to create a giant list with input of 100000 and then click run, we see that's a lot of memory that we're using up and once it's done, only then we can use this list and it's going to access that list in memory and then we're able to use it. But a more efficient way is to use a generator and actually generate this without taking space in memory.

"""


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)

print(my_list)

li = make_list(100000)

# print(li)


print("*******************************")


"""

A list is an iterable. But what was an iterable? An iterable is any object in Python which we're able to loop through and it actually has the dunder iter method (__iter__). So when the object is created, this __iter__ allow us to have an iterable object that can be iterated over. To iterate something or iteration is the act of taking an item from an iterable, doing something to it then going to the next one. When we use loops like for loops or while loops, we call that iteration. It's the process itself and generators are actually iterable. Well, everything that is a generator is an iterable. We can iterate over them. But not everything that is iterable is a generator. For example a range is a generator. So that is always going to be an iterable. But a list is an iterable but it's not a generator. So a generator is a subset of an iterable. So:

every Generator are Iterable.
But:
every Iterable aren't Generator.

The difference between a generator and a regular iterable is the way we implement them.

A general way to create a generator:

Let's define our own generator.

Well, generators are usually functions. Just like range that is a function, generators are usually created this way (Lines 94 to 96). Here in our function we have a for loop that is going to loop over a range for example like this (Line 95) just like we had before (Line 33). But the difference is that generator_fucntion is going to create these items (0 to num), but instead of returning like we would in a regular function (Line 35), we're going to use a keyword called yield. And here we're going to yield the i (the item). So, we instead of returning and appending this list (result in line 32) and creating all these data, we're going to use yield.

What does yield do? Well, yeild pauses the function and comes back to it when we do something to it which is called next. So yield says, hey pause the function and just yield (give) i (the item) and when you tell me to keep going again then I'll keep going. 

So how can we do this?

Well, we can do like this (Line 99). We can say for item in the generator_function and give it an input like 1000, we're going to print the item. Now here what is going to happen is we're going to loop over the generator_function and we're going to print each item. In the generator_function because this (generator_function(1000)) is an iterable, it's going to run and it's going to loop and for every item in this (range(num)), we're going to yield i. So it's going to keep looping and looping and when we come back and loop over, we're going to run this (yield i) and the yield comes back and run again.  Just run the program and you'll see what i mean. Well, what we did here is similar to this function (make_list function in Line 31). But instead of having to create that list (rsult) in memory, it just keep going one by one and we only held one item in memory and we used it however we wanted to. For example in our case all we did was print item.

Let's explore this yield keyword a little bit more. What does it actually do.

Let's say we wanted multiply this i by 2 (Line 105). But now instead of doing the for loop let's just call the function and say g equals to generator_function2(100) with the input of 100. Now if we print g like this (Line 114) and then run the program, we'll get something like this: <generator object generator_function2 at 0x000002694FB29EB0>. And actually we'll get a generator object. And remember that this is just the standard way in Python that we can create a generator function using the range and the yield keyword.

The standard way: 

def generator_function(num):
    for i in range(num):
        yield i


And this yield keyword gives us some power. Because if we just return the i here (Line 110), we're not going to get anything special (Line 118) and as a matter of fact we're just going to get a value (0 here in line 119). Instead by using the yield keyword, what we're able to do is to turn this into a generator funtion (Line 105) that can do this (line 123).

We can say next(g) (Line 123). Now if we print next(g) here (line 123), and then cick run, we get 0. If we print next(g) another time, we get 2. But now if we do next(g) three times and then print next(g) again, we get 10. Why is that? Remember the yield keyword pauses the function. So what just happened here is that we ran the function with input of 100. The first item in range(100) was 0 (for 0 in range(num) in line 104). Now here before we were even able to run this, it says, hey this is a generator function and the first time you run it give the output 0 * 2 that is 0 (yield i * 2 in line 105). If we run it agin with next(), then we have 1 * 2 that is 2. Now if we do this three times, we have 2 * 2 that is 4 (Line 127), 3 * 2 that is 6 (Line 128), 4 * 2 that is 8 (Line 129) and then 5 * 2 that is 10 (Line 130).

So yield pauses the function and then comes back to it when next is called. So if it has a yield keyword, it becomes a generator. It keeps track of this state (i * 2 in line 105) what we call the value and it only keeps the most recent data in memory, for example 10 (in here), it remebers that. Because on line 134 if we do print(next(g)), it remembers that previously this i (Line 105) was 5. So now if we print this we have 6 * 2 that is 12.

Now if we create a generator like h with input of 1 (Line 137), and then run next(h) more than once, we get this error: print(next(h)) StopIteration. We get a StopIteration. So next can be called as many times as we want, as many times until this range (Line 104) expires and when we exceed the number of items in the range, well, we get a StopIteration error to let us know that, hey you can't call next anymore, we've reached the end line. When we use for loops with ranges it actually detects it for us and then stops for loop but this is hidden away from us as users.

"""


def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(1000):
    print(item)


def generator_function2(num):
    for i in range(num):
        yield i * 2


def generator_function3(num):
    for i in range(num):
        return i * 2


g = generator_function2(100)
print(g)
# <generator object generator_function2 at 0x000002694FB29EB0>


r = generator_function3(100)
print(r)
# 0


print(next(g))
# 0
print(next(g))
# 2
next(g)
next(g)
next(g)
print(next(g))
# 10


print(next(g))
# 12

h = generator_function2(1)

print(next(h))
# 0

# print(next(h))
# print(next(h)) StopIteration.


print("*******************************")


"""

The true power of generators:

I have two functions here. The long_time funtion that uses a range and another long_time2 funtion that uses a range (A generator) and then converts it into a list. So second one creates a list and then form that list that's created in memory on our computers, it's going to go one by one and multiply thing by 5 versus first one that is a range which is a generator that comes built into Python that is going to one by one hold 0 in memory and multiply it by 5, hold 1 in memory and multiply it by 5 and keeps going, keeps going and removes from memory any old numbers.

What is the performance of this two functions?

long_time()     ->    took 12.906043529510498 s
long_time2()    ->    took 18.10884141921997 s

So the generators have better performance and is so much faster.

So with generators we're able to not hold things in memory, not have to consume all that resources and instead process data efficiently.

Generators are really really useful when calculating large sets of data. Particulary if we're using long loops where we don't really want to store that memory and we don't need to calculate everything at the same time.

"""


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result
    return wrapper


@performance
def long_time():
    print('using range:')
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print('using list:')
    for i in list(range(100000000)):
        i * 5


long_time()
long_time2()


print("*******************************")


"""

Implementing our own *for loop* and our own *range function*:

1) for loop:
All it's doing is receiving an iterable and then we're going to say iterator is going to equal an iterable. Now for us to have an iterable, we should use iter function and convert it to an iterable. This iter function is going to allow us to use next funtion on this iterable. Now we use a while loop and inside of it we use a try block. Now inside our try block, we say until everything is fine, at first print our iterator and then with the next function we'll go to our next value in our iterable that we passed to this function. And then finally we say that, we want to stop, when we have the StopIteration exception. So inside this exception we use break statement. So now if we call special_for and then give it a list, and then click run, we'll see that we loop through some iterable objects using next function. And we see that this object exists in the same memory space (Something like this: <list_iterator object at 0x00000194575BA0D0>) even though we're constantly looping through it.

So this is how for loops work. When we do this (for num in [1, 2, 3]), it's going to turn it into an iterable and it's going to keep runnig and keep calling next function on it over and over until we finish the end of line and then break out of the loop. 

We also can check the actual values of the iterator with printing our next function. We also can something like this here (Line 250) and multiply our iterator by 2. So now our special for loop, jsut multiplied our list by 2.


2) range function:

Let's create a class. And this class is going to mimic what range function does. So this class will have an init function (Line 263). And inside of it, we have first and last. In range we could say like range(2, 15) and 2 was our start and 15 was our end. So here first is our start and last is our end. Note that we use class here, because we're just creating our own data type, our own special range in Python. 

Now we can use our Dunder methods. So remember how we have the iter() to get an iterator and use next on them, well we have Dunder method that is __iter__ and this __iter__ allows us to create an iterable. 

And finally we want to be able to run next function on our gen (Line 278). So once again we can use a Dunder method which is called __next__ and this is built into Python. Now all we want to do here is to let it know how we want next to work. We need some sort of state or data to keep track of where we are. Well, we can create a class object attribute (Line 261). So we can say current equals to zero. So this is where we are currently on our iteration and now we can say if our current as long as is less than our last, we want a num to equals our current and we want to increase this current by 1, and then return num. So if our current get bigger than last, we simply going to raise a StopIteration. Because there's no more things to iterate over. 

Note that the for loop automatically catches this StopIteration, so it doesn't error out and it's stops looping. So That's how things work with range. 

"""


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


def special_for1(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


def special_for2(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


special_for([1, 2, 3])
special_for1([1, 2, 3])
special_for2([1, 2, 3])


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)


print("*******************************")


"""

Exercise Fibonacci Numbers: 


Using List And Using Generator:


"""


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


for item in fib(21):
    print(item)


print(fib2(21))


print("*******************************")
