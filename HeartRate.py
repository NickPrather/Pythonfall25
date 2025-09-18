"""

Create a Python script to track heart rate readings and calculate the average heart rate.
"""
time = ["breakfast","Mid Day","lunch","dinner"]
heart_rates = []
for t in time:
    heart_rates.append(int(input("enter your heart rate at " + t + ": ")))
avg_heart_rate = sum(heart_rates) / len(heart_rates)
for item in range(len(heart_rates)):
    print(f"For {time[item]} your heart rate(in BPM) was {heart_rates[item]}")
print("your average heart rate (in BPM) is", avg_heart_rate)
