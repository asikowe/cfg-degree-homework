# --------------
#   QUESTION 1
# --------------
"""
COMPLEXITY ANALYSIS: 

CODE SAMPLE 1
Hashing based approach: 
Hashing allows to search for elements in O(1) (constant) time. As we iterate over the array just once,
and return the matching pair immediately after it is found,  in the worse case scenario (for example
if the matching number will be at the end of the array), the time complexity will be O(n) (linear,
growing linearly and in direct proportion to the size of the input data set). 
We don't store any results, so the space complexity will be O(1) (constant, won't change even if
the input size changes).

CODE SAMPLE 2
Graph data structure:
Insertion and deletion of the elements of the stack runs in O(1) time complexity. However, we will
have to traverse all vertices via their edges at least once (sometimes more times, if we have to backtrack),
so the time complexity for this one will be O(verices+edges). 
All the nodes will be stored in a collection, therfore space complexity for this will be O(n), 
growing in linear proportion to the size of the input.

CODE SAMPLE 3:
Palindrome:
To be able to find if a word is a palindrome, the pointers have to meet in the middle, so they have
to traverse the whole string. Therefore, the Big O notation, in the worse case scenario, will be
O(n) - linear. We don't store any results, only return boolean for the found/not found palindrome,
so space complexity will be O(1).

CODE SAMPLE 4:
Binary Search:
For searching in binary tree, because of halving the result each time, the time complexity is O(log n) 
(logarithmic time complexity). That means that as the input size grows, the number of operations grows 
very slowly. We don't store any results, we just return an integer of an index or -1 that denotes 
the element was not found, so the space complexity will be O(1).


"""
# --------------
#   QUESTION 4
# --------------
"""
My app will be a phone-based application that will allow people to discover music from all over the
world, from different time periods and many genres. 

It will use gradient backgroud, delicate greens and pastel yellows - greens for the portrayal of hope of 
finding something new and exciting, yellow for the fun of discovery.

PERSONAS:
Lucy: loves going to small, quirky festivals around the world with no knowledge of the bands that are
playing. This approach made her find some great gems and experience strong emotional reactions to the
music. She would like to recreate that feeling on a smaller scale at home.

George: absolutely bored with the Spotify algorithm that serves him music he finds appealing, but never
exciting. He would like to branch out more to widen his musical horizons.

Kath-O: a DJ that everyone loves, beause of their unique and eclectic music taste. They love browsing
through all sorts of retro music shops in search of the perfect vinyl, but they recently started to
browse through the Internet in search of music treasures.

------
As the app will be mainly designed for people who want to discover new music, there will be a button
right in the middle with words "Surprise me" - if they click on it, a new song will pop up above it
(make things visible). This will make George happy, as he will be able to find some exciting new tunes
with one click of a button (simplifying the structure of the task). 
There will be also a small widget at the bottom showing a song that was recently played by someone.
Because of her love of comunity at the festivals, Lucy will find this feature exciting.
Users will be able to save the songs they found appealing to favourites (by clicking on heart next to it)
- that will help Kath-O with growing their music collection and being able to reference it back. 
Songs can be paused, stopped, played again. All that by using icons people already know (using both knowledge 
in the world and in the head, when all else fails - standarise).
The button will stay on the page (unless user checks their profile and stored songs), so they will always
have access to it (exploit the power of constraints).
There will also be a history of played songs, in case user clicks on the button again by accident, and
they didn't save the song, and want to play it again (design for error).

This is an application I would much like to use myself, as I am currently after a festival where I discovered
a new exciting music I wouldn't search myself of a genre I probably wouldn't pick. I am also very tired
of Spotify algorithm and its choices for me, so would love to dive into something different. I am not a DJ
though, but know my DJ friends would for sure appreciate an app of quirky, non-mainstream music.

The app would have to consider paying royalties (the copyright changes constantly). People are also changing
the way they play music, so it would have to be made connective with smart home appliances and phone Assistants.
It would also have to go through accessibility testing to make sure people with impaired vision would be able
to use it.

"""