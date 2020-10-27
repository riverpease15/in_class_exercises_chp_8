## 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that
## starts with 'From ' like the following line:
    ## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
## You will parse the From line using split() and print out the second word in the line
## (i.e. the entire address of the person who sent the message). Then print out a count
## at the end.
## Hint: make sure not to include the lines that start with 'From:'. Also look at the
## last line of the sample output to see how to print the count.

file_name = input("Enter file name: ")

if len(file_name) < 1 :
    file_name = "mbox-short.txt"
file = open(file_name)

data = []
count = 0

for line in file :
    if line.startswith("From") and len(line.split()) > 2 :
        list_line = line.split()
        data.append(list_line[1])

for item in data :
    print(item)

print("There were", len(data), "lines in the file with From as the first word")
