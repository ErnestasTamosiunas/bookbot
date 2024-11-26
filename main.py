import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        sortedCharacters = sortCharacters(countAlphabetChars(file_contents))

        # Report sorted by the highest count of each letter used!
        print("--- Begin report of books/frankensteins.txt ---")
        print(f"{countWords(file_contents)} words found in the document! \n")

        for character in sortedCharacters:
            print(f"The '{character["char"]}' character was found {character["count"]} times")
        print("--- End report ---")

def countWords(file):
    return len(file.split())

def countAlphabetChars(file):
    characters = {}
    
    for char in file.lower():
        if char in string.ascii_lowercase:
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1
    return characters

def sortCharacters(dict):
    characters = []
    for key in dict:
        characters.append({
            "char": key,
            "count": dict[key] 
        })
    characters.sort(reverse=True, key=sortOn)
    return characters

def sortOn(dict):
    return dict["count"]

main()
