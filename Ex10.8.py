# If there are 23 students in your class, what are the chances that 
# two of you have the same birthday? You can estimate this probability 
# by generating random samples of 23 birthdays and checking for matches. 
# Hint: you can generate random birthdays with the randint function in the random module.

from random import randint

def date_generator(students):
    dates = []
    for s in range(students):
        dates.append(randint(1,366))
    return dates

# The Date Generator will generate the random number of dates using randint() function

def has_matches(dates):
    dates.sort()
    for i in range(len(dates) - 1):
        if dates[i] == dates[i+1]:
            return True
        return False

#The has_matches function will match the birthday days between two students having
# birthday at same date

def same_day_birthday(num_of_iteration, students):
    matches = 0
    for i in range(num_of_iteration):
        dates = date_generator(students)
        if has_matches(dates):
            matches += 1
    print(f'There are {matches} classes having student with the same birthday date in {num_of_iteration} chances')

same_day_birthday(500,23)
# The same_day_birthday will do the number of iterations to check the how one student birthday date
# can be matches with another student birthday. When it matches it increases the match count.

# Important Part: As date_generator() generates the random date using randint(), it generates the random
# date for one student at a time which means with the help of same_day_birthday(), it iterates 1000 times for
# one student with number of random dates and with has_matches(), it compares the two students having same birthday date
# and increasing the count of matches in same_day_birthday() so, that we can print the number of matches 
# which is done through 1000 iterations for per student.
