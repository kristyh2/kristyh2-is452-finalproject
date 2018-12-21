# kristyh2-is452-finalproject
This holds materials for my final project in IS452. The purpose of my final project is to develop a program that grades assignments for completion credit.

## Project Abstract

The purpose of this programming project is to develop a program that will grade assignments and assign a completion grade to each student. This tool is not intended for assignments that require the evaluation of ideas or other forms of abstract thinking. Instead, this tool is better-suited for assignments that are graded on the student's ability to follow instructions delineated by the administrator. This tool may be particularly useful to instructors in large lecture classes who would like to expedite the process of assigning completion credit to students based on some objective criterias.

This program is meant to be expanded. Currently, it can only grade based on completion and wordcount. In the future, you will be able to grade based on keywords/answers.

This program is able to complete the following tasks:

* Input a list of IDs (e.g., a class roster; UIN) and also a list of txt files (e.g., assignment submissions) to assign grades to those who completed the assignment.

Beyond this basic task, this program is able to assign a weighted grade to each student based on the following criteria:
* Follows basic instructions outlined in the rubric
* Meets word limit criteria
* Contains keywords relevant to the topic of the assignment (COMING SOON!)
* Answers questions correctly (COMING SOON!)

## Sample Assignment Instructions (Feel free to copy and paste this text into your assignment instructions)

To receive a grade for this assignment, you must follow the following formatting requirements:
1. The first line of your assignment must be [Insert name of Assignment].
2. The second line of your assignment must be your UIN.
For example:
  CMN529_ASSN1
  UIN: 67203477

3. Name your assignment "CMN_ASSN1_YOUR-UIN" (e.g., CMN529_ASSN1_67203477)
4. Submit you assignment as a word document (e.g., CMN529_ASSN1_67203477.doc) and a plain text file (e.g., CMN529_ASSN1_67203477.txt). You will be graded based on the contents of your text file submission. Please make sure to double-check that you meet these formatting requirements before submitting.

## How To Run the Program

Step 0. Before you can run the program, you will need to create a project folder for the assignment. The folder should contain the following items:
* The python code (kristyh2_final-project.py)
* All submitted assignments in plain txt files (Hint: Files must be named "assignment-name_ID#.txt" for example, "CMN529_ASSN1_67203477.txt")
* A CSV file with a list of student IDs (see Step 1).

Step 1. Create a csv file with unique IDs that represent the students in your class (like a class roster os student ID numbers). You must follow these criteria:
* Column A will hold the list of IDs 
* In row 1, give your list a name (e.g., "id")
* Save your spreadsheet as a .csv (Hint: Before saving, copy the file name you create so that you can easily input it in the next step).

Step 2. Run the program. Once you run the program, you will be prompted to input the following:
* csv_input: Name of CSV file with unique student IDs (Hint: this will be the name you just copied).
* assn_name: Name of assignment you told students to put in the submission (e.g., CMN529_ASSN1)
* possible_points: The total amount of points this assignment is worth (e.g., 20)
* completion_wt: The percentage that submitting the assignment is weighted (Hint: If you do not have a word limit, enter 0).
* wordcount_min: The minimum number of words students must have to receive credit (Hint: If you are only grading for completion, enter 0).
* wordcount_max: The maximum number of words students must have to receive credit. (Hint: If there is no wordcount limit, enter something like 100000000000).
* wordcount wt: The percentage that following the wordcount criteria for the assignment is weighted (Hint: If you do not have a word limit, enter 0).

