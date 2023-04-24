

'''Homework 1 App 2.   Developed by : Sonal Mann. 18 April 2023.

Student scoring/grading App.
input : student name (string), HomeWork 1 & 2 score (float), Test 1 & 2 score (float)
outputs : name (string), Homework 1 score out of 50 (float), Homework 2 score out of 50 (float),
Test 1 score out of 30(float), Test 2 score out of 30 (float), scaled total score out of 100 (float), Grade (string) '''


#user enters name , scores for Homework 1 & 2 and Test 1 & 2. display name, Home work 1 scores, Homework 2 scores, 
#Test 1 scores, Test 2 scores, Scaled total score, grades. 

#input
name = str(input('Enter Student Name >'))
homework_1_score = float(input('Enter Home work 1 scores \n >'))
homework_2_score = float(input('Enter Home work 2 scores \n >'))
test_1_score = float(input('Enter Test 1 scores \n >'))
test_2_score = float(input('Enter Test 2 scores \n >'))

#initialisations
homework_weight = 60 # weight for homework score is 60%
test_weight = 40     #weight for test score is 40%


#computation

max_homework_score = 50 + 50    # homework max score is 50 each 
max_testscore = 30 + 30         # test max score is 30 each 

#scaled total score is calculated out of 100, by scaling the homework component to 60 points, 
#and the test component to 40 points

total_homework_score = homework_1_score + homework_2_score 
total_test_score = test_1_score + test_2_score
scaled_total_score = (total_homework_score * homework_weight / max_homework_score) + (total_test_score * test_weight / max_testscore) 

#Grades assigned according to scaled total score

if scaled_total_score > 90: # > 90 - 100
    grade = 'A'
elif scaled_total_score >= 80:  # 80 - 90
    if test_1_score == 30:  # test score 1 got 30 scores, grade upgrades to A
        grade = 'A'
    elif test_2_score == 30: # test score 2 got 30 scores, grade upgrades to A
        grade = 'A'   
    else: 
        grade = 'B'
elif scaled_total_score >= 60: # >= 60 
    grade = 'C'
else:                          # remaining
    grade = 'D'        
#ends if



#output

print(f'Name :      {name :s}')
print(f'Homework 1: {homework_1_score: .2f}/50 ')
print(f'Homework 2: {homework_2_score : .2f}/50 ')
print(f'Test 1:     {test_1_score :.2f}/30 ')
print(f'Test 2:     {test_2_score :.2f}/30')
print(f'Scaled Total score: {scaled_total_score: .2f}/100 \nGrade: {grade :s}')


