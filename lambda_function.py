def run():

palindrome = lambda string: string == string[::-1]

print(palindrome("ana"))


#Cómo se haría con fuciones normales?:

def palindrome(string):
    return string == string[::-1]

print(palindrome("ana"))

if __name__ == "__main__":
    run() 