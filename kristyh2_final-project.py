#Final Project
#Kristy Hamilton
#netid: kristyh2

## RUBRIC FOR STUDENTS
# 1. The first line of your assignment must be [Insert name of Assignment].
# 2. The second line of your assignment must be your UIN.
# For example:
# CMN529_ASSIGNMENT1
# UIN: 67203477

# For the sake of this assignment, we start at the point of having assignments submitted as txt files.
# In the future, I will add code that is able to convert word documents into txt files using the following method:
# https://automatetheboringstuff.com/chapter13/


## BASIC PROGRAM:


# this is a brief explanation of the program
print("This program grades basic assignments for a class. To get started, you must create a CSV file that contains a list of "
      "unique IDs that correspond to an assignment in the first column. Give the column a heading name in row 1. All other columns must be empty.")

# input a csv file
csv_input = input("What is the name of the csv you would like to read? (e.g., CMN529_assn1.csv): ")


# list of assignment criteria selected by the grader
assn_name = input("What is the name of the assignment? (You must instruct students to write the assignment name on the first line of their word document): ")
assn_name = assn_name.lower()

possible_points = float(input("How many points is this assignment worth? (e.g., 20): ")) #this represents a total. Weighted percentages will act upon this number
completion_wt = float(input("How much is completion weighted? (e.g., put .9 if completion is worth 80% of the grade): "))
wordcount_min = float(input("What is the MINIMUM word count for this assignment? (e.g., 500): "))
wordcount_max = float(input("What is the MAXIMUM word count for this assignment? (e.g., 1000): "))
print("  IMPORTANT: You have ", round(1-completion_wt, 2), "left to distribute.")
wordcount_wt = float(input("How much is wordcount weighted? (e.g., put .1 if completion is worth 20% of the grade): "))
wt_total = wordcount_wt + completion_wt

if (wt_total) != 1.0:
    print("Your weighted inputs must add to 1.0. Please try again.")
    completion_wt = float(input("How much is completion weighted? (e.g., put .9 if completion is worth 80% of the grade): "))
    print("  IMPORTANT: You have ", round(1-completion_wt, 2), "left to distribute.")
    wordcount_wt = float(input("How much is wordcount weighted? (e.g., put .1 if completion is worth 20% of the grade): "))



## SAMPLE INPUT FOR TESTING

# csv_input = "sample_CMN529_assn1.csv"
# assn_name = "CMN529_ASSN1"
# assn_name = assn_name.lower()
# possible_points = 20
# completion_wt = .9
# wordcount_min = 500
# wordcount_wt = .1

# This section contains all the functions I will be using for this program

# function that counts words
def wordcount(text):
    return len(text.split())

#function to grade each assignment
def grade_assn(text):
    completion_score = completion_wt*possible_points #calculate the possible points for completion
    wordcount_score = wordcount_wt*possible_points
    count = wordcount(text)
    if wordcount_max > count > wordcount_min:
        text = wordcount_score + completion_score
    else:
        text = completion_score
    return text

#function to clean file name so that it shows only the ID (this will serve as a check)
def clean_filename(line_str):
    line_str = line_str[len(assn_name)+1:]
    line_str = line_str[:-4]
    return line_str


## MAIN CODE STARTS HERE

# Code to input a CSV file

import csv

id_list = [] # id_list contains a string of unique IDs that correspond to all students in the class

with open(str(csv_input), 'r', newline = '') as infile: #opens the csv file with IDs and makes a list
    csvin = csv.reader(infile)
    headers = next(csvin)
    for line in csvin:
        id_list.append(line)

id_list = [i[0] for i in id_list]
# print(id_list)


# Now, I will create a path with all assignment submissions to do the main thing
import glob

read_files = glob.glob(str(assn_name)+"*.txt") #this creates a path for all txt files that begin with "Sample". You can change this to something like the name of your course.

clean_id_list = []
possible_points_list = []
wordcount_list = []
grade_list = []
percentage_list = []

gradebook = [] # I'm creating a gradebook which will become a dictionary that will be exported to CSV. This is like "allrows"

completed_assn = []
for f in read_files:
    completed_assn.append(clean_filename(str(f)))
print(completed_assn)

for id in id_list:
    for f in read_files: # for one assignment in all the assignments glob found
        clean_id = clean_filename(str(f))
        if id == clean_id:
            with open(f, "r", encoding = 'utf-8') as infile: # may have to change encoding if you're getting an error
                text = infile.readlines()
                assignment = text[0] #first line of the assignment (should be assignment name)
                uin = text[1] #second line of the assignment (should be uin)
                assntext = "".join(text[2:]) #everything after line 2 is the assignment text
                count = wordcount(assntext)
                grade = grade_assn(assntext)
                percentage = (grade/possible_points)*100
                print(clean_id, assignment, uin, count, grade, percentage)
                row = []
                row.append(id)
                row.append(possible_points)
                row.append(count)
                row.append(grade)
                row.append(percentage)
                gradebook.append(row)
                # long format
                clean_id_list.append(clean_id)
                possible_points_list.append(possible_points)
                wordcount_list.append(count)
                grade_list.append(grade)
                percentage_list.append(percentage)
    if id not in completed_assn:
                row = []
                row.append(id)
                row.append(possible_points)
                row.append(0)
                row.append(0)
                row.append(0)
                gradebook.append(row)
            # long format
            # clean_id_list.append("NA")
            # possible_points_list.append(possible_points)
            # wordcount_list.append(0)
            # grade_list.append(0)
            # percentage_list.append(0)



# print(clean_id_list, possible_points_list, wordcount_list, grade_list, percentage_list)
# print(len(clean_id_list), len(possible_points_list), len(wordcount_list), len(grade_list), len(percentage_list))




headers = ["clean_id", "possible_points"+" ("+str(possible_points)+")", "wordcount"+" ("+str(wordcount_min)+")", "grade", "percentage"]

with open(str(csv_input[:-4])+"_GRADED"+".csv", "w", newline = "") as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(gradebook)

# OLD STUFF, BLEH

# # once we have a txt file with all the assignments, we can do the thing.
# infile = open("assn.txt",errors='ignore')
# assn = infile.read()
# assn_lines = assn.split('\n') #splits into a list based on new lines
# infile.close() #close the connection
# end = "endofdocument"
# assn_lines.append(end) #append end so I can use that as a stopping point to slice information
# assn_words = clean_words(assn_lines)
# end_index = assn_words.index('endofdocument')


# print(assn_lines)
# print(assn_words)
# print(end_index)
#
# #print(wordcount(assn_lines)) #I verified this against the google doc word counter
# print(assn_name)
# print(assn_words)
# match = closeMatches(assn_name,assn_words)
# print(match)
# wordcount_list = []
# completion_list = []

# for id in id_list:
#     print(id)
#     completion_score = completion_wt*possible_points #calculate the possible points for completion
#     def contains(name): #function that looks for string within lines
#         for line in assn_lines:
#             if str(assn_name) in line.lower():
#                 name = assn_name
#         return name
#     if id in assn_words:
#         completion_list.append(completion_score) #if id is in the assn, append completion score to the list of completion scores
#         assn_start = assn_words.index(id)
#         print(assn_start)
#         assn_parameter = assn_words[assn_start:end_index]
#         parameter_end = []
#         for string in assn_parameter:
#             string = str(string)
#             parameter_end = [(m.start(0), m.end(0)) for m in re.finditer(str(assn_name), assn_parameter)]
#         print(parameter_end)
#         print(assn_end)
#         one_assn_parameter = assn_parameter[assn_start:assn_end] #This is the parameter from the id that is in question until the next assignment. This may be a good place to add the keyword stuff
#         wordcount = wordcount(one_assn_parameter) #code to count words in assignment
#         wordcount_score = wordcount_wt*possible_points
#         if wordcount > wordcount_min:
#             wordcount_list.append(wordcount_score) #if wordcount is greater than a minimum number than they get full credit. If not, they get 0.
#     else:
#         completion_list.append("0") #if id is not in assn, append 0 to the list of completion scores
#         wordcount_list.append("0")
#
# print(id_list)
# print(wordcount_list)
# print(completion_list)

############################################################################
##                                                                        ##
##                             ADD-ON PROGRAM                             ##
##                                                                        ##
############################################################################

# keywords = eval(input("How many keywords would you like to input? This could be an answer to a question. (e.g., 5): "))
#
# keyword_list = []
# keyword_wt_list = []
#
# for i in range(keywords):
#     num = i + 1
#     keyword = float(input("What is your keyword? "))
#     keyword_wt = float(input("What is the weight of this keyword? "))
#     keyword_list.append(keyword)
#     keyword_wt_list.append(keyword_wt)

# def wordcount(parameter_of_lines):
#     big_string = "\n".join(parameter_of_lines)
#     def clean(big_string):
#         for character in string.punctuation:
#             big_string = big_string.replace(character, "")
#         return big_string
#     word_list = big_string.split()
#     parameter_of_lines = len(word_list)
#     return(parameter_of_lines)
