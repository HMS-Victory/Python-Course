import re,pyperclip

#it takes a lot of code to analyze text properly
# this is how you would do it without methods
def isPhoneNumber(text): #415-555-
    if len(text) !=12:
        return False #Not phone number sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] !='-':
        return False #missin dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7] != '-':
        return False #missing sedond dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #missing las 4 digits
    return True

#message='Call me 415-555-1011 tomottow, or at 415-555-9999 for my office line'
#foundNumber=False
#for i in range(len(message)):
#    chunk=message[i:i+12]
#    if isPhoneNumber(chunk):
#        print('Phone number found: '+chunk)
#        foundNumber=True
#if not foundNumber:
#    print('could not find any phone numbers.')

#code with methods

import re

#message='Call me 415-555-1011 tomottow, or at 415-555-9999 for my office line'
# '\d' is looking for digits numeric '-' represents a '-'.
#phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#find one
#mo=phoneNumRegex.search(message)
#find all
#mo=phoneNumRegex.findall(message)
#print(mo.group())

# '()' mark out groups
#phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo=phoneNumRegex.search('My number is 412-323-5544')
#returns the first group defined above '(\d\d\d)'
#mo.group(1)


#
#batRegex=re.compile(r'Bat|man|mobile|copter|bat')
#mo=batRegex.search('Batmobile lost a wheel')
#mo.group()


#match a specific number of repetitions
#'?' means the wo group needs to appear in the group 0 or 1 times to match.
batRegex=re.compile(r'Bat(wo)?man')
#recognizes batman
#mo=batRegex.search('The Adventures of Batman')
#mo.group()

#same expression recognizes bat woman
#mo=batRegex.search('The Adventures of Batwoman')
#mo.group()

#this fails because '?' expects 0 or 1 repetitions of 'wo'
#mo=batRegex.search('The adventures of Batwowowowoman')
#mo==None #returns true

#says the area code is optional
#phoneRegex=re.compile(r'(\d\d\d)-?\d\d\d-\d\d\d\d')


# '*' same as '?' except that a group must appear 0 or more times
#batRegex=re.compile(r'Bat(wo)*man')
#evaluatues true because '*'
#mo=batRegex.search('The adventures of Batwowowowoman')


# '+' same as '*' but the group must appear 1 ot more times
#batRegex=re.compile(r'Bat(wo)+man')
#only evaluates true for Batwoman or Batwowoman
# batRegex.search('adventures of Batman')


#checks for each of these characters specifically
#regex=re.compile(r'\+\*\?')


#must repeat 3 times in the string
#haRegex=re.compile(r(Ha)(3))
#haRegex.search('He said HaHaHa')


#checks to see if between 3 and 5 digits are in a string
#greedy
#digitRegex=re.compile(r'(\d) {3,5}')
#non greedy
#digitRegex=re.compile(r'(\d) {3,5}?')


#we can make our own regex characters
#if any of these match returns true
vowelRegex=re.compile(r'[aeiouAEIOU]')
#'^' could be added to the previous piece of code to act as a not operator
#so to collect anything that does not match the following vowels.










