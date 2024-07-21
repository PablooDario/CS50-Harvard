import emoji

userInput = input("Input: ").strip()
print("Output: ", emoji.emojize(userInput, language='alias'))