# Alexander Shelton
#
#
#
#

import sys
import requests
from itertools import permutations
import time

##todo: fix instagram, must log in first

SERVICES = ['twitter', 'instagram', 'twitch', 'tiktok']



#setUpSite: Takes the users program argument to check whether or not it is a legitament social media that the program uses
#The function will then return the url used to search for usernames
def setUpSite(_website):
    website = _website.lower()
    if website not in SERVICES:
        print("'{}' is not an accepted service to check usernames for\nGoodbye.".format(website))
        sys.exit()
    print("Accepted web service")
    return website


def generateURL(_service, _name):
    if _service == "instagram":
        url = "https://www.instagram.com/"+_name+"/?__a=1" #uinstagram wont let you view accounts without logging in so we use a account details link
    elif _service == "twitch":
        url = "https://www.twitch.tv/"+_name
    elif _service == "tiktok":
        url = "https://www.tiktok.com/@"+_name
    else:#twitter
        url = "https://www.twitter.com/"+_name
    return url



def scrapeList(_filename):
    path = "../names/"+_filename
    usernames = []
    file = open(path, 'r').read().split('\n')
    for line in file:
        if not line == '':
            # print(len(line))
            usernames.append(line)
    return usernames


#Get numChars is used when program is not gathering usernames from a text file
#The function prompts users to enter how many letters/symbols they want in their username

def getNumChars():
    isOkay = False
    while(isOkay == False):
        numChars = int(input("Usernames must be between 1 and 15 characters\nhow many letters do you want in your username: "))
        if numChars >= 1 and numChars <= 15:
            isOkay = True
    return numChars



#function will send a request to the websites account searching for the profile of the username
#if a 404 or page not found is given, then the username is still available,
#if the page is found, the name is taken
#Program will write to the file "availablenames.txt" of names still available
def checkAvailability(_usernames, _service, website):
    print("checking available names") #debugging
    file = open("../names/availablenames.txt", "w") #opening text file to write names to
    for name in _usernames:
        url = generateURL(_service, name)
        try:
            r = requests.get(url)
            print("Checking username: {}\nStatus code: {}".format(url,r.status_code))
        except requests.exceptions.ConnectionError:
            print("Connection refused, too many requests")
            time.sleep(10)
        #if the webpage was not found, username isnt taken
        if r.status_code==404:
            print(">> Available: {}".format(name))
            file.write(name)
            file.write('\n')
    #outside of loop close file
    file.close()
    print("complete")



#Put user input into a function

def main():
    letters = [] #letter pool to generate usernames
    usernames = [] #usernames desired to search
    service = setUpSite(sys.argv[1])
    if len(sys.argv) == 3:
        usernames = scrapeList(sys.argv[2])
        print("Usernames collected")
    else:
        numCharacters = getNumChars()
        yn = int(input("Would you like to use all letters from the alphabet or choose a list of characters to generate username from?\nEnter 0 for A-Z, anything else to choose letters: "))
        if yn == 0:
            letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        else:
            end = False
            while end == False:
                userIn = input("Enter 0 to finish\nEnter your desired letters: ")
                letters.append(userIn.lower())
                if userIn == "0":
                    letters.pop()
                    break

        names = permutations(letters, numCharacters)#creating a tuple of permutated strings
        for name in list(names):
            _name = ''.join(name) #turning tuple into a string
            usernames.append(_name)
        print("Usernames generated")
    checkAvailability(usernames, service ,sys.argv[1].lower()) #fix lower to either site name



##Running the program
if __name__ == '__main__':
    main()
