#Given a .txt file that has a list of a bunch of names, 
# count how many of each name there are in the file, 
# and print out the results to the screen.

with open('basicExercise9.txt', 'r') as f:
    # contents = f.readlines()
    # print(contents)                   #print the content

    lines = len(f.readlines())
    print('Total Number of lines:', lines)      #print the number of lines of content

f.close()
