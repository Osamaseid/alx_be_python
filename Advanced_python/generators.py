def simple_counter(limit):
    """
    A generator function that yields numbers from 1 to 'limit'.
    
    Parameters:
    limit (int): The upper limit for the count.
    
    Yields:
    int: The next number in the sequence.
    """
    for i in range(1, limit + 1):  # Iterate from 1 to 'limit'
        yield i  # Yield the current number

# Example usage of the generator
if __name__ == "__main__":
    limit = 5  # Set the upper limit for counting
    print(f"Counting up to {limit}:")
    
    # Create the generator
    counter_gen = simple_counter(limit)
    # Iterate over the generator and print each number
    for number in counter_gen:
        print(number)
    