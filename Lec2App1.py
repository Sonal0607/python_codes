""" Functions.
"""
#define a function = create a function
"""
def  greet(msg): #header
    print(msg)
#end function

def bye():
    print('Good Bye!')

# 1 a funtion to display a greeting

#main
#call the function = invoke the function
message = 'Good Evening!'
greet(message)   #msg = message
#parameter = agument

message = 'Bye!'
greet(message)
#bye()

# r = 10
#radius = 4
# pi * radius squared 

"""



# score at or above 80 gets A others get B

#name ? compute_grade()
#output ? grade (str)
#input ? score (float)

#functions
def compute_grade(score):
    if score >= 80.00:
        grade ='A'
    else:
        grade = 'B'

    print(grade)
#end function

#main
score = float(input('Enter your score >'))
compute_grade(score)



























