import os   #importing operating system library to access system operations
from difflib import SequenceMatcher #importing SequenceMatcher from difflib library to perform plagiarism operations
file1 = open("file1.txt", "x")  #Create File 1
file2 = open("file2.txt", "x")  #Create File 2
str1 = input("Write the contents in file 1: ")  #Input data that is to be transfered to file 1
str2 = input("Write the contents in file 2: ")  #Input data that is to be transfered to file 2
file1.write(str1)   #Write file 1 with data from the user in variable str1
file2.write(str2)   #Write file 2 with data from the user in variable str2
with open('file1.txt') as file1, open('file2.txt') as file2:    #Open file 1 as doc1 and open file 2 as doc2
    #file1_data and file2_data reads the data of the document doc1 and doc2 respectively 
    file1_data = file1.read()
    file2_data = file2.read()
    #SequenceMatcher compares the two files and .ratio() function calculates the ratio of plagiarism in the two files
    similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
    print('Similarity: ', similarity*100)   #print function prints the amount of plagiarism in the two files
#To avoid dublication of files, the files that were created at the start of the program are deleted 
os.remove('file1.txt')  
os.remove('file2.txt')