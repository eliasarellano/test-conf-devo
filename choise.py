import random

#input file
fin = open("data.txt", "rt")
#output file to write the result to
fout = open("index.php", "wt")
#for each line in the input file
for line in fin:
    #fout.write(line.replace('question1', words[firstquestion]).replace('question2', words[secondquestion]).replace('question3', words[thirdquestion]))
    fout.write(line)
#close input and output files
fin.close()
fout.close()