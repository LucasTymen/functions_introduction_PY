"""
Introduction to Functions
Parameters & Arguments

Let’s return to our trip_welcome() function one more time! Let’s modify our function to give a welcome that is a bit
more detailed.

def trip_welcome():
  print("Welcome to Tripcademy!")
  print("Looks like you're going to Times Square today.")

trip_welcome()

This will output:

Welcome to Tripcademy!
Looks like you're going to Times Square today.

Our function does a really good job of welcoming anyone who is traveling to Times Square but a really poor job if they
are going anywhere else. In order for us to make our function a bit more dynamic, we are going to use the concept of
function parameters.

Function parameters allow our function to accept data as an input value. We list the parameters a function takes as
input between the parentheses of a function ( ).

Here is a function that defines a single parameter:

def my_function(single_parameter)
  # some code

In the context of our trip_welcome() function, it would look like this:

def trip_welcome(destination):
  print("Welcome to Tripcademy!")
  print("Looks like you're going to " + destination + " today.")

In the above example, we define a single parameter called destination and apply it in our function body in the second
print statement. We are telling our function it should expect some data passed in for destination that it can apply to
any statements in the function body.

But how do we actually use this parameter? Our parameter of destination is used by passing in an argument to the
function when we call it.

trip_welcome("Times Square")

This would output:

Welcome to Tripcademy!
Looks like you're going to Times Square today.

To summarize, here is a quick breakdown of the distinction between a parameter and an argument:

    The parameter is the name defined in the parenthesis of the function and can be used in the function body.

"""

def trip_welcome(destination): #'destination' is the parameter
    print("Welcome to TripAcademy !")
    print("Looks like you're going to the" + destination + "today.") #parameters are treated like variables within function

"""
A function definition in Python

    The argument is the data that is passed in when we call the function, which is then assigned to the parameter name.
 argument as value :
"""

trip_welcome("Empire State Building") # 'Empire State Building' is the argument as values.

"""
The argument is the data that is passed in when we call the function, which is then assigned to the parameter name.
Let’s write a function with parameters and call the function with an argument to see it all in action!
Instructions
1.

We want to create a program that allows our users to generate the directions for their upcoming trip!

Create a function called generate_trip_instructions() that defines one parameter called location.

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t worry,
we will be filling in the code in the next step.
2.

generate_trip_instructions() should print out the following:

Looks like you are planning a trip to visit <location>

Where <location> will represent the location parameter.
3.

generate_trip_instructions() should also let our users know they can reach their location using public transit.

Let’s have generate_trip_instructions()also print out the following on a new line:

You can use the public subway system to get to <location>

Where <location> will represent the location parameter.
4.

Time for some greenery! Let’s see what happens when we call the function and input the argument "Central Park", a
backyard wonder in the heart of New York City.
5.

The day trip is over and we need to get back to the train station to head home. Change the argument to "Grand Central
Station" and call the function again.

What changed in the output?
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
