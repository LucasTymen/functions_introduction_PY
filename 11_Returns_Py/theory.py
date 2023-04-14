"""

Skip to Content
My Home
Introduction to Functions: Returns
Learn
Introduction to Functions
Returns

At this point, our functions have been using print() to help us visualize the output in our interpreter. Functions can
also return a value to the program so that this value can be modified or used later. We use the Python keyword return to
do this.

Here’s an example of a program that will return a converted currency for a given location a user may want to visit in
our trip planner application.
"""

def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

"""
This would output:

100 dollars in US currency would give you 140 New Zealand dollars

Saving our values returned from a function like we did with new_zealand_exchange allows us to reuse the value (in the
form of a variable) throughout the rest of the program.

When there is a result from a function that is stored in a variable, it is called a returned function value.

Let’s try to return some data in the exercises!

Note: Working with multiple functions can be a bit overwhelming at first. Don’t hesitate to use hints or even look at
the solution code if you get stuck.
Instructions
1.

Our travel application is getting really popular. Some of our users have posted on social media that it would be useful
if our application could help them track their budget during trips. We want to help them track their starting budget and
let them know how much they have left after an expense.

We have provided some starting code to get started. Take a second to understand the code and then click Run and take a
look at the output.
2.

Let’s create a new function called deduct_expense() that will take two parameters.

The first parameter will be budget and the second parameter will be expense. Our function will be taking in a budget
value as well as the expense we want to subtract.

We will want our function to return the budget minus the expense our travelers are incurring.

Remember to use the keyword return followed by the subtraction of expense from budget.
3.

Looks like the most common expense our travelers are incurring is a t-shirt purchase.

Let’s create a variable called shirt_expense and for now, we will give it a set value of 9 (We are not accounting for
currency changes at the moment). Make sure this is defined outside of the functions in your script.

Define shirt_expense outside of all of the functions in your script and set it equal to 9.
4.

Now that we have an expense to subtract, create a new variable called new_budget_after_shirt and set it to be the
function call of deduct_expense().

Pass our current_budget variable as the first argument and the shirt_expense variable as the second argument.

Here is an example of calling a function with two arguments:

my_function(argument1, argument2)

5.

Lastly, we want our users to see the remaining budget.

Call the provided print_remaining_budget() function, passing in new_budget_after_shirt as the only argument.

Make sure to call print_remaining_budget() outside of the function definitions and with new_budget_after_shirt as the
argument.
6.

Great Job! This is the biggest program with functions we have built so far! Take a second to review your code and click
Run one last time when you are ready to move on.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
1
2
3
4
5
6
7
8
9
10
Output:



11/13
Well done! You've just met your weekly target.

"""
