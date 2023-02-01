# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), 
# and instead of printing the results to a screen, write the results to a txt file. 
# In your code, just make up a name for the file you are saving to.

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

with open("basicExercise9.txt","w") as f:        #create the txt file
    for story_heading in soup.find_all(class_="story-heading"): 
        if story_heading.a: 
            f.write(story_heading.a.text.replace("\n", " ").strip())    #writing into the txt file
        else: 
            f.write(story_heading.contents[0].strip())           #writing into the txt file

f.close()