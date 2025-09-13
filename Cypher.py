# Fun02
# Function Start
# Open File.txt
# Store the handle in the variable local_10
# Open another File: File1.txt
# Store the handle in the variable local_14
# Start a loop
#    Do {
#             Read characters and store into the variable local_5
#              If the character is uppercase, set the variable local_c to A
#              If the character is lowercase, set the variable local_c to a
#              Perform caeser encryption (+3 shift)
#             Store the encrypted value in the variable local_5
#             Store the the value in local_5 to file1.txt
# } While (this is not the end of the first file(File.txt))
# Close the files
# Function End

def fun02():
    print("Welcome to Function 02 - Your file will be encrypted")
    try:
        with open('File.txt', 'r') as local_10, open('File1.txt', 'w') as local_14:
            while True:
                file_char = local_10.read(1)
                if not file_char:
                    break

                if file_char.isupper():
                    ascii_A = ord('A')
                    file_char_position = ord(file_char) - ascii_A
                    caeser_shift = file_char_position + 3
                    if caeser_shift >= 26:
                        caeser_shift -= 26
                    encrypted = chr(caeser_shift + ascii_A)
                elif file_char.islower():
                    ascii_a = ord('a')
                    file_char_position = ord(file_char) - ascii_a
                    caeser_shift = file_char_position + 3
                    if caeser_shift >= 26:
                        caeser_shift -= 26
                    encrypted = chr(caeser_shift + ascii_a)
                else:
                    encrypted = file_char

                local_14.write(encrypted)
                print(f"{encrypted}")


        print("Encryption complete. Output written to File1.txt")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Fun03
# Function Start
# Open File1.txt
# Store the handle in the variable local_10
# Open another File: File2.txt
# Store the handle in the variable local_14
# Start a loop
# Do {
#     Read characters and store into the variable local_5
#     If the character is uppercase, set the variable local_c to A
#     If the character is lowercase, set the variable local_c to a
#     Perform decryption (-3 shift)
#     Store the decrypted value in the variable local_5
#     Store the value in local_5 to file2.txt
# } While (this is not the end of the first file(File1.txt))

# Close the files

def fun03():
    print("Welcome to Function 03 - Your file will be Decrypted!")
    try:
        with open('File1.txt', 'r') as local_10, open('File2.txt', 'w') as local_14:
            while True:
                file_char = local_10.read(1)
                if not file_char:
                    break

                if file_char.isupper():
                    ascii_A = ord('A')
                    file_char_position = ord(file_char) - ascii_A
                    caeser_shift = file_char_position - 3
                    if caeser_shift < 0:
                        caeser_shift += 26
                    decrypted = chr(caeser_shift + ascii_A)

                elif file_char.islower():
                    ascii_a = ord('a')
                    file_char_position = ord(file_char) - ascii_a
                    caeser_shift = file_char_position - 3
                    if caeser_shift < 0:
                        caeser_shift += 26
                    decrypted = chr(caeser_shift + ascii_a)

                else:
                    decrypted = file_char

                local_14.write(decrypted)
                print(f"{decrypted}")

        print("Decryption complete. Output written to File2.txt")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



# Fun01
# Function Start
# {
#       Print a message
#       Read user’s input and store it in local_c
#       Perform some checks:
#         If (the input(local_c) is equal to 1) {
#             Call Fun02
#             }
#             else if (the input is equal to 2) {
#                         call Fun03
#                           }
#                           else {
#                               Print “invalid-Option”}
#                               }
#  Function End

def fun01():
    print("welcome, You can choose between Encryption and Decryption. Option 1 is for Encryption and 2 is for Decryption")
    users_input = input("Please Enter your preferred option: ")
    if int(users_input) == 1:
        fun02()
    elif int(users_input) == 2:
        fun03()
    else:
        print("Bad input. Unable to process")

fun01()