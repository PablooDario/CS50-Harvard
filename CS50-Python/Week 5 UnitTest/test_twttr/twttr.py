def main():
    user = input("Input: ")
    user = shorten(user)
    print("Output:", user)

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for w in word:
        if w in vowels:
            word = word.replace(w, '')
    return word

if __name__ == "__main__":
    main()