import sys
data_to_pass = 'Send this string to javascript file'
input = sys.argv[1]
output = data_to_pass
print(output)
sys.stdout.flush()

    


from difflib import SequenceMatcher #importing SequenceMatcher from difflib library to perform plagiarism operations
def Plagiarism_Checker(file1_data, file2_data): 
    similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
    return (similarity*100)

str1 = input("Enter doc1: ")
str2 = input("Enter doc2: ")
final = Plagiarism_Checker(str1, str2)
print("Similarity: ", final, "%")