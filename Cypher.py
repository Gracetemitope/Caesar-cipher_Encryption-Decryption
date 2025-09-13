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
    print("Welcome to Function 02 - This is for Encryption")
    File = open("File.txt", "r")
    File_content = File.read()
    print(File_content)





def fun03():
    print("Welcome to Function 03 - This is for Decryption")

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

