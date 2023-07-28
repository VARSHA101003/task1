#python code for function called most_frequent that takes a string and prints the letters in decreasing order of frequency

def most_frequent(input_string):
    letter_frequency = {}
    for letter in input_string:
        if letter.isalpha():  
            letter = letter.lower()
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
    sorted_letters = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
    print("Letters in decreasing order of frequency:")
    for letter, frequency in sorted_letters:
        print(f"{letter}: {frequency}")
input_string = "mississippi"
most_frequent(input_string)

#output
i=4
s=4
p=2
m=1
