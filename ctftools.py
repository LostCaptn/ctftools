"""
Christian Nelson
22 Jan 2025
Common CTF Cipher Decoder
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
    menu = """
    Please choose from the follow:
    1. base32
    2. base64
    3. ipv4bin2dec
    4. Substitution Cipher
    5. Hexadecimal
    6. Rot(N)
    7. Brute Forcer (Will try every cipher)
    8. Exit
    """
    while True:
        print(menu)
        action = input("Enter a number: ")
        if action == "1":
            base32main()
            break
        elif action == "2":
            base64main()
            break
        elif action == "3":
            ipv4decoder()
            break
        elif action == "4":
            subciphermain()
            break
        elif action == "5":
            hexmain()
            break
        elif action == "6":
            rot_n_main()
            break
        elif action == "7":
            bruteforcermain()
        elif action == "8":
            return
        else:
            print("I'm sorry, that option isn't available right now")
    uestools()



#---------------------------------------------DECODERS---------------------------------------------------------------

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

def base32decoder(string):
    try:
        return base64.b32decode(string.encode('ascii')).decode('ascii')
    except Exception as e:
        return e

def subbruteforce(string):
    library = "abcdefghijklmnopqrstuvwxyz"
    library_upper = library.upper()
    counter = 0
    # while loop to increment x by 1 each iteration, to test all 25 possibilities
    try:
        while counter < 25:
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
                return
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

def hex2ascii(string):
    library = "0123456789abcdef"
    dec_string = ""
    hex_string = string
    hex_string = hex_string.replace(".", " ")
    temp = ""
    try:
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
    except Exception as e:
        return e

def hex2dec(string):
    library = "0123456789abcdef"
    dec_string = ""
    hex_string = string
    temp = ""
    try:
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
    except Exception as e:
        return e

def rot13decode(string):
    try:
        return codecs.encode(string, 'rot13')
    except Exception as e:
        return f"Invalid Input: {e}"

def rot47decode(string):
    try:
        x = []
        for i in range(len(string)):  # access characters by index
            j = ord(string[i])  # set j to the corresponding ordinal number
            if 33 <= j <= 126:  # checks for ROT47 range
                # decode left 47, account for negative 33, wrap %94
                x.append(chr(33 + ((j - 47 - 33) % 94)))
            else:
                x.append(string[i])  #adds non ROT47 characters without changes
        return ''.join(x)  # turns the list into a string
    except Exception as e:
        return e

#--------------------------------------------------VALIDATORS----------------------------------------------------------

def octetvalidator(): #validates the input
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


#--------------------------------------------------MAIN FUNCTIONS_______________________________________________________
def bruteforcermain():
    string = input("Enter a string to be tested: ")
    result = base32decoder(string)
    print(f"Base32: {result}")
    result = base64decoder(string)
    print(f"Base64: {result}")
    result = rot13decode(string)
    print(f"ROT13: {result}")
    result = rot47decode(string)
    print(f"ROT47: {result}")
    result = hex2dec(string)
    print(f"Hex2dec: {result}")
    result = hex2ascii(string)
    print(f"Hex2ASCII: {result}")
    while True:
        action = input("Would you like to view the substitution brute force? Y/n: ")
        if action in ["Y" , "y"]:
            subbruteforce(string)
            break
        elif action == "n":
            break
        else:
            print("That's not a valid option")
    return

def base32main():
    while True:
        string = input("Enter a base32 string to decode: ")
        decoded = base32decoder(string)
        print(f"Decoded string: {decoded}")
        return

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

def ipv4decoder():
    new_octet = octetvalidator() #assigns the output to a variable
    first_octet = convert2decimal(new_octet) #assigns variable to the output of new_octet being passed into converter
    print(first_octet)
    new_octet = octetvalidator()
    second_octet = convert2decimal(new_octet)
    print(second_octet)
    new_octet = octetvalidator()
    third_octet = convert2decimal(new_octet)
    print(third_octet)
    new_octet = octetvalidator()
    fourth_octet = convert2decimal(new_octet)
    print(fourth_octet)
    print(f"The IPV4 address is {first_octet}.{second_octet}.{third_octet}.{fourth_octet}")

def convert2decimal(new_octet):
    new_dec = int(new_octet, 2) #converts the binary to decimal form using int()
    return new_dec #returns the input to pass on for printing

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

def rot13main():
    string = input("Enter a string to encode/decode: ")
    result = rot13decode(string)
    print(f"Your message is: {result}")

def rot47main():
    string = input("Enter a ROT47 string: ")
    result = rot47decode(string)
    print(f"Your message is: {result}")

def rot_n_main():
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
            return
        else:
            print("That is not a valid response")

def uestools():
    while True:
        user_continue = input("Would you like to continue? Y/n: ")
        if user_continue in ["Y" , "y"]:
            options()
            return
        elif user_continue == "n":
            return
        else:
            print("Invalid option")

#-----------------------------------------------CODE EXECUTION----------------------------------------------------------
print(banner)
options()


