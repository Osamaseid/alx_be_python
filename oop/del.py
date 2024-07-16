class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')  # Open the file for reading

    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()  # Close the file when the object is destroyed

# Create an object of FileHandler
file1 = FileHandler('sample.txt')
print(file1.read_data())
file_obj = FileHandler('sample.txt')
print(file_obj.__del__())

# Object is no longer needed, it will be garbage collected, and __del__ method will be called automatically to close the file