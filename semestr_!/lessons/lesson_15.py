"""
LEGB - local Enclosed Global Built-in



"""


# name ="xumo"


# def x():
#     global name
#     name= "abbos"
    

# x()
# print(name)




# def x():

#     name= "abbos"
#     print(name)

# x()



# def foo(items):
#     items.append(42)

# a= [1,2,3,4,5,6,7,9,0]
# foo(a)
# print(a)



# def bar(items):
#     items = [1,2,4]

# b = [1,2,3,4,5]
# bar(b)
# print("b не поменялось:", b)

                                                # legb LEGB - local Enclosed Global Built-in

# global
# def parent():
#     # enclosed
#     a =5 
#     def sui():
#         # local
#         return a
#     return sui()


# print(parent())



def outer():
    #enclosed
    x ="local"
   
    def inner():
        # local
        nonlocal x
        x ="non local"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
