"""
Introduction to Functions
Types of Arguments

In Python, there are 3 different types of arguments we can give a function.

    Positional arguments: arguments that can be called by their position in the function definition.

    Keyword arguments: arguments that can be called by their name.

    Default arguments: arguments that are given default values.

Positional Arguments are arguments we have already been using! Their assignments depend on their positions in the
function call. Let’s look at a function called calculate_taxi_price() that allows our users to see how much a taxi would
cost to their destination 🚕.
"""

def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

"""
In this function, miles_to_travel is positioned as the first parameter, rate is positioned as the second parameter, and
discount is the third. When we call our function, the position of the arguments will be mapped to the positions defined
in the function declaration.

# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)

Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the
function call. Notice in the code example below that the arguments do not follow the same order as defined in the
function declaration.

calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

Lastly, sometimes we want to give our function arguments default values. We can provide a default value to an argument
by using the assignment operator (=). This will happen in the function declaration rather than the function call.

Here is an example where the discount argument in our calculate_taxi_price function will always have a default value
of 10:
"""

def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

"""
When using a default argument, we can either choose to call the function without providing a value for a discount (and
thus our function will use the default value assigned) or overwrite the default argument by providing our own:

# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)

Let’s practice using these different types of arguments!
Instructions
1.

Tripcademy (our trusty travel app) needs to allow passengers to plan a trip (duh).

Write a function called trip_planner() that will have three parameters: first_destination, second_destination and
final_destination.

Give the final_destination parameter a default value of "Codecademy HQ".

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t
worry, we will be filling in the code in the next step.

Remember the structure of a multi-parameter function:
"""

def my_function(param1, param2, param3):
  # Some code..

    """
2.

First, we want to introduce the trip to users. Use print() in our function to output Here is what your trip will look
like!.

Make sure to add the print() statement inside of your function by indenting it. Check spelling and capitalization for
your string so it matches the one provided in the instructions.
3.

In our function definition let’s provide an itinerary that will describe the destinations our user will visit in order.
Print a statement that follows this form:

First, we will stop in <first_destination>, then <second_destination>, and lastly <final_destination>

An example call to our function using positional arguments:


trip_planner("London", "India", "New Zealand")


Should output:

Here is what your trip will look like!
First, we will stop in London, then India, and lastly New Zealand

To test out your function, call trip_planner() with the following values for the parameters:

    first_destination: "France"

    second_destination: "Germany"

    final_destination: "Denmark"

Use + to concatenate strings together. Here is an example:
"""

learning = "I am learning "
py_funcs = "Functions"

print(learning + py_funcs)

"""
Would output:

I am learning Functions

Note: We can add an extra space at the end of learning to make sure the string is properly formatted when it is combined.

Your output should be:

Here is what your trip will look like!
First, we will stop in France, then Germany, and lastly Denmark

4.

Call the function trip_planner() again with the following values for the parameters:

    first_destination: "Denmark"

    second_destination: "France"

    final_destination: "Germany"

Note the difference in your output depending on the position of your arguments.

Your output should be:

Here is what your trip will look like!
First, we will stop in Denmark, then France, and lastly Germany

5.

Call the function trip_planner() again using keyword arguments in this exact order:

    first_destination: "Iceland"

    final_destination: "Germany"

    second_destination: "India"

Make sure to enter the arguments in the order specified.

Remember, that when using keyword arguments, we explicitly refer to the assignment of each argument in the function call.
Here is an example:

trip_planner(first_destination = "Disney World", final_destination = "Legoland", second_destination = "Sea World")

6.

Lastly, go ahead and call the function trip_planner() using only two positional arguments to see the default argument in
action:

    first_destination: "Brooklyn"

    second_destination: "Queens"

Your output should be:

Here is what your trip will look like!
First, we will stop in Brooklyn, then Queens, and lastly Codecademy HQ

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
