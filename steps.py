"""

Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.
"""
# creates a list of all days in a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = [] # initializes a list to store steps taken each day
for day in days: # loop to go through and collect steps for each day
    steps.append(int(input(f"How many steps did you take on {day}? ")))
    total_steps = sum(steps)
# displays the total and average steps taken in the week
print("you took a total of", total_steps, "steps this week")
average_steps = total_steps / len(steps)
print("your average steps per day is", average_steps)
