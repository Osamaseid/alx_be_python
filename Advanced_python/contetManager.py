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

#############################################
import sqlite3

class DatabaseManager:
    """
    A context manager for handling database connections.
    """

    def __init__(self, db_name):
        """
        Initializes the context manager with a database name.
        
        Parameters:
        db_name (str): The name of the database file.
        """
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """
        Establishes the database connection and returns the connection object.
        
        Returns:
        connection object: The opened database connection.
        """
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the database connection when exiting the context.
        
        Parameters:
        exc_type: Exception type raised (if any).
        exc_value: Exception value raised (if any).
        traceback: Traceback object (if any).
        """
        if self.connection:
            self.connection.close()  # Ensure the connection is closed
            if exc_type is not None:
                print(f"An error occurred: {exc_value}")

# Example usage of the context manager
if __name__ == "__main__":
    with DatabaseManager('example.db') as conn:
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
        cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
        cursor.execute('INSERT INTO users (name) VALUES (?)', ('Bob',))
        conn.commit()  # Commit the changes

    # Querying the database to check the content
    with DatabaseManager('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)  # Output: (1, 'Alice'), (2, 'Bob')