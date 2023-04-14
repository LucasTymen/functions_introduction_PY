"""
Introduction to Functions
Review

Excellent work! 👏 In this lesson, you’ve covered a major fundamental programming concept used in the majority of all programs to organize code into reusable blocks. To recap, we explored:

    What problems arise in our programs without functions
    What functions are and how to write them
    How whitespace plays an important role in how a program will execute our code and more importantly distinguish function code from non-function code
    How to pass input values into our functions using parameters and arguments
    The difference between built-in and user-defined functions and some common built-in functions python offers
    How we can reuse function output with the return keyword, as well as multiple returns.
    Where variables can be accessed in our programs that use functions

Let’s practice putting all these concepts together!
Instructions
1.

Alright, this is it. We are going to use all of our knowledge of functions to build out TripPlanner V1.0.

First, like in our previous exercises, we want to make sure to welcome our users to the application.

Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this:

Welcome to tripplanner v1.0 <Name Here>

Where <Name Here> represents the parameter variable of name we defined.

Call trip_planner_welcome(), passing your name as an argument.

Let’s remember what a function declaration looks like with one parameter:
"""
def function_name(single_parameter):
  # Some Code


    """
2.

Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user’s trip.

An example call for this function will look like this:

estimated_time_rounded(2.5)

Where 2 represents 2 hours and .5 represents 30 minutes.

Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:

    Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
    Return rounded_time.

After the function definition, call estimated_time_rounded() with a decimal argument and save the result to a variable called estimate. Since this amount represents a time, be sure to use a positive number.

Here is how you would use the round() function and return it from a user-defined function:
"""

def return_round():
  rounded_value = round(5.53)
  return rounded_value

"""
3.

Next, we are going to generate messages for a user’s planned trip.

Create a function called destination_setup() that will have four parameters in this exact order:

    origin
    destination
    estimated_time
    mode_of_transport

Give the parameter mode_of_transport a default value of "Car". The program will error out if we run it since we have not defined a function body yet. Don’t worry we will do that in the next step.

Here is an example of a four-parameter function definition with a default value for the last parameter:

def four_params(param1, param2, param3, param4="Default Value"):
  # Some code

4.

Next, we are going to write four print() statements in our function. The output on this function call should look like this:

Your trip starts off in <origin>
And you are traveling to <destination>
You will be traveling by <mode_of_transport>
It will take approximately <estimated_time> hours

Each of these print() statements use a different parameter from our function destination_setup().

Note: The estimated_time parameter will come in the form of an integer. Make sure to use str() to convert the parameter in your print statement.

After the function definition, call destination_setup() with the following arguments:

    origin and destination should be string values representing the places you will travel from and to
    Use the estimate you created earlier for estimated_time
    If you will be traveling by a mode other than Car, be sure to overwrite the default value of mode_of_transport

Use + to concatenate a string variable with another string. For example:
"""
world = "World"

hello_world = "Hello" + world
print(hello_world)
"""
Would output:

Hello World

Since we know estimated_time will be a number, we will need to use the str() function to convert it to a string. Here is an example:

number = 101
print("You are taking a " + str(101) + " course"

Would output:

You are taking a 101 course

Make sure to double-check your spelling, punctuation, and capitalization. If you are still having issues, use the string provided in the exercise.
5.

Great job! 👏

We have successfully finished our first version of the trip builder application. Go ahead and try passing different values into your functions!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.

"""
