## Task 1 (Git and Github)

### 1.1
Great definitions and knowledge of git fundamentals.

4/4

### 1.2
Again, you've shown you understand the flow and how git works, nice work!

3/3

### 1.3
Great stuff, just be a little careful about terms but all these definitions have the right combination of local/remote repository, staging area and working directory. Your definitions of fetch/pull are great! I've not given the mark for `git add` purely because the term staging area was needed.

5/6

## Task 2 (Exception Handling)

Brilliant code! I've been through and tried to break it, here's what I found:
- The pin functionality works great! Accepts any input without raising errors but only lets me in with a correct pin.
- It doesn't accept a non-numeric and asks to withdraw a valid amount - great
- It doesn't allow negative numbers either, treating it the same as an invalid input.

The two things stipulated in the mark scheme are 2 exceptions caught in try/except (done!) and raising an exception (which you've done too ... nice!)

This is an extremely nice and concise script, it catches everything it needs to nicely and LOVE the ascii art, nice touch. Absolutely perfect!

15/15

## Task 3 (Testing)

Great test cases!! This is brilliant. I did wonder why `atm()` was commented out in the main programme, this is a great use case for `if __name__ == '__main__'`, it loads `atm` if ran as a script and doesn't when imported (e.g. in the test script).

Testing exceptions is great but coupling that with the exception messages is awesome! You've clearly put the time in the practice and it shows.

The one thing this is missing is testing `pin_tries` or `atm`, now both as is might be a little much for unit testing as is so might need refactoring to make parts more accessible. It would've been great to see an attempt with a patch or two to enable testing. See the example I added to see how it could work (not as large as I thought it might become!)

12/15
