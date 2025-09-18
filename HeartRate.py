"""

Create a Python script to track heart rate readings and calculate the average heart rate.
"""
# establishes list of times of day
time = ["breakfast","Mid Day","lunch","dinner"]
# creates a input for the user to give their heart rate too
heart_rates = []
# loop to ask for heart rate them too moving by time of day
for t in time:
    heart_rates.append(int(input("enter your heart rate at " + t + ": ")))
avg_heart_rate = sum(heart_rates) / len(heart_rates)
# loop to print all your hear rates for each time of day then gives the average
for item in range(len(heart_rates)):
    print(f"For {time[item]} your heart rate(in BPM) was {heart_rates[item]}")
print("your average heart rate (in BPM) is", avg_heart_rate)
