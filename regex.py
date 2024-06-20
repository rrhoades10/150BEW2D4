'''
1. **Dot (.)**
    - The wildcard: Matches any single character except newline (`\n`).
    - Imagine it as a shape-shifter, able to become any character you need, just for a moment.
2. **Caret (^)**
    - The anchor for the start of a string.
    - Like a sentinel, standing guard at the beginning of your text.
3. **Dollar ($)**
    - The anchor for the end of a string.
    - The sentinel at the gates, ensuring nothing goes beyond the end of your text.
4. **Asterisk (*)**
    - Matches zero or more occurrences of the pattern left to it.
    - Think of it as a multiplier, creating copies of the character before it.
5. **Plus (+)**
    - Matches one or more occurrences of the pattern left to it.
    - Similar to the asterisk, but insists on at least one occurrence.
6. **Question Mark (?)**
    - It makes the preceding character optional.
    - It's the symbol of uncertainty, allowing flexibility in your patterns.
7. **Backslash (\)**
    - Escapes special characters or signals a special sequence.
    - The key to differentiating between a literal character and a magical symbol.
8. **Square Brackets ([])**
    - A set of characters. Matches any one character in the brackets.
    - Like choosing one tool from a toolbox, it selects one character from a set.
9. **Pipe (|)**
    - The OR operator. It matches either the pattern before or after it.
    - A fork in the road, giving you a choice between paths.
10. **Parentheses (())**
    - Groups patterns together and captures them.
    - Think of them as binding a spell, containing its power within.
11. **Curly Braces ({})**
    - Curly braces are used to define the exact number of times a character or a pattern must occur for a match to be found.
    - It's like telling your magic spell exactly how much power to use.
'''
### **Simple Exercises for Understanding**


'''
1.  **Dot (.) - The Wildcard Character**
    - **Task**: Find any three-character sequence in a text, where the middle character can be anything, the first has to be ‘c’ and the last has to be ‘t’.
    - **Regex Pattern**: `c.t`
    - **Test Sentence**: "I found a cat, a cot, and a cut in the room and the cat was cute, ctt cct coot colt"
    - **Expected Matches**: `['cat', 'cot', 'cut', cat, cut]`
    - **Explanation**: The dot `.` matches any single character (except newline), so it finds sequences where 'c' and 't' are separated by any character.
2. **Caret (^) - The Beginning Anchor**
    - **Task**: Find strings that start with 'Py'.
    - **Regex Pattern**: `^Py`
    - **Test Sentence**: "Python is fun"
    - **Expected Matches**: `[’Py’]` from 'Python' at the beginning of the sentence.
    - **Explanation**: The caret `^` ensures that the match must occur at the start of the string or line.
3. **Dollar ($) - The End Anchor**
    - **Task**: Identify strings that end with 'fun'.
    - **Regex Pattern**: `fun$`
    - **Test Sentence**: "Learning regex is fun"
    - **Expected Matches**: `['fun']` from 'Learning regex is fun.'
    - **Explanation**: The dollar `$` ensures that 'fun' is matched only if it's at the end of the string or line.
4. **Asterisk (*) - Zero or More Occurrences**
    - **Task**: Match a character followed by zero or more 'a's.
    - **Regex Pattern**: `ba*`
    - **Test Sentence**: "I saw a bat, and a ball in my bed, baaah!"
    - **Expected Matches**: `['ba', 'ba', 'b', 'baaa']` from ‘bat’, ‘ball’, ‘bed’, and ‘baaah!’.
    - **Explanation**: The pattern starts with the literal character 'b'. This means it will first look for occurrences of 'b' in the text. Following the 'b', we have 'a*'. Then, the asterisk  `*` which matches zero or more occurrences of the preceding character ('a' in this case).
5. **Plus (+) - One or More Occurrences**
    - **Task**: Find a character followed by one or more 'a's.
    - **Regex Pattern**: `ba+`
    - **Test Sentence**: "The battle of ba and baat."
    - **Expected Matches**: `['ba', 'ba', 'baa']` from ‘battle’, ‘ba’, and ‘baat’.
    - **Explanation**: The plus `+` matches one or more occurrences of the preceding character ('a' in this case).
6. **Question Mark (?) - Zero or One Occurrence**
    - **Task**: Match 'colour' or 'color'.
    - **Regex Pattern**: `colou?r`
    - **Test Sentence**: "The color is nice. I like this colour."
    - **Expected Matches**: `['color', 'colour']`
    - **Explanation**: The question mark `?` makes the preceding character ('u' in this case) optional.
7. **Backslash (\) - Escaping Special Characters**
    - **Task**: Match a period character in a sentence.
    - **Regex Pattern**: **`\.`**
    - **Test Sentence**: "End of sentence. Start of a new one."
    - **Expected Matches**: The periods `[.]` at the end of 'sentence.' and before 'Start'.
    - **Explanation**: In regex, the period (.) is a special character used as a wildcard. To match an actual period, the backslash **`\`** is used to escape the special meaning of the period, treating it as a literal character. The pattern **`\.`** specifically looks for the period character in the text.
8. **Square Brackets ([]) - Character Sets**
    - **Task**: Find all vowels in a word.
    - **Regex Pattern**: `[aeiou]`
    - **Another Pattern**: `[A-Za-z+]` - 
    - **Test Word**: "Regular"
    - **Expected Matches**: `['e', 'u', 'a']`
    - **Explanation**: The square brackets `[]` define a set of characters, any of which can be matched.
9. **Pipe (|) - The OR Operator**
    - **Task**: Match 'cat' or 'dog'.
    - **Regex Pattern**: `cat|dog`
    - **Test Sentence**: "I have a cat and a dog."
    - **Expected Matches**: `['cat', 'dog']`
    - **Explanation**: The pipe `|` acts as an OR operator, matching either the pattern before or after it.
10. **Parentheses (()) - Grouping**
    - **Task**: Find repetitions of 'woof' or 'meow'.
    - **Regex Pattern**: `(woof|meow)+`
    - **Test Sentence**: "The pets say woof woof and meow."
    - **Expected Matches**: `['woof’,  'woof', 'meow']`
    - **Explanation**: Parentheses `()` group patterns, allowing the plus `+` to apply to the entire group.
11. **Curly Braces ({}) - Specifying Exact Occurrences**
    - **Task**: Match a word where 'l' is followed by exactly two 'o's.
    - **Regex Pattern**: **`lo{2}`**
    - **Regex Pattern**: **`[L|lo{2}]`**
    - **Regex Pattern**: **`[A-Z|a-zo{2}]`**
    - **Test Sentence**: "Look at the loom and the balloon in the room, loser."
    - **Expected Matches**: ['loo', 'loo']
    - **Explanation**: The pattern **`lo{2}`** searches for an 'l' followed by exactly two 'o's. In our test sentence, it successfully identifies 'loo' within the words 'loom' and 'balloon', demonstrating the ability of curly braces **`{}`** to specify an exact number of occurrences.

'''

"""1. **\d - The Digit Hunter**
    - Hunts down digits (0-9) in your text.
    - It's like a metal detector that beeps only when it finds numbers.
2. **\w - The Word Wizard**
    - Finds word characters (letters, digits, and underscores).
    - Imagine it as a magnet that attracts only words and numbers, leaving everything else behind.
3. **\s - The Space Scout**
    - Seeks out whitespace (spaces, tabs, newlines).
    - Think of it as a radar that pings whenever it detects open space in your text.

### **Putting Special Sequences to the Test**

1. **The Digit Hunter in Action**:
    - **Task**: Extract all phone numbers from a text for a phone number in the format 'XXX-XXX-XXXX', where each 'X' is a digit
    - **Regex Pattern**: `\d{3}-\d{3}-\d{4}`
    - **Test Sentence**: "Call me at 123-456-7890 or 987-654-3210."
    - **Expected Matches**: `['123-456-7890', '987-654-3210']`
    - **Explanation**: The `\d` sequence finds digits, and `{3}` specifies exactly three digits. The hyphen `-` is a literal character, It separates different segments of the phone number. Overall, this pattern searches for sequences like a U.S. standard phone number format.
2. **The Word Wizard’s Spell**:
    - **Task**: Identify words containing numbers.
    - **Regex Pattern**: `\w+\d+\w*`
    - **Test Sentence**: "My username is user123 and my password is pass99word. my really cool username is Rhoadehouse10 fhosdhflsjdhfljsdhf"
    - **Expected Matches**: `['user123', 'pass99word', "Rhoadehouse]`
    - **Explanation**: `\w*` matches any word character zero or more times, and `\d` ensures there's at least one digit. This pattern finds words mixed with numbers.
3. **The Space Scout’s Exploration**:
    - **Task**: Split a sentence into words.
    - **Regex Pattern**: `\s+`
    - **Test Sentence**: "Welcome to the world of        regex!"
    - **Expected Matches**: The spaces between ' ', ' ', ' ', ' ', '        '’
    - **Explanation**: `\s+` matches one or more whitespace characters. It does not match the characters of the words themselves but the empty space that separates them, allowing us to see where one-word ends and another begins.

### **More Special Sequences**

1. **\D - The Non-Digit Detector**
    - Finds any character that is not a digit.
    - Like a filter that lets everything but coins pass through.
2. **\W - The Non-Word Character Identifier**
    - Matches any character that is not a word character (opposite of \w).
    - Imagine it as a tool that highlights everything in the text that isn't a word or number.
3. **\S - The Non-Whitespace Finder**
    - Identifies any character that is not a whitespace.
    - It's like a spotlight that ignores spaces and shines on everything else.
4. **\b - The Word Boundary Beacon** " as."
    pattern = "\b[as]\b
    - A marker for the positions between a word and a non-word character.
    - Think of it as a flare that lights up the borders of each word.
5. **\B - The Non-Word Boundary Signal**
    - Matches positions where a word boundary does not occur.
    - It’s the silent guardian that watches over continuous strings of word characters without interruption.
6. **\A - The Beginning Sentinel**
    - Matches only at the start of the string.
    - It’s like a gatekeeper that only allows patterns that appear right at the opening of your text.
7. **\Z - The End Guardian**
    - Matches only at the end of the string, before the final newline, if one exists.
    - Think of it as the final checkpoint at the very end of your textual journey.

    """

import re # import the regular expression module - this only needs to be done one time
# gives us access to searching and matchign patterns within a string

# wayys to match patterns within a string
# re.findall(r"pattern", "string we're searching through") - return all non-overlapping matches of a pattern in a string - returns a list of matches
# re.search(r"pattern", "string we're searching through") - scan through the entirety of a string, looking for the first occurrence of the pattern - returns a match object
# "my email is ryanr@codingtemple.com"
# re.match(r"pattern", "string we're searching through") - only checks the start of the string - returns a match object
# "ryanr@codingtemple.com"
# re.split() - split a string by pattern occurrences
# re.sub() - replace occurences of a pattern with a replcement string
# re.compile() - compiles our pattern into a regex object, makes matching a bit more efficient


# METACHARACTERS
# . - wildcard - matches any single character except newline
sentence = "I found a cat, a cot, and a cut in the room in connecticut"
# find all words that start with a c and end with a t, with a single character between them
ct_words = re.findall(r"c.t", sentence)
print(ct_words) # ["cat", "cot", "cut"]

# re.search() - returns the first match 
# cat
ct_words = re.search(r"c.t", sentence)
# ct_words - match object
print(ct_words)
# <re.Match object; span=(10, 13), match='cat'>
# span - index range of the match
# accessing the matched word from the string - use .group()
print(ct_words.group())

# ^ - mark the start of a string - matches if whatever we're looking for is the first thing in the string
carret_pattern = r"^Py"
sentence = "Python is fun. I love Python"
matched_words = re.findall(carret_pattern, sentence)
print(matched_words) # ["Py"]

# $ - opposite of the carret - mark the end of the string
#                    not this guy                         matches this guy
my_sentence = "It is fun to learn python. Learning Regex is fun"
matched_words = re.findall(r"fun$", my_sentence)
print(matched_words)

# * 0 to many occurrences
# a b followed by 0 or many a's
pattern = re.compile(r"ba*")
my_sentence = "baaaa baaaaaa black sheep, have you any wool. barber baby bubble and a bumble bee"
matched_words = re.findall(pattern, my_sentence)
print(matched_words)

# + 1 or more occurrences 
pattern = re.compile(r"ba+") #searching for b followed by at least 1 a
my_sentence = "The battle of ba and baat it was bad and bitter"
matched_words = re.findall(pattern, my_sentence)
print(matched_words)

# ? optional occurence - 1 or 0
my_sentence = "If you're American you say color and if you're European you say colour"
pattern = re.compile(r"colou?r")
matched_words = re.findall(pattern, my_sentence)
print(matched_words)

# sets []
word = "Regular"
pattern = re.compile(r"[aeiou]") #looking for individual instances of each vowel in the word
# pattern = r"[aeiou]"
matched_letters = re.findall(pattern, word)
print(matched_letters)
print(pattern)

# | or - we can look for this or this or this
my_sentence = "I have a cat and a dog"
pattern = re.compile(r"cat|dog")
# looking for cat or dog in our sentence
matched_words = re.findall(pattern, my_sentence)
print(matched_words) #['cat', 'dog']

# () - groups - repitions of patterns
my_sentence = "The pets say woofwoof and meow"
pattern = re.compile(r"woof|meow")
matched_words = re.findall(pattern, my_sentence)
print(matched_words)

# {} - setting a number of occurrences of a range of occurrences
# {2} - something happening exactly 2 times
# {2,} - at least two times
# {2, 6} - between 2 and 6 times
my_sentence = "Look at the loom and the balloooooooon in the room lololol"
pattern = re.compile(r"lo{2,4}") #l followed by 2 o's
matched_words = re.findall(pattern, my_sentence)
print(matched_words)

# Special Sequence Characters
# \b - match word boundaries between word characters and non word characters
# a word character surrounded by non-word charactesr, spaces or special characters
# letters surrounded by spaces or special charactesr like !@#$%%^^^&%^*&
# \B - match word boundaries between two word characters
# letters surrounded by letters or digits
my_sentence = "black cat tomcat certificate catfish"
pattern = re.compile(r"cat\b")
matched_words = re.findall(pattern, my_sentence)
print(matched_words) # []'cat']
# "black\bcat\btomcat certifciate catfish"

# \d - matches any number character or digit
my_sentence = "Please call me at Ryan 123-456-7890 or Skylar 987-654-3210 456-789-3154"
pattern = re.compile(r"[A-z]+\s(\d{3}-\d{3}-\d{4})")
matched_words = re.findall(pattern, my_sentence)
print(matched_words)

# using sets to find a phone number
phone_pattern = re.compile(r"[0-9]{3}-[0-9]{3}-[0-9]{4}")
matched_numbers = re.findall(phone_pattern, my_sentence)
print(matched_numbers)

# using metacharacters and special sequence all together to match patterns within a string
# finding an email within a string
# ryanr@codingtemple.com
# ryan_rhoades@gmail.com
# cool-guy-420@gmail.com
text = "Contact us at support@example.org or sales_team@gmail.com ryanr@codingtemple.com ryan_rhoades@gmail.com cool-guy-420@gmail.com"
#                          username         domain
pattern = re.compile(r"[A-Za-z0-9._%!$+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
#                                                        escaping the . so its NOT read as wildcard
found_emails = re.findall(pattern, text)
print(found_emails)

# checking individual emails match - checking at the start of the string
email = "@codingtemple.com ryanr@codingtemple.com"
# this immediately returns none
pattern = re.compile(r"[A-Za-z0-9._%!$+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# re.match() - check at the start of the string and ONLY return a match object if everything in that string matches the pattern

if re.match(pattern, email):
    print("That is a valid email")
else:
    print("That email is invalid")

matched = re.match(pattern, email) # setting a match object to a variable
print(matched)

# validating a user input email
contact_dictionary = {}
# email = input("Please enter your email: ")

if re.match(pattern, email):
    print("That is a valid email")
    contact_dictionary[email] = {"name": "Ryan"}
else:
    print("That email is invalid")
print(contact_dictionary)



email = "@codingtemple.com ryanr@codingtemple.com"
# keep searching even if the first part of the string isnt a match
pattern = re.compile(r"[A-Za-z0-9._%!$+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# re.search() serach the entirety of the string and return the first instance of a match

matched = re.search(pattern, email)
if matched:
    print("That is a valid email")
    print(matched)

else:
    print("That email is invalid")


# find hashtags in a post on twitter
post = "Boy do i love #Regex and learning #Python also #yolo"
hashtags = re.findall(r"#\w+", post)
print(hashtags)
# \w - match any word character A-Za-z 0-9

# re.search() - finds the first occurrence of a pattern in a string - search the entire string
text = "Contact us at support@example.org or sales_team@gmail.com ryanr@codingtemple.com ryan_rhoades@gmail.com cool-guy-420@gmail.com"
pattern = re.compile(r"[A-Za-z0-9._%!$+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
found_email = re.search(pattern, text)
print(found_email)
print(found_email.group()) #match.group() return the matched string
# group() can take a number as an argument which will determine which matched group to return
# group(0) - the first matched group

text = "Contact us at 630-852-8209"
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(f"Phone number found: {match.group()}")

# extracting dates
# \b - most matches will work without the boundary but its a nice way to be sure
sentence = "The event was held on 20/06/2024"
match = re.search(r"\b\d{4}\b", sentence)
if match:
    print(f"Year extracted: {match.group()}")

# re.match() - checks the start of the string - if no match is immediately found - returns None
text = "World! Hello"
if re.match(r"^Hello", text):
    print("The string starts with Hello!")
else:
    print("The string does not start with Hello")

if re.search(r"^Hello", text):
    print("The string starts with Hello!")
else:
    print("The string does not start with Hello")


# matching a username
# \w is any word character
username = "rhoadehouse"
if re.match(r"@\w+", username):
    print("That is a valid username")
else:
    print("That is not a valid username")

# re.split("pattern")
text = "Python,Regex;Splitting-Example. Fun, right?"
words = re.split(r"[,;.\s\?]+", text)
print(words)

sentence = "Hello! I hope you're having a great day. Please, please stay hydrated."
words = re.split(r"[!,;.\s\?]+", sentence)
print(words)


# splitting with non word characters
# \W any non word character
sentence = "Hello, world! Welcome to Python."
parts = re.split(r"\W+", sentence)
print(parts)


# re.sub() - replaces pieces of a string based on a pattern
phone = "Phone: +1 (123) 456-8790"
standard_phone = re.sub(r"\D", "", phone)
print(standard_phone)

# cleaning html by removing the tags
html = "<p>This is <em>HTML</em> content!</p>"
clean_text = re.sub(r"<.*?>", "", html)
# ? 0 or 1
print(clean_text)

# reformatting dates with re.sub()
date_string = "Today's date is 20/06/2024"
#                                                      references each matched group
formatted_date = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2-\1-\3", date_string)
#                             1       2       3
print(formatted_date)

# regex with loops - validating information in a list
emails = ["ryanr@codingtemple.com", " @gmail.com", "avnick89@gmail.com", "coolperson@gmail.com", "invalidgmail.com", "megaman@gmail.com"]

def validate_emails(emails):
    pattern = re.compile(r"[A-Za-z0-9._%!$+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    valid_emails = []
    invalid_emails = []
    for email in emails:
        if re.match(pattern, email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    return valid_emails, invalid_emails #returns a tuple with our two email lists
# unpacks the tuple and assigns each list to a relevant variable
valid_emails, invalid_emails = validate_emails(emails)
print(valid_emails)
print(invalid_emails)

# re.sub() uncensor some words
def replace_censored_words(text):
    censored_words = {"Python": "*$@!#$@#%", "regex": "!#@%*^#@"}
    for word, censor in censored_words.items():
        text = re.sub(word, censor, text)
    return text

original_text = "Learning Python is great, regex is the devil"
censored_text = replace_censored_words(original_text)
print(censored_text)


