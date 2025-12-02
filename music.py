import sys
import time 

def print_lyrics():
    lyrics = [
       "Don't wanna close my eyes",
        "Don't wanna fall asleep",
        "'Cause I'd miss you babe",
        "And I don't wanna miss a thing",
        "'Cause even when I dream of you",
        "The sweetest dream would never do",
        "I'd still miss you babe",
        "And I don't wanna miss a thing"
    ]

    # Adjusted delays focusing on the rhythm of the original eight lines:
    # A bit shorter for the quick phrases, longer for the dramatic finishes.
    delays = [
        0.5, # Don't wanna close my eyes
        0.6, # Don't wanna fall asleep
        0.4, # 'Cause I'd miss you baby
        1.0, # And I don't wanna miss a thing 
        0.5, # 'Cause even when I dream of you
        0.7, # The sweetest dream would never do
        0.5, # I'd still miss you baby
        1.5  # And I don't wanna miss a thing 
    ]

    print(" \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08) # Slightly faster character printing
        print()
        time.sleep(delays[i])

# Call the function
print_lyrics()