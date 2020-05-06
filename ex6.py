# Using f'' to format a string

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x!r}")
print(f"I also said: '{y}'")

#Using .format() to format a string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# Concatenate strings

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


#Learn about !r, !s, 
#Learn that w+ e is ineffcient
#''.join([w,e]) is better