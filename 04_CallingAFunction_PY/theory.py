"""
Introduction to Functions
Calling a Function

Now that we’ve practiced defining a function, let’s learn about calling a function to execute the code within its body.

The process of executing the code inside the body of a function is known as calling it (This is also known as “executing a function”). To call a function in Python, type out its name followed by parentheses ( ).

Let’s revisit our directions_to_timesSq() function :
"""

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")

"""
To call our function, we must type out the function’s name followed by a pair of parentheses and no indentation:
"""
directions_to_timesSq()
"""
Calling the function will execute the print statements within the body (from the top statement to the bottom statement) and result in the following output:

Walk 4 mins to 34th St Herald Square train station.
Take the Northbound N, Q, R, or W train 1 stop.
Get off the Times Square 42nd Street stop.

Note that you can only call a function after it has been defined in your code.

Now it’s your turn to call a function!
Instructions
1.

Call the directions_to_timesSq() function.

Click Run to see it execute and print out.

Make sure you call the function directions_to_timesSq() outside of the function definition. It should not be indented at all.
2.

Add an additional print statement to our directions_to_timesSq() function.

Have the statement print "Take lots of pictures!"

Run your code again and see how your output changes.

Remember to add the print statement inside of the function definition for directions_to_timesSq(). It should be indented and contain the text "Take lots of pictures!". Make sure to place it after the other print statements in the function.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
