#this program says hello and asky for my name
import pyperclip,re

print('hello world')

print('what is your name?')

myName=input()
print('It is good to meet you' +myName)
print('The length of your name is: ')
print(len(myName))

print('what is your age?')
myAge=input()
print('You will be '+str(int(myAge) +1)+' in a year.')
