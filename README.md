# Attendance Sheet Generator

This script is written to generate attendance sheets for face-to-face exams.
An html page source from university's system should be downloaded containing the pictures and other information of course's students.

### Things to Check
Please check the tags and indexes if the university is different than Bogazici.

Please check the file and folder names. 
You should create the folder MT1-Attendance (the target folder to save the pdfs).

An excel file named "seating.xlsx" is read, this file contains the seating plan for the exam. This code reads the excel for 4 sessions, 3 classes, and creates the attendance sheets accordingly. Modify it if your plan is different.

Pdfkit's configuration and beautifulsoup encoding is done according to Windows, change them if you are using a different operating system.

### Required Packages
BeautifulSoup
Pandas
Numpy
Pdfkit
