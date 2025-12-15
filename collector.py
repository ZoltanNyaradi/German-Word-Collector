import os
import json

min_appearance = 1
# Sort out words with less appearance.
save_words = False
# Write -True- if you want to save the words in a file, -False- if not.
saving_file = "words"
# Name the file where you want to save the words.
test = True
# Enable test mode write -True- or -False-.
num_of_words_to_print = 1000
# Set how many words want you to print out to the screen.

#______________________________________________________________

def clear_content(content):
    """Clear non letter characters return words"""
    words_of_content=[]
    word = ""

    for char in content:
        if char.isalpha() or char=="'":
            word += char
        else:
            if len(word)>1:
                words_of_content.append(word)
            word = ""

    if((content[-1].isalpha() or content[-1]=="'") and len(word)>1):
        words_of_content.append(word)

    return words_of_content


def list_words(words_of_content, words):
    """Counts words and add up to the existing records"""
    for word in words_of_content:

        words.append(word)

    return words



def get_words(file, words):
    """
    Opens a file
    and add new induvidual words to the collection
    """
    with open(f"texts/{file}", "r", encoding="utf-8") as f:
        content = f.read()
        if content == "":
        	return words

        words_of_content = clear_content(content)

        words = list_words(words_of_content, words)

        return words

#______________________________________________________________

def count_words(sorted_words):
    """Count the words."""
    counted_words = []
    word_before = sorted_words[0]
    quantity = 0

    for word in sorted_words:
        if word == word_before:
            quantity += 1
        else:
            counted_words.append([word_before, quantity])
            word_before = word
            quantity = 1

    counted_words.append([word_before, quantity])

    return counted_words


#______________________________________________________________

def print_result(final_words, num_of_words_to_print):
    
    i = 0
    for word in final_words:
        print(f"{word[0]}: {word[1]}")
        i += 1
        if i==num_of_words_to_print:
            return

#______________________________________________________________


def delete_rare_words(min_appearance, sorted_counted_words):

    final_words=[]
    for word in sorted_counted_words:
        if word[1]>=min_appearance:
            final_words.append(word)
        else:
            return final_words

    return final_words

#______________________________________________________________

def save_words(final_words, saving_file):

    words=[]

    for word in final_words:
        words.append(word[0])

    with open(f"{saving_file}.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)


#______________________________________________________________

files = os.listdir("texts")
words = []

for file in files:
    if(test):
        if(file=="test.txt"):
            print(f"Processing {file}")
            words = get_words(file, words)
    else:
        if(file!="test.txt"):
            print(f"Processing {file}")
            words = get_words(file, words)

sorted_words = sorted(words)

counted_words = count_words(sorted_words)

sorted_counted_words = sorted(counted_words, key=lambda row: row[1], reverse=True)

if(min_appearance>1):
    final_words = delete_rare_words(min_appearance, sorted_counted_words)
else:
	final_words = sorted_counted_words

if(save_words):
    save_words(final_words, saving_file)

print_result(final_words, num_of_words_to_print)


