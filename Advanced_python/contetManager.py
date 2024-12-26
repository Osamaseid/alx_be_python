class FileManager:
    """
    A context manager for handling file operations.
    """
    def __init__(self, filename, mode):
        """
        Initializes the context manager with a filename and mode.
        
        Parameters:
        filename (str): The name of the file to be managed.
        mode (str): The mode in which to open the file (e.g., 'r', 'w').
        """
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """
        Opens the file and returns the file object.
        
        Returns:
        file object: The opened file.
        """
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the file when exiting the context.
        
        Parameters:
        exc_type: Exception type raised (if any).
        exc_value: Exception value raised (if any).
        traceback: Traceback object (if any).
        """
        if self.file:
            self.file.close()  # Ensure the file is closed
            if exc_type is not None:
                print(f"An error occurred: {exc_value}")

# Example usage of the context manager
if __name__ == "__main__":
    with FileManager('example.txt', 'w') as f:
        f.write('Hello, World!\n')  # Write to the file

    # Reading the file to check the content
    with FileManager('example.txt', 'r') as f:
        content = f.read()
        print(content)  # Output: Hello, World!