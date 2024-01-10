#  Winter break Python Mad libs 
# Create a short mad lib story about your winter break. 
# Your mad lib should include 6 input fields for users to enter data.
# Your mad lib program should prompt the user to enter 2 nouns, 2 verbs, and 2 adjectives. 
# Your mad lib should be written in complete sentences. 
# Once completed, submit your madlib to your github repository by using the source control tool in codespaces. 
work = input('Put in a verb ')
food = input('Put in a noun that is food ')
important = input('Put in a noun that is work ')
excer = input('Put a verb that is exercise ')
fruit = input ('Put in the size of a fruit, and the fruit your eating ')
clock = input('Put in the time ')

Break = "During the break I mostly slept in and just relaxed did some  " + work
Eat = 'I had some ' + food + ' for dinner'
With = 'I worked on ' + important + ' and more major progress'
Move = 'I went on a workout doing ' + excer + ' and it was great.'
Ate = 'I even ate a '  + fruit +  ' and that was weird.'
Time = 'I ended my date going to bed at ' + clock + ' because the time just felt right.'

print(Break, Eat, With, Move, Ate, Time)

