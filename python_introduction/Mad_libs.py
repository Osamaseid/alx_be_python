print("Let's play a Mad Libs game!")

# Prompt the user for different words
day_adjective = input("Enter an adjective to describe the day: ")
monkey_adjective = input("Enter an adjective to describe the monkey: ")
lion_adjective1 = input("Enter an adjective to describe the lion: ")
lion_adjective2 = input("Enter another adjective to describe the experience: ")

# Build the story
story = f"On a {day_adjective} day, I went to the zoo. I saw a {monkey_adjective} monkey swinging from the trees. Then, I spotted a {lion_adjective1} lion lounging in the sun. What a {lion_adjective2} experience!"

# Conditional touches
if day_adjective.lower() == "beautiful":
    story += " The weather was simply stunning."
elif day_adjective.lower() == "ugly":
    story += " The weather was quite dismal."

if monkey_adjective.lower() == "funny":
    story += " It was hilarious to watch the monkey's antics."
elif monkey_adjective.lower() == "boring":
    story += " I quickly grew tired of watching the monkey."

if lion_adjective1.lower() == "majestic":
    story += " The lion's presence commanded respect."
elif lion_adjective1.lower() == "lazy":
    story += " The lion seemed quite lazy and uninterested in its surroundings."

if lion_adjective2.lower() == "wild":
    story += " It was a thrilling and exhilarating experience."
elif lion_adjective2.lower() == "tame":
    story += " The experience felt a bit underwhelming."

# Display the final story
print("\nHere's your Mad Libs story:")
print(story)
      