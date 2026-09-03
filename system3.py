name=input("Enter full name: ")
"Jedidiah Roberts"
sentence = input("Enter a sentence: ")
'Hello, I am in grade nine'
print ("My name is " + format(name) + " and I want to say: " + format(sentence))
sentence_search = input("Enter a word to search in the sentence: ")
'grade'
if sentence_search in sentence:
 print("The word " + sentence_search + " is in the sentence.")
sentence_length = len(sentence)
print("The length of the sentence is: " + str(sentence_length))
sentence_upper = sentence.upper()
print("The sentence in uppercase is: " + sentence_upper)
sentence_lower = sentence.lower()
print("The sentence in lowercase is: " + sentence_lower)
sentence_title = sentence.title()
print("The sentence in title case is: " + sentence_title)
sentence_split = sentence.split()
print("The sentence split into words is: " + str(sentence_split))