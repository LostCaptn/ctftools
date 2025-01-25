"""
Christian Nelson
22 Jan 2025
Convert binary octets into decimal
"""


def options():
    print("Please choose from the following options:\n 1. Base64 \n 2. ipv4bin2dec \n 3. Substitution Cipher \n 4.Exit")
    while True:
        option = input("\nEnter a number: ")
        if option == "1":
            base64main()
            uestools()
        elif option == "2":
            ipv4decoder()
            uestools()
        elif option == "3":
            subciphermain()
            uestools()
        elif option == "4":
            break
        else:
            print("I'm sorry, that option isn't available right now")
            uestools()
        return


def base64decoder():
    import base64
    import binascii

    while True:
        base_64 = input("Enter the base64 string: ")
        try:
            # decode the input from base64 to ascii text
            base_64_bytes = base_64.encode("ascii")
            sample_bytes = base64.b64decode(base_64_bytes)
            sample = sample_bytes.decode("ascii")
            # encode the decoded message again back to base64
            sample_string_bytes = sample.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
            # check if the base64 encoded message matches the original message
            if base_64 == base64_string:
                #if it is, then we decode the message again and print it in human-readable form
                print("The input is base64")
                base64_string_bytes = base64_string.encode("ascii")
                sample_bytes = base64.b64decode(base64_string_bytes)
                sample = sample_bytes.decode("ascii")
                print(sample)
                break
        # avoids the program erroring out because the input isn't base64
        except binascii.Error :
            print("The input is not base64")

def base64encoder():
    import base64
    #courtesy of GeeksforGeeks.org
    while True:
        #gets input, turns into bytes
        sample_string = input("Enter the phrase you would like to encode: ")
        sample_string_bytes = sample_string.encode("ascii")
        #encodes it, then makes it readable base64
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        print(f"Encoded string: {base64_string}")

def base64main():
    action = input("Choose an option: \n 1. Encode \n 2. Decode \n 3. Exit \n")
    if action == "1":
        base64encoder()
        base64main()
    elif action == "2":
        base64decoder()
        base64main()
    elif action == "3":
        print("Goodbye")
    else:
        print("I'm sorry, that's not a valid option.")
        base64main()


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

def subbruteforce():
    letters = "abcdefghijklmnopqrstuvwxyz"
    x = 0
    enc_string = input("Enter the string to be decoded: ")
    # while loop to increment x by 1 each iteration, to test all 25 possibilities
    while x < 26:
        x += 1
        stringtodecrypt = enc_string
        stringtodecrypt = stringtodecrypt.lower()
        ciphershift = int(x)
        stringdecrypted = ""
        # for loop to convert the letter in the input to a number
        for character in stringtodecrypt:
            position = letters.find(character)
            # sets the position of the desired letter by taking away the value of x from the position
            newposition = position - ciphershift
            # if the character is contained in letters, then we add that letter to our decrypted string
            # by passing it the new position
            if character in letters:
                stringdecrypted = stringdecrypted + letters[newposition]
            # if the input character is not within letters, we add it to the string as normal
            else:
                stringdecrypted = stringdecrypted + character
        print(f"You used a substitution of {ciphershift}")
        print(f"Your decrypted message is: {stringdecrypted}")

def subkeydecript():
    letters = "abcdefghijklmnopqrstuvwxyz"
    enc_string = input("Enter the string to be decoded: ")
    # while loop to set the value of the key
    while True:
        key = input("what key would you like to use: ")
        stringtodecrypt = enc_string
        stringtodecrypt = stringtodecrypt.lower()
        ciphershift = int(key)
        stringdecrypted = ""
        # for loop to convert the letter in the input to a number
        for character in stringtodecrypt:
            position = letters.find(character)
            # sets the position of the desired letter by taking away the value of key from the position
            newposition = position - ciphershift
            # if the character is contained in letters, then we add that letter to our decrypted string
            # by passing it the new position
            if character in letters:
                stringdecrypted = stringdecrypted + letters[newposition]
            # if the input character is not within letters, we add it to the string as normal
            else:
                stringdecrypted = stringdecrypted + character
        print(f"You used a substitution of {ciphershift}")
        print(f"Your decrypted message is: {stringdecrypted}")
        break

def subkeyencript():
    letters = "abcdefghijklmnopqrstuvwxyz"
    enc_string = input("Enter the string to be encoded: ")
    # while loop to set the value of the key
    while True:
        key = input("what key would you like to use: ")
        stringtoencrypt = enc_string
        stringtoencrypt = stringtoencrypt.lower()
        ciphershift = int(key)
        stringencrypted = ""
        # for loop to convert the letter in the input to a number
        for character in stringtoencrypt:
            position = letters.find(character)
            # sets the position of the desired letter by taking away the value of key from the position
            newposition = position + ciphershift
            # if the character is contained in letters, then we add that letter to our decrypted string
            # by passing it the new position
            if newposition > 25:
                newposition = newposition - 26
            if character in letters:
                stringencrypted = stringencrypted + letters[newposition]
            # if the input character is not within letters, we add it to the string as normal
            else:
                stringencrypted = stringencrypted + character
        print(f"You used a substitution of {ciphershift}")
        print(f"Your encrypted message is: {stringencrypted}")
        break
def subciphermain():
    action = input("Enter a Number: \n 1. Encode \n 2. Decode \n 3. Brute Force \n 4. Exit \n Option: ")
    if action == "1":
        subkeyencript()
        subciphermain()
    elif action == "2":
        subkeydecript()
        subciphermain()
    elif action == "3":
        subbruteforce()
        subciphermain()
    elif action == "4":
        print("Goodbye")
    else:
        print("I'm sorry, that's not a valid option.")
        subciphermain()


def uestools():
    while True:
        user_continue = input("Would you like to continue? Y/n: ")
        if user_continue == "Y":
            options()
        elif user_continue == "n":
            break



options()



