# open a file , read to it , write from it
# file_name , file_mode
# w mode - write mode - override a file if it already exists(clears everything inside it) or creates a new file
file  = open("test.txt", "w")
file.write("Hello World\nmy name is abhi") # use\n to move to next line in the file
file.close() # close the file to avoid memory leaks

# rather than opening and closing file manually we write it this way
# best practice to working with files - closes the file automatically
with open("test_auto.txt", "w") as file:
    file.write("Hello World\nmy name is abhi")



# # a mode - append mode - add to the end of the file
with open("test_auto.txt", "a") as file:
     file.write("\nnew addition")
    

# # r mode - read mode
with open("test_auto.txt", "r") as file:
    text = file.read()
    print(text)