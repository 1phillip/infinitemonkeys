# Infinite Monkeys
This program attempts to simulates the "infinite monkey theorem."
From Wikipedia: The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare.

This program will repeatedly generate a random string of characters (length specified by user) and search for that string of characters within a passage. In this case, the passage is Shakespeare's Hamlet. The program first creates a pool of every possible character (letters, numbers, punctuation marks, etc.) in the passage. Then the program draws from this pool of possible characters to generate the random string. As a result, the passage can be changed to any language. Note that there is no mechanism in place to prevent the same string from being generated multiple times.

The program keeps count of how many attempts it has made to generate a random string that matches with text in the given passage. Once it finds one, it will output how many attempts it took in addition to a short excerpt from the passage where the random string was found.

EXAMPLE:

Length of randomly generated search query: 3
Attempt 1: faP
Attempt 2: wLK
Attempt 3: upx
Attempt 4: Dvn
Attempt 5: WLl
Attempt 6: cVb
Attempt 7: ctd
Attempt 8: T;?
Attempt 9: Fc!
Attempt 10: KaI
Attempt 11: PrQ
Attempt 12: OHA
Attempt 13: ZSK
Attempt 14: F-&
Attempt 15: wB 
Attempt 16: QMk
Attempt 17: gll
Attempt 18: taA
Attempt 19: y'C
Attempt 20: O?T
Attempt 21: sFF
Attempt 22: yOK
Attempt 23: Lce
Attempt 24: .Ez
Attempt 25: yzO
Attempt 26: aen
Attempt 27: :hB
Attempt 28: nKu
Attempt 29: aya
Attempt 30: Dxy
Attempt 31: !&z
Attempt 32: ]VA
Attempt 33: Z:i
Attempt 34: T ;
Attempt 35: SSe
Attempt 36: mLZ
Attempt 37: om 

The string "om " was found on attempt 38 in the following location:

...Bernardo speak of this.

BERNARDO

    Last night of all,
    When yond same star that's westward from the pole
    Had made his course to illume that part of heaven
    Where now it burns, Marcellus ...
