# this code will convert number name to number eg: "three hundred" to 300

def word_to_number(word):
    # Define number words and their corresponding values
    ones = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19
    }
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    scales = {
        "hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000
    }

    words = word.lower().replace('-', ' ').split()
    current = result = 0

    for w in words:
        if w in ones:
            current += ones[w]
        elif w in tens:
            current += tens[w]
        elif w in scales:
            current *= scales[w]
            result += current
            current = 0
        elif w == "and":
            continue
        else:
            raise ValueError("Invalid word: " + w)

    return result + current


# Example usage
number = input("Enter a Number Name: ")
print(word_to_number(number))
