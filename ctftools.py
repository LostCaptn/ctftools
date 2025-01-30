"""
Christian Nelson
22 Jan 2025
Convert binary octets into decimal
"""
import base64
import codecs
banner = r"""
_______________________________ ________                          .___            
\_   ___ \__    ___/\_   _____/ \______ \   ____   ____  ____   __| _/___________ 
/    \  \/ |    |    |    __)    |    |  \_/ __ \_/ ___\/  _ \ / __ |/ __ \_  __ \
\     \____|    |    |     \     |    `   \  ___/\  \__(  <_> ) /_/ \  ___/|  | \/
 \______  /|____|    \___  /    /_______  /\___  >\___  >____/\____ |\___  >__|   
        \/               \/             \/     \/     \/           \/    \/       by Christian Nelson
"""


def options():
    options = """
    Please choose from the follow:
    1. base32
    2. base64
    3. ipv4bin2dec
    4. Substitution Cipher
    5. Hexadecimal
    6. Rot(N)
    7. Exit
    """
    print(options)
    while True:
        option = input("Enter a number: ")
        if option == "1":
            base32main()
            break
        elif option == "2":
            base64main()
            break
        elif option == "3":
            ipv4decoder()
            break
        elif option == "4":
            subciphermain()
            break
        elif option == "5":
            hexmain()
            break
        elif option == "6":
            rotNmain()
            break
        elif option == "7":
            break
        else:
            print("I'm sorry, that option isn't available right now")
        return

def base64decoder(string):
    try:
        return base64.b64decode(string.encode('ascii')).decode('ascii')
    except Exception as e:
        return e

def base64encoder(string):
    try:
        return base64.b64encode(string.encode("ascii")).decode('ascii')
    except Exception as e:
        return e


def base64main():
    action = input("Choose an option: \n 1. Encode \n 2. Decode \n 3. Exit \n")
    if action == "1":
        string = input("Enter the string to encode: ")
        encoded = base64encoder(string)
        print(f"Encoded string: {encoded}")
        base64main()
    elif action == "2":
        string = input("Enter the string to decode: ")
        decoded = base64decoder(string)
        print(f"Decoded string: {decoded}")
        base64main()
    elif action == "3":
        print("Goodbye")
    else:
        print("I'm sorry, that's not a valid option.")
        base64main()

def base32decoder(string):
    try:
        return base64.b32decode(string).decode('ascii')

    except Exception as e:
        return e

def base32main():
    string = input("Enter a base32 string to decode: ")
    decoded = base32decoder(string)
    print(f"Decoded string: {decoded}")


def ipv4decoder():
    new_octet = octetfix() #assigns the output to a variable
    first_octet = convert2decimal(new_octet) #assigns variable to the output of new_octet being passed into converter
    print(first_octet)
    new_octet = octetfix()
    second_octet = convert2decimal(new_octet)
    print(second_octet)
    new_octet = octetfix()
    third_octet = convert2decimal(new_octet)
    print(third_octet)
    new_octet = octetfix()
    fourth_octet = convert2decimal(new_octet)
    print(fourth_octet)
    print(f"The IPV4 address is {first_octet}.{second_octet}.{third_octet}.{fourth_octet}")

def octetfix(): #validates the input
    while True:
        octet_str = input("Enter the octet: ")
        try:
            octettest = int(octet_str, 2) #verifies that the string can convert to binary
        except ValueError:
            print("That is not a binary number, please input only binary.")
        if len(octet_str) == 8: #verifies that the input is exactly 8 characters
            break
        else:
            print("That is not a valid octet")
    return octet_str #returns our input to pass on later

def convert2decimal(new_octet):
    new_dec = int(new_octet, 2) #converts the binary to decimal form using int()
    return new_dec #returns the input to pass on for printing

def subbruteforce(string):
    library = "abcdefghijklmnopqrstuvwxyz"
    library_upper = library.upper()
    counter = 0
    # while loop to increment x by 1 each iteration, to test all 25 possibilities
    try:
        while counter < 26:
            counter += 1
            shift = int(counter)
            result = ""
            # for loop to convert the letter in the input to a number
            for i in string:
                position = library.find(i) # sets the position of the desired letter by taking away the value of counter from the position
                new_letter = position - shift
                upper_position = library_upper.find(i)
                new_upper = upper_position - shift
                # if the character is contained in letters, then we add that letter to our decrypted string
                # by passing it the new position
                if i in library:
                    result = result + library[new_letter]
                elif i in library_upper:
                    result = result + library_upper[new_upper]
                else:
                    result = result + i # if the input character is not within letters, we add it to the string as normal
            if string == result:
                result = "Not a substitution cipher."
                print(result)
            else:
                print(f"You used a substitution of {shift}")
                print(f"Your decrypted message is: {result}")
    except Exception as e:
        print(e)

def subkeydecript(string):
    library = "abcdefghijklmnopqrstuvwxyz"
    library_upper = library.upper()
    try:
        while True:
            key = input("Enter a key: ")
            shift = int(key)
            result = ""
            for i in string:
                position = library.find(i)
                new_letter = position - shift
                upper_position = library_upper.find(i)
                new_upper = upper_position - shift
                if i in library:
                    result = result + library[new_letter]
                elif i in library_upper:
                    result = result + library_upper[new_upper]
                else:
                    result = result + i
            if string == result:
                result = "Not a substitution cipher."
                return result
            else:
                return key,result
    except Exception as e:
        return e

def subkeyencript(string):
    library = "abcdefghijklmnopqrstuvwxyz"
    library_upper = library.upper()
    try:
        while True:
            key = input("Enter a key: ")
            #string = string.lower()
            shift = int(key)
            result = ""
            # for loop to convert the letter in the input to a number
            for i in string:
                position = library.find(i)
                # sets the position of the desired letter by taking away the value of counter from the position
                new_letter = position + shift
                if new_letter > 25:
                    new_letter = new_letter % 26
                upper_position = library_upper.find(i)
                new_upper = upper_position + shift
                if new_upper > 25:
                    new_upper = new_upper % 26
                # if the character is contained in letters, then we add that letter to our decrypted string
                # by passing it the new position
                if i in library:
                    result = result + library[new_letter]
                # if the input character is not within letters, we add it to the string as normal
                elif i in library_upper:
                    result = result + library_upper[new_upper]
                else:
                    result = result + i
            if string == result:
                result = "Not a substitution cipher."
                return result
            else:
                return key,result
    except Exception as e:
        return e

def subciphermain():
    string = input("Enter the string: ")
    action = input("Enter a Number: \n 1. Encode \n 2. Decode \n 3. Brute Force \n 4. Exit \n Option: ")
    if action == "1":
        result = subkeyencript(string)
        print(f"Your encrypted message: {result}")
        subciphermain()
    elif action == "2":
        result = subkeydecript(string)
        print(f"Your decrypted message is: {result}")
        subciphermain()
    elif action == "3":
        subbruteforce(string)
        subciphermain()
    elif action == "4":
        print("Goodbye")
    else:
        print("I'm sorry, that's not a valid option.")
        subciphermain()

def hexvalidator():
    while True:
        hex_string = input("Enter a hexadecimal string: ")
        temp = hex_string
        hex_string = hex_string.replace(".", " ")
        hex_string = hex_string.replace(" ", "")
        hex_string = hex_string.lower()
        try:
            hextest = int(hex_string, 16) #verifies that the string can convert to hex
            hex_string = temp
            break
        except ValueError:
            print("That is not a hex number, please input only hex.")
    return hex_string  # returns our input to pass on later

def hex2dec(new_hex):
    library = "0123456789abcdef"
    dec_string = ""
    hex_string = new_hex
    print("You enter: ", hex_string)
    temp = ""
    for i in hex_string:
        if i in library:
            temp = temp + i
            hex_string = hex_string.replace(i, "", 1)
        if i not in library:
            temp = int(temp, 16)
            dec_string = dec_string + str(temp)
            dec_string = dec_string + i
            temp = ""
            hex_string = hex_string.replace(" ", "", 1)
            hex_string = hex_string.replace(".", "", 1)
        if hex_string == "":
            temp = int(temp, 16)
            dec_string = dec_string + str(temp)

    return dec_string

def hex2ascii(new_hex):
    library = "0123456789abcdef"
    dec_string = ""
    hex_string = new_hex
    hex_string = hex_string.replace(".", " ")
    print(hex_string)  # checker
    temp = ""
    for i in hex_string:
        if i in library:
            temp = temp + i
            hex_string = hex_string.replace(i, "", 1)
        if i not in library:
            temp = chr(int(temp, 16))
            dec_string = dec_string + str(temp)
            temp = ""
            hex_string = hex_string.replace(" ", "", 1)
        if hex_string == "":
            temp = chr(int(temp, 16))
            dec_string = dec_string + str(temp)
            break
    return dec_string


def hexmain():
    print("Choose from the following options:\n 1. Hex to Decimal\n 2. Hex to ASCII\n")
    option = input("Enter a number: ")
    if option == "1":
        new_hex = hexvalidator()
        dec_string = hex2dec(new_hex)
        print("Hex value in decimal: ", dec_string)
    elif option == "2":
        new_hex = hexvalidator()
        ascii_string = hex2ascii(new_hex)
        print("Hex value in ASCII: ", ascii_string)

def rot13Decode(string):
    try:
        return codecs.encode(string, 'rot13')
    except Exception as e:
        return f"Invalid Input: {e}"

def rot13main():
    string = input("Enter a string to encode/decode: ")
    result = rot13Decode(string)
    print(f"Your message is: {result}")

def rot47Decode(string):
    try:
        x = []
        for i in range(len(string)):  # access characters by index
            j = ord(string[i])  # set j to the corresponding ordinal number
            if j >= 33 and j <= 126:  # checks for ROT47 range
                # decode left 47, account for negative 33, wrap %94
                x.append(chr(33 + ((j - 47 - 33) % 94)))
            else:
                x.append(string[i])  #adds non ROT47 characters without changes
        return ''.join(x)  # turns the list into a string

    except Exception as e:
        return f"Exception: {e}"

def rot47main():
    string = input("Enter a ROT47 string: ")
    result = rot47Decode(string)
    print(f"Your message is: {result}")

def rotNmain():
    print("""
    Please select from the following ROT Ciphers:
    1. ROT13
    2. ROT47
    3. Exit
    """)
    while True:
        choice = input("Enter a number:")
        if choice == "1":
            rot13main()
        elif choice == "2":
            rot47main()
        elif choice == "3":
            break
        else:
            print("That is not a valid response")

def uestools():
    while True:
        user_continue = input("Would you like to continue? Y/n: ")
        if user_continue == "Y" or "y":
            options()
        elif user_continue == "n":
            break
        else:
            print("Invalid option")


print(banner)
options()
uestools()


