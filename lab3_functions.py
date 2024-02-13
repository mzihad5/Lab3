# File: lab3_functions.py

def write_name_to_file():
    try:
        name = input("Enter your name: ")
        with open("my_name.txt", "w") as file:
            file.write(name)
        print("Name written to file successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Test the function
if __name__ == "__main__":
    write_name_to_file()
