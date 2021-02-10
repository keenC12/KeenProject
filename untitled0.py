

#modules for data analysis

import pandas as pd
import matplotlib.pyplot as plt

#Variables for list
subjects = []
scores_subject = []

def number_of_subjects():
    subjN= int(input("Enter Number of Subjects: "))
    return subjN
def number_of_scores():
    studentsN = int(input("Enter number of students: "))
    return  studentsN



#description about the program
print("\nThis program will record scores in a subject of x-number of students")


#Ask imput for Subject name and respective  scores
def recordSubject(sub_j):
    sub_j = []
    while True:
        subjN = number_of_subjects()
        if subjN > 12 or subjN < 0 :
            print("Input error!!!")
            continue
        for i in range (1,subjN+1) :
            subject = str(input("Enter a subject: "))
            sub_j.append(subject) #add each input to the list
        break    
    return sub_j
           
'''def recordScores(scores_sub,recordsub):   
    scores_sub = []
    while True:
        scoresN = number_of_scores()
        if scoresN > 30 or scoresN < 0 :
            continue
        for sub in recordsub:
            print("\nRecord {} scores".format(sub.upper()))
            for i in range (1,scoresN+1):
                print("\nStudent no.",i)
                score = int(input("Enter Score: "))    
                scores_sub.append(score) #add each input to the list
        break
    return scores_sub'''

def arrangedata(subjectList,students):
    for sub in subjectList:
        scoreList = []
        dataList = []
        print("\nRecord {} scores".format(sub.upper()))
        for i in range (1,students+1):
            print("\nStudent no.",i)
            score = int(input("Enter Score: "))
            scoreList.append(score)
        data = dataframe(sub,scoreList)
        dataList.append(data)  
            
        return print(dataList)
        
def dataframe(subject, scores):
    df = pd.DataFrame({ subject: scores})
    return df

def main(record,student_ctr):
    x = student_ctr
    ctr = 0
    while ctr != x:
        arrangedata(record,x)
        ctr += 1

 
#list of subject   
recordsub = recordSubject(subjects)



#Sets the subject and scores in a data frame                           
#scores_df = pd.DataFrame(recordscore)
subject_df = pd.DataFrame(recordsub)

#data = pd.DataFrame({recordscore+recordsub})
main(recordsub,number_of_subjects())


print(recordsub)
#print(recordscore)

#print(scores_df) 
print(subject_df) 

