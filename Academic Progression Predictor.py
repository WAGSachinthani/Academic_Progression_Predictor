#import sys
import sys

#Initializing variables
progress=0 
trailer=0 
retriever=0 
excluded=0
outcome=0
student_number=0
mark_range=[0,20,40,60,80,100,120]
pass_credit = 0
defer_credit =0
fail_credit =0
total_credit=0
input_credits=0
all_student_data = []
progresslist = []
trailerlist =[]
excludelist =[]
retrieverlist = []

#Print 'welcome ' and Display instructions
print("                                                          ::::::::::::::::::::::  ")
print("                                                        ::::::::::::::::::::::::::  ")                  
print("                                                 ::::::::   W E L C O M E! ! !  - Academic Progression Predictor :::::::: ")
print("                                                        ::::::::::::::::::::::::::  ")
print("                                                          ::::::::::::::::::::::  ")
print("IMPORTANT : Enter your PASS , DEFER and FAIL credits to predict progress results at the end of each academic year.  " )

#Get user input credits
def input_credits():
    while True:
        try:
            pass_credit = int(input("\nEnter your PASS credits: "))  #Get user pass credits
            if pass_credit not in mark_range:
                print(" ---OUT OF RANGE!--- ")  # display ‘Out of range’ if credits entered are not in the range.
                continue
            defer_credit = int(input("Enter your DEFER credits: ")) #Get user defer credits
            if defer_credit not in mark_range:
                print(" ---OUT OF RANGE!--- ")  # display ‘Out of range’ if credits entered are not in the range.
                continue
            fail_credit = int(input("Enter your FAIL credits: ")) #Get user fail credits
            if fail_credit not in mark_range:
                print(" ---OUT OF RANGE!--- ")  # display ‘Out of range’ if credits entered are not in the range.
                continue
            total_credit = pass_credit + defer_credit + fail_credit
            if total_credit != 120:
                print(" ---TOTAL INCORRECT!--- ") #display ‘Total incorrect’ if the total of the pass, defer and fail credits is not 120.
                continue
            return pass_credit, defer_credit, fail_credit
        except ValueError:
            print(" ---INTEGER REQUIRED!--- ") # display ‘Integer required’ if a credit input is the wrong data type
            continue

#Get the Number of students
while True:
    student_number+=1 #reset the student number
    print("\nStudent :", student_number) #Display the number of students
       
    pass_credit, defer_credit, fail_credit = input_credits() #calling for input credits
    
#Append student data to the list        
    student_data=[]
    student_data.append(pass_credit)
    student_data.append(defer_credit)
    student_data.append(fail_credit)
    all_student_data.append(student_data)

#Providing predictions of progress results
    while True:
        if pass_credit==120 and defer_credit==0 and fail_credit==0:
            print ("\nProgression Outcome :  Progress") #Print progression outcomes
            progress+=1 #Count progression outcomes
            outcome+=1 #Count outcomes for get total outcomes
                        
        elif pass_credit==100 and defer_credit==20 and fail_credit==0:
            print("\nProgression Outcome :Progress (module trailer)")
            trailer+=1
            outcome+=1
                        
        elif pass_credit==100 and defer_credit==0 and fail_credit==20:
            print("\nProgression Outcome :Progress (module trailer)")
            trailer+=1
            outcome+=1
                        
        elif pass_credit==40 and defer_credit==0 and fail_credit==80:
            print("\nProgression Outcome :Exclude")
            excluded += 1
            outcome += 1
                        
        elif pass_credit==20 and defer_credit==20 and fail_credit==80:
            print("\nProgression Outcome :Exclude")
            excluded += 1
            outcome += 1
                        
        elif pass_credit==20 and defer_credit==0 and fail_credit==100:
            print("\nProgression Outcome :Exclude")
            excluded += 1
            outcome += 1
            
        elif pass_credit==0 and defer_credit==40 and fail_credit==80:
            print("\nProgression Outcome :Exclude")
            excluded += 1
            outcome += 1
            
        elif pass_credit==0 and defer_credit==20 and fail_credit==100:
            print("\nProgression Outcome :Exclude")
            excluded += 1
            outcome += 1
            
        elif pass_credit==0 and defer_credit==0 and fail_credit==120:
            print("\nProgression Outcome :Exclude")
            excluded += 1
            outcome += 1
            
        else:
            print("\nProgression Outcome :Do not progress – module retriever")
            retriever += 1
            outcome += 1

# Get predict progression outcomes for multiple students.
        print("\nWould you like to enter another set of data?")
        next_round = input("Enter 'y' for yes or 'q' to quit and show the histogram. (y/q)?").lower() #Ask for the next student or display histogram(yes/no)
        if next_round == "y":
            break
        elif next_round=="q":

#Producing a 'histogram' where each star represents a student achieving a progress result in the category range.
            print('-'*150)
            print("                                               ;;;::::: H I S T O G R A M :::::;;;")  #Print 'histogram'
            print("   progress ", progress ,":",'*'*progress )
            print("   Trailer  ", trailer  ,":",'*'*trailer )
            print("   Retriever",retriever ,":",'*'*retriever)
            print("   Excluded ",excluded  ,":",'*'*excluded)
            print("\n ",outcome,"Outcomes in total")   #Display outcomes in total
            print('-'*150)

            print("\n\nSTUDENT DATA: ") #print student data

#input data stored in a list
            for sublist in all_student_data:
               if sublist == [120, 0, 0]:
                  progresslist.append(sublist)
               elif sublist in [[100,0,20] , [100,20,0 ]]:
                  trailerlist.append(sublist)
               elif sublist in [[40,0,80] ,[20,20,80] , [20,0,100], [0,40,80] , [0,20,100] , [0,0,120]]:
                  excludelist.append(sublist)
               else:
                  retrieverlist.append(sublist)
            
# Output retrieved from the list
            print("   progress                   - ",progresslist) #Print lists
            print("   Progress (module trailer)  - ",trailerlist)
            print("   Module Retriever           - ",retrieverlist)
            print("   Exclude                    - ",excludelist)
            print('-'*150)

#Get user file name to save data
            file_name = input("Enter the file name to save your data: ")
            
#Write Input data saved to text file
            with open(file_name, mode="w") as file:
                print("   progress                   - ",progresslist,file=file)
                print("   Progress (module trailer)  - ", trailerlist,file=file)
                print("   Module Retriever           - ", retrieverlist,file=file)
                print("   Exclude                    - ", excludelist,file=file)

#Read the Output retrieved from text file
            with open(file_name, 'r') as file:
                contents = file.read()
                print("T E X T  F I L E  : ") #Print 'Text file'
                print(contents)  #Display saved data          
                print('-'*150)                    
                sys.exit() #Exit the program
        else:
            print("\nInvalid input! You have successfully exited the program! ") #Print 'Invalid input' error
            sys.exit() #Exit the program

#End of the code
#References: Python.org. (2019). The Python Tutorial — Python 3.8.0 documentation. [online] Available at: https://docs.python.org/3/tutorial/.
