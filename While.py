"""

Write the program "99 Bottles of Beer on the Wall" using a while loop.
 Be mindful to change the word 'bottles' to 'bottle' when down to the 
last one. You must do the full 99 bottles; the sample shows the last 3 verses.
"""
# defines the number of bottles at the start
bottles = 99
# while loop to count down the number of bottles
while bottles > 1:
    print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
    # starts the subtraction of bottles and when bottles hit 1 it changes to bottle
    print(f"Take one down, pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n")
    bottles = bottles - 1
# prints no more bottles of beer when the loop is over
print("No more bottles of beer on the wall.")
