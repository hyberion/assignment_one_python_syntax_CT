#Task 1 - Code correction - below is a piece of Python code with incorrect indentation.  Correct it

weather = "sunny"
if weather == "sunny":
    print("Wear Sunglasses!")
else:
    print("Take an umbrella!")

#TasTask 2 - Your mood today.  Ask the user how they feel today.  If they say happy print "That's greatot hear!", and ift hey say sad print "I hope your day gets better!
# Ensure your if statment is properly indented.
# 
print("************************************************************************************************")
print("The amazing Mood detector from Ronco!  If you aren't sure if it's worth anything, it's a Ronco!")
print("************************************************************************************************")
mood= input("What is your mood today? ")
#convert input to lower case for consistency
mood = mood.lower()

#response based in input.
if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I hope your day gets better!")
else:
    print("thats a unique mood! Tell me more about it using small words and mime!")
