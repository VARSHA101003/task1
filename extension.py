#write a python program to accept a filename from user and print the extension of that
#program
def get_file_extension(filename):
    parts = filename.split(".")
    if len(parts) > 1:
        return parts[-1]
    else:
        return ""

def main():
    filename = input("Enter the filename: ")
    extension = get_file_extension(filename)
    if extension:
        print(f"The extension of the file is: {extension}")
    else:
        print("The file has no extension.")

if __name__ == "__main__":
    main()
