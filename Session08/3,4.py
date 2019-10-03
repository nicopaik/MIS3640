#Exercise 3 , 4 , 5
#https://blackboard.babson.edu/bbcswebdav/pid-1085612-dt-content-rid-3547571_1/courses/2019Fall-MIS3640-01/notebooks/Strings.html

#3 
#Split
# text= 'This example sentence'

# # splits at space
# print(text.split("e"))

# text= "This is an example sentence"
# print(text.split(" ", 2)) #Splits number of times

# #strip
# text= 'eeseee This example sentence'
# print(text.strip("e")) #Gets rid of leading and trailing chars

# #replace 
# text= "New Text"
# print(text.replace("New","Old")) 

# text= "New New New Text"
# print(text.replace("New","Old", 2)) #2 Chooses the number of times it can replace


#4.1 cheap is $33, free is $34 !
# 1. You walk into a store where each item is priced according to the letters in its name: 
# 'a' costs $1, 'b' is $2, and so on. 
# Write a program that prints a receipt for this wacky store:
final_value = 0 #final value holder
words = 'bananas,rice,paprika,potato chips'#words

for word in words.split(','): #word = each word separated by commas
  for letter in word: #from each word taking each letter
    value = ord(letter) - 96 #ord("a") = 97 so -96 a=1
    final_value += value #adds all the values of each word in the loop
print(final_value)

