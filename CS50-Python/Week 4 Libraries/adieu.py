# Inflect Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words.
import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        #ask the names for the user
        try:
            names.append(input("Name: "))
        #Stop when the user writes ctrl+d
        except EOFError:
            break
    if len(names) > 0:
        adieu(names)

def adieu(names):
    #Print the names correctly spell (comas & and)
    goodbye = "\nAdieu, adieu, to "
    print(goodbye + p.join(names))

main()