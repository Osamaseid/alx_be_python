def file():
    try:
        f = open("current_file.txt")
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("The file was opened successfully.")
    finally:
        print("The file() function has completed.")
print(file())        