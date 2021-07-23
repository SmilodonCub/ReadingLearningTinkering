#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:22:07 2021

@author: bonzilla
"""


class Customer:
    # code for the class goes here
    def identify( self ):
        print( "I am Customer " + self.name )
    
    def set_name( self, new_name):
        #create an attribute by assigbning a value
        self.name = new_name


# %%
c1 = Customer()
c1.set_name( "Laura" )
c1.identify( ) #will be interpreted by python as Customer.identify( c1, "Laura")

# classes are templates, how to refer to data of a particular object?
# self is a stand-in for a particular object used in a class definition
# self should be the first argument of any method so that we can use it to call to attributes and methods within the class definition

# %%

class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary( self ):
        return self.salary/12
    
# %%
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)
mon_sal = emp.monthly_salary()
print( mon_sal )

# %%

#Methods are function definitions within a class
#Attributes are defined by assignment within the class
#both methods and attributes refer to the self

#Constructor: add data to an object when creating it
#defining attribute in the constructor is better practice because it is:
#   1) easier to know all the attributes
#   2) attributes get created when the object is created
#   3) more usable and maintainable code

#Conventions:
#   1) CamelCase for class names
#   2) lower_snake_case for functions and attributes
#   3) use 'self' as 'self' (python won't stop you otherwise, but it's best practice to stick with convention)
#   4) Use docstrings

# %%

class Customer:
    #constructor that will be called whenever a class instance is instantiated
    def __init__( self, name ):
        self.name = name
        print( "the __init__ method was called" )
        
        
# %%
cust = Customer( "Lara de Silva" )
print( cust.name )        
        

# %%
class Employee:
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary > 0:
            self.salary = salary 
        else:
            self.salary = 0
            print( "Invalid salary!" )

   
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

# %%
import math
# Write the class Point as outlined in the instructions
class Point:
    def __init__( self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    def distance_to_origin( self ):
        return math.sqrt( self.x**2 + self.y**2 )
    def reflect( self, axis ):
        if axis == 'x':
            self.y = -self.y
        elif axis == 'y':
            self.x = -self.x
        else:
            print( "Invalid axis" )
            
# %%
# Class level data. like making global values available to all class instances
# Class Attributes: for global constant related to class (eg: min/max values. common vals: like pi etc.)
class Employee:
    
    MIN_SALARY = 30000
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= Employee.MIN_SALARY:
            self.salary = salary 
        else:
            self.salary = Employee.MIN_SALARY
            
emp1 = Employee( "TBD", 40000 )
print( emp1.MIN_SALARY )

# %% Class Methods. similar in scope as Class Attributes: cannot access any instance level data       
class Employee:  
    MIN_SALARY = 30000
    
    @classmethod
    def from_file( cls, filename ):
        with open( filename, 'r' ) as f:
            name = f.readline()
        return cls( name )
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= Employee.MIN_SALARY:
            self.salary = salary 
        else:
            self.salary = Employee.MIN_SALARY
            
            
# %%
class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move( self, steps ):
        if self.position + steps < Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION
      
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()

# %%
class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        #parts = datestr.split("-")
        #year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        year, month, day =  map(int, datestr.split("-"))
        # Return the class instance
        return cls(year, month, day)     
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, datetime):
      year, month, day = datetime.year, datetime.month, datetime.day
      return cls( year, month, day)


# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)

# %%
#Class Inheritance
# new class functionality = old class functionality + something extra

# implementing class inheritance

# class MyChild( MyParent ):
#    #do something here
# 1) MyParent: old class
# 2) MyChild: new class

# Inhertance "is-a" relationship: A MyChild is a MyParent

class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  def display( self ):
    print( "Manager " + self.name )


mng = Manager( "Debbie Lashko", 86500 )
print( mng.name )
mng.display()

# %%

class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

# %%
Customizing a Dataframe

# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF( pd.DataFrame ):
    def __init__( self, *args, **kwargs ):
        pd.DataFrame.__init__( self, *args, **kwargs )
        self.created_at = datetime.today()
    def to_csv(self, *args, **kwargs):
        # Copy self to a temporary DataFrame
        temp = self.copy() 
        # Create a new column filled with self.created_at
        temp["created_at"] = self.created_at    
        # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
        pd.DataFrame.to_csv( temp, *args, **kwargs )
    
    
ldf = LoggedDF({"col1": [1,2], "col2": [3,4]})
print(ldf.values)
print(ldf.created_at)

# %% Making objects integrate with standard python operations

# Overloading

# __eq__() is called when 2 objects of a class are compared using ==
# and other operators: __ge__() __lt__()  etc.
# __hash__() to use objects as dictionary keys and in sets

class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__( self ):
        emstr = """Employee name: {}, 
        Employee salary: {}.""".format(self.name, self.salary)
        return emstr

    # Add the __repr__method  
    def __repr__(self):
        emrep = """Employee(\"{name}\",{salary})""".format( name = self.name, salary = self.salary ) 
        return emrep 

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)


# %% Exception handling: try - except - finally 
# prevent the program from terminating when an exceptio is raised

# try - try this code first
# except - if this error occurs, execute the following
# finally - if all else failed, try this

# raising exceptions

# custom exceptions - allow for more granular handling of errors

def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print( 'Cannot divide by zero!' )
    except IndexError:
        print( 'Index out of range!' )
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))

# %%
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
       raise BonusError( 'The bonus amount is too high!') 
        
    elif self.salary + amount <  Employee.MIN_SALARY:
       raise SalaryError("The salary after bonus is too low!")
      
    else:  
      self.salary += amount
      
# It's better to list the except blocks in the increasing order of specificity, 
#i.e. children before parents, otherwise the child exception will be called 
#in the parent except block.
      
# %%
# Polymorphism - using a unified interface to operate on objects of different classes
      
# Liskov substitution principle - base class should be interchangeable with any of its 
# subclasses without altering any properties of the program (Barabara Liskov)
# This should be the case both syntactically & semantically:
      # Syntactically - function signitures are comparable (arguments/return values)
      # Semantically - the state of the object and the program remain consistnet
