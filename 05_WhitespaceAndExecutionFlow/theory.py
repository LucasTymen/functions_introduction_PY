"""
Introduction to Functions
Whitespace & Execution Flow

Consider our welcome function for our trip planning application:
"""

def trip_welcome():
  print("Welcome to Tripcademy!")
  print("Let's get you to your destination.")

"""
The print statements all run together when trip_welcome() is called. This is because they have the same base level of indentation (2 spaces).

In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function.

If we wanted to write another statement outside of trip_welcome(), we would have to unindent the new line:
"""

def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!")
  print("Let's get you to your destination.")

# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")

trip_welcome()

"""
Our trip_welcome() function steps will not print Woah, look at the weather outside! Don't walk, take the train! on our function call. The print() statement was unindented to show it was not a part of the function body but rather a separate statement.

We would see the following output from this program:

Woah, look at the weather outside! Don't walk, take the train!
Welcome to Tripcademy!
Let's get you to your destination.

Lastly, note that the execution of a program always begins on the first line. The code is then executed one line at a time from top to bottom. This is known as execution flow and is the order a program in python executes code.

Woah, look at the weather outside! Don't walk, take the train! was printed before the print() statements from the function trip_welcome().

Even though our function was defined before our lone print() statement, we didn’t call our function until after.

Let’s play around with indentation and the flow of execution!
Instructions
1.

We are going to help our trip planner users figure out if they should travel today based on the weather. Let’s let our users know we can check the weather for them.

Write a print() statement that will output Checking the weather for you!.

To print() a string use the following syntax and replace <Your string in here> with the string you want to output:

print("<Your string in here>")

You can copy and paste the string from the checkpoint instructions to make sure there are no typos.
2.

We took a look outside and see a bright sunny day. Write a function called weather_check() that will print a message to our users that it’s a great day to travel! The function should output:

Looks great outside! Enjoy your trip.

Note: Don’t call your function just yet! We will do that in the next step.

Remember to use def before weather_check(): to define the function and to indent the print statement to show that it is part of the function.
3.

Oh no! It looks like some clouds came in and it started raining. Our users shouldn’t go on a trip in the rain. In our weather_check() function add a second print() statement under the first one which prints a warning message for our travelers! It should print:

False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.

Make sure to add another print() statement inside of your function under the first print() statement at the same level of indentation.
4.

Call the function weather_check().

Be sure to add weather_check() at the bottom of your code without any indentation.
5.

Unindent your final print statement in your weather_check() function. Run the program again.

What is different?

Remember to unindent the front of the second print statement in your weather_check() function. You should notice a different order in your output terminal due to the change in the indentation.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
