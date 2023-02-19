import os
from collections import Counter
import re
import socket

# Get the list of all files and directories

path = "/home/data"
output_path = "/home/output"
dir_list = os.listdir(path)

dir_list_text_files = []
for element in dir_list:
    if '.txt' in element.lower():
        dir_list_text_files.append(element)

dir_list = dir_list_text_files

output_file = open(output_path+'/result.txt', "w")

print('List of Text Files in the location')
output_file.write('List of Text Files in the location\n')
for files in dir_list:
    print(files)
    output_file.write(files+'\n')

words_in_files = Counter()

for files in dir_list:
    counter = Counter()
    f = open(path + '/' + files, "r")
    docs = f.readlines()
    f.close()
    for lines in docs:
        counter.update(re.findall('\w+', lines))
    words_in_files[files] = counter.total()

print('\nTotal Number of Words are shown as below for each text file')
output_file.write('\nTotal Number of Words are shown as below for each text file\n')
for files in words_in_files:
    print('Total Number of Words in the file: {} is {}'.format(files,words_in_files[files]))
    output_file.write('Total Number of Words in the file: '+files + ' is ' + str(words_in_files[files]) + '\n')

print('\nGrand Total Number of Words present in all the Text Files is: {}'.format(words_in_files.total()))
output_file.write('\nGrand Total Number of Words present in all the Text Files is: '+ str(words_in_files.total())+'\n')

files = 'if.txt'
counter = Counter()
if files in list(map(lambda x: x.lower(), dir_list)):
    f = open(path + '/' + 'IF.txt', "r")
    docs = f.readlines()
    f.close()
    for lines in docs:
        counter.update(re.findall('\w+', lines.lower()))

    top_three_words = counter.most_common(3)
    print('\nTop 3 Words with maximum number of counts for the file IF.txt')
    output_file.write('\nTop 3 Words with maximum number of counts for the file IF.txt\n')
    for element in top_three_words:
        print('The number of occurences for the word "{}" is: {}'.format(element[0],element[1]))
        output_file.write('The number of occurences for the word "'+element[0]+'"'+' is: '+ str(element[1])+'\n')
else:
    print('\nThere is no file name IF.txt in the folder. Please upload')
    output_file.write('\nThere is no file name IF.txt in the folder. Please upload\n')

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("\nIP Address is: {}".format(IPAddr))
output_file.write('\nIP Address is: '+IPAddr+'\n')
output_file.close()