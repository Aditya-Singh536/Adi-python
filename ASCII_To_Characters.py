def printCharactersForGivenAsciiRange(start :str, end : str)-> None: 
    """
    Program to print all charachters for a given range of ASCII values.
    """
    if (start.isdigit() and end.isdigit()):
        start, end = min(int(start), int(end)), max(int(start), int(end))
        asciiCodes = [i for i in range(start, end + 1)]
        print(f"Ascii codes: {asciiCodes}")
        print(f"Folloing are the characters between {start} and {end}:")
        for ascii in asciiCodes:
            print(f"{ascii} ===> {chr(ascii)}")
    else:
        print("Wrong input: Please enter integer.")

if __name__ == '__main__':
    start = input("Give starting Ascii number: ")
    end = input("Give ending Ascii number: ") 
    printCharactersForGivenAsciiRange(start, end)
