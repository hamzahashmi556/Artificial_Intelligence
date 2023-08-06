import re


def checkPalindrome(inputString):
    # Remove punctuation and convert to lowercase
    inputString = re.sub(r'[^\w\s]', '', inputString).lower()

    # Get the Start & End Index of Comparison
    startIndex = 0
    endIndex = len(inputString) - 1

    isMatchingLetter = True  # First And Last Index Letter Match = True, Else False
    # First Check if the String is Empty
    if len(inputString) == 0:
        return True
    else:
        # Compare Until reach to middle character of string
        while startIndex != endIndex and isMatchingLetter:
            leftLetter = inputString[startIndex]
            rightLetter = inputString[endIndex]

            # Ignore White Spaces
            while leftLetter == " ":
                startIndex += 1
                leftLetter = inputString[startIndex]
            while rightLetter == " ":
                endIndex -= 1
                rightLetter = inputString[endIndex]

            # if Index at Middle Break
            if startIndex == endIndex:
                break
            # if comparison is true keep comparing to middle character
            elif leftLetter == rightLetter:
                startIndex += 1
                endIndex -= 1
            # else break the loop and return false
            else:
                isMatchingLetter = False
                break
        return isMatchingLetter


if __name__ == '__main__':
    # Test Cases
    inputs = ["level", "", "a", "hello", "a man a plan a canal panama", "Able was I, ere I saw Elba!", "12321"]

    # for input in inputs:
    #     isPalindrome = checkPalindrome(input)
    #     if isPalindrome:
    #         print(f"'{input}' is Palindrome")
    #     else:
    #         print(f"'{input}' is not Palindrome")
