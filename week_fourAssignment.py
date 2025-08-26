def file_read_write():

    filename = input("Enter the filename to read: ")

    try:

        with open(filename, "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f" Successfully created {new_filename} with modified content.")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: Permission denied. You don’t have access to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


file_read_write()
