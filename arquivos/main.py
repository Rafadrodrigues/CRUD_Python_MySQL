#Local onde vai ser executado o código do sistema
if __name__=="__main":
    pass

#Things that i considered important to learn in python to achive intermediate level
#1.  Use the built in functions to do the things that i wanna do.
#list comprehesion
new_list = [x for x in range(50) if x % 2 == 0]

#lambda
x = lambda y: y * 2

#Collections
my_list = [1,2,34,5,56,2,22,321,31]
my_list = map(lambda x: x + 2,my_list)

#args.**kwags
def new_func(*args,**kwargs):
    print(args,kwargs)
# *args = receives uncountable amount of value 
# **Kwags = recive amount of value as a dictionary
new_func("hello", x="bye")

# Advanced class behavior
