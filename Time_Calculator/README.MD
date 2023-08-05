# Time Calculator

This is the boilerplate for the Time Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

Steps:
1. Parse the input start time, duration, and optional starting day of the week.
2. Extract the hour, minute, and AM/PM from the start time and convert the start time to 24-hour format.
3. Extract the hour and minute from the duration time.
4. Add the start time hour and duration hour, and the start time minute and duration minute separately to get the total hour and minute.
5. Calculate the number of days the result will be later by dividing the total hour by 24.
6. Calculate the remaining hours by taking the modulo of the total hour with 24.
7. Determine the new AM/PM based on the remaining hours.
8. Convert the remaining hours to 12-hour format.
9. Construct the new time string using the 12-hour format, minutes, and the new AM/PM.
10. If there's a starting day of the week provided, find the new day of the week based on the number of days later.
11. Append the new day of the week to the result string if applicable.
12. Append the "next day" or "(n days later)" message based on the number of days later to the result string if applicable.
13. Return the final result string.