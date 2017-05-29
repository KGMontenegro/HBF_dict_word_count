# put your code here.
our_file = open("test.txt")
#our_bigger_file =open("twain.txt")

#pseudo code
#open file
#create a function
#we want the function to take the body of text inside file and counts how many times 
#each word occurs separated by spaces
#we need a empty dictionary to store word count
# create for loop for file;
#we need a for loop that iterates thru file 
#inside our for loop we need a conditional that checks if word is in dict then +1 if not add 1

def count_words(afile):
    our_dict = {}
    #sentence = afile.split(" ")
    
    for line in afile:
        sentence = line.split()
        print sentence

count_words(our_file)