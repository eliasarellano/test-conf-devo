# input file
fin = open("data.txt", "rt")
# output file to write the result to
fout = open("index.php", "wt")
# for each line in the input file
for line in fin:
    fout.write(line)
# close input and output files
fin.close()
fout.close()