#Concept = String Creation

#single_quote = 'Hello'
#double_quote = "World"
#triple_quote = """Multi-line-string"""

#Concept = String Indexing and Slicing

text = "Python Programming"

print(text[0])   #first character
print(text[-1])  #last character
print(text[0-6]) #slice 0 to 5
print(text[:6])  #from start to 5
print(text[7:])  #7 to end

#Concept = String Methods

name = "Spongebob Squarepants"

print(len(name))  #Length
print(name.strip()) #Remove Whitespace
print(name.upper()) #Uppercase
print(name.lower()) #Lowercase
print(name.title()) #Title case
print(name.replace("Spongebob", "Patrick")) #Replace

#Concept = String Formatting

name = "Sapnaa Vijayakumar"
age = 24

message_1 = f"My name is {name} and I am {age} years old"            #f-strings
message_2 = "My name is {} and I am {} years old".format(name, age)  #str.format() 
message_3 = "My name is %s and I am %d years old" % (name,age)       #%-formatting

print(message_1)
print(message_2)
print(message_3)

#Concept = String Manipulation

the_text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

total_words = the_text.split() #Split the text into a list of words
word_count = len(total_words) #Count the items in the list

print(word_count)

