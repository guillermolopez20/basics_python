# functiones
def addnumeros(numero1, numero2):
    sum = numero1 + numero2
    print('Sum: ',sum)
#----------------------------
def find_square(num):
    result = num * num
    return result
    print(result)
#---------------------------
def multiply_numbers((num1, num2):
    product = num1 * num2
    return product
result = multiply_numbers(3, 4)
print(result)
# Default Parameters
def student(firstname, lastname ='Memo', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')
#---------------------
def greet(name='guillermo', message='Hi'):
    return f"{message} {name}"
greeting = greet()
print(greeting)
#------------------------
#Keyword Arguments
def hello_world_arbitrary_keyword_args(**kwargs):
    print(kwargs)
#-----------------------
 def f(**kwargs):
        return kwargs
    
    f(a=1, b=True, h=50, z="Hello, world!")
    {'a': 1, 'h': 50, 'b': True, 'z': 'Hello, world!'}
    #------------------------
    def f(message="Hello", name=None):
    print("{0}, {1}!".format(message, name))
    
    kwargs = {"message": "Hola", "name": "mundo"}
    f(**kwargs)
    Hola, mundo!
    #Recursive Functions
    def Recur_facto(n):
   
    if (n == 0):
        return 1
   
    return n * Recur_facto(n-1)
   
# print the resultado
print(Recur_facto(6))
#----------------------------
def fact(n):
  """ Function to find factorial """
  if n == 1:
    return 1
  else:
    return (n * fact(n-1))

print ("3! = ",fact(3))
#Lambda Expressions
potencia = lambda x: x ** 2
print(potencia(3)) 
#---------------------
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
#Function Docstrings
def my_add(x,y):
    '''Takes two inputs and returns the sum'''
    return x+y
print(my_add(5,7)) #12 
print(my_add.__doc__)
#-------------------------------------
def add_binary(a, b):
    """
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    """
    binary_sum = bin(a+b)[2:]
    return binary_sum


print(add_binary.__doc__)
#--------------------------

