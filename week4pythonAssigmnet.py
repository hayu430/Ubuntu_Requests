# 🖋️ File Read & Write Challenge
# This program reads a file, modifies its content, and writes it into a new file.
# It also handles errors if the file doesn’t exist or can’t be read.

def file_read_write():
    try:
        # 🧪 Ask user for filename
        filename = input("Enter the name of the file to read: ")

        # Open file in read mode
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified file created: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    file_read_write()
