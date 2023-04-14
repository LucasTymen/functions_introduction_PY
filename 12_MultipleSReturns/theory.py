"""
Introduction to Functions
Multiple Returns

Sometimes we may want to return more than one value from a function. We can return several values by separating them
with a comma. Take a look at this example of a function that allows users in our travel application to check the
upcoming week’s weather (starting on Monday):
"""

weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

"""
This function takes in a set of data in the form of a list for the upcoming week’s weather. We can get our returned
function values by assigning them to variables when we call the function:
"""

monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)

"""
This will print:

Tomorrow the weather will be Sunny
The following day it will be Sunny
Two days from now it will be Cloudy

Let’s practice using multiple returns by returning to our previous code example.
Instructions
1.

Our users liked the previous functionality that we added to our travel application, but recently we have had an influx of users planning trips in Italy. We want to create a small function to output the top places to visit in Italy. Another member of our team already started on the implementation of this feature but it is still missing a few key details.

Take a second to review the code and click Run when you are ready to move on. For now, there will be no output.
2.

We want to be able to return the three most popular destinations from our function top_tourist_locations_italy().

Add a line in the function top_tourist_locations_italy() that will return the values of first, second, third in that exact order.

A function that returns multiple values would like like this:

my_function():
  a = 1
  b = 2
  c = 3
  return a, b, c

3.

In order to use our three returned values from top_tourist_locations_italy() we need to assign them to new variables names after we call our function.

Set the return of the function top_tourist_locations_italy() to be equal to three new variables called most_popular1, most_popular2, and most_popular3 in that exact order.

To set multiple return value variables from a function, declare them with commas in between and set them to the function call. For example:

return1, return2, return3 = multi_return()

4.

Use three print() statements to output the value of most_popular1, most_popular2, and most_popular3.

Your output should be:

Rome
Venice
Florence

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
