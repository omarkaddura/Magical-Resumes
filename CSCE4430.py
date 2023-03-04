
#Make sure you have all the libraryies imported/installed, use the pip command in cmd if necessary
# python -c "import nltk; nltk.download('punkt')"
# # python -c "import nltk; nltk.download('stopwords')"
from requests_html import HTMLSession
from rake_nltk import Rake

#function to extract text, it works by feeding it a url and an xpath and it returns you the text of the xpath
def extract_text(url, xpath):
    
    #start session
    s = HTMLSession()

    #store url response in response
    response = s.get(url)
    
    #look for the text in that xpath and return it
    return response.html.xpath(xpath)

#function below checks if a link is valid
def is_valid_link(link):
    try:
        session = HTMLSession()
        response = session.get(link)
        response.raise_for_status()
        return True
    except Exception as e:
        print(e)
        return False

#loop below prompts the user to enter the option 1-3 and only breaks when the user input is correct
while True:
    prompt = input("Choose site(Enter corresponding digit):\n1-LinkedIn\n2-Indeed\n3-Glassdoor\n")

    if prompt.isdigit() and (int(prompt) == 1 or int(prompt) == 2 or int(prompt) == 3):
        break
    else:
        print("Error, input has to be either 1,2 or 3. Try Again!\n")
        continue

#necessary xpath values to search for in each website
#xpath for LinkedIn
linkedinXPath = '//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div//text()'
#xpath for Indeed
indeedXPath = '//*[@id="jobDescriptionText"]//text()'
#xpath for glassdoor
glassdoorXPath = '//*[@id="PageContent"]/div[1]/div[2]/div//div/p/text() | //*[@id="PageContent"]/div[1]/div[2]/div//ul/li/text() | //*[@id="PageContent"]/div[1]/div[2]/div//div/div/text() | //*[@id="PageContent"]/div[1]/div[2]//div/p[1]/b/text()'

#if the user inputted 1
if int(prompt) == 1: 

    #loop below prompts user to enter link and only breaks when the user enters a valid link
    while True:
        url = input("Paste your LinkedIn URL here: ")
        print("\n")
        if is_valid_link(url):
            break
        else:
            print("Link is not valid, try again")
            continue
    #call extract_text and store it in storeList
    storeList = extract_text(url, linkedinXPath)
    #print(storeList) use this to test the extract_text result

#if the user inputted 2
elif int(prompt) == 2:
    #loop below prompts user to enter link and only breaks when the user enters a valid link
    while True:
        url = input("Paste your Indeed URL here: ")
        print("\n")
        if is_valid_link(url):
            break
        else:
            print("Link is not valid, try again")
            continue
    #call extract_text and store it in storeList
    storeList = extract_text(url, indeedXPath)
    #print(storeList) use this to test the extract_text result

#if the user inputted 2
elif int(prompt) == 3:
    #loop below prompts user to enter link and only breaks when the user enters a valid link
    while True:
        url = input("Paste your GlassDoor URL here: ")
        print("\n")
        if is_valid_link(url):
            break
        else:
            print("Link is not valid, try again")
            continue
    #call extract_text and store it in storeList
    storeList = extract_text(url, glassdoorXPath)
    #print(storeList) use this to test the extract_text result

#if the user wrong input and somehow it got through the while loop, print an error statement and exit
else:
    print("Error, input is not 1,2 or 3")
    exit()



#code below is to convert list into a string, "extract_text" returns a list and rake only works with strings
my_string = ', '.join(storeList)
#use code below to test the input of the string
print(my_string)


#code below utilizes the rake_nltk lib to search for key phrases and prints key phrases that were repeated more than 5 times, it currently does not work
#r = Rake()
#r.extract_keywords_from_text(my_string)
#for rating, keyword in r.get_ranked_phrases_with_scores():
#    if rating > 5:
#        print(rating, keyword)
