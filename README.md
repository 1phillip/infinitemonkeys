# Infinite Monkeys
This program attempts to simulates the "infinite monkey theorem."
From Wikipedia: The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare.

This program will repeatedly generate a random string of characters (length specified by user) and search for that string of characters within a passage. In this case, the passage is Shakespeare's Hamlet. The program first creates a pool of every possible character (letters, numbers, punctuation marks, etc.) in the passage. Then the program draws from this pool of possible characters to generate the random string. As a result, the passage can be changed to any language. Note that there is no mechanism in place to prevent the same string from being generated multiple times.

The program keeps count of how many attempts it has made to generate a random string that matches with text in the given passage. Once it finds one, it will output how many attempts it took in addition to a short excerpt from the passage where the random string was found.
