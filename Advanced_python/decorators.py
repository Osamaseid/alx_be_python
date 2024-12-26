import time

def timer_decorator(func):
    """
    A decorator that measures the execution time of a function.
    
    Parameters:
    func (function): The function to be decorated.
    
    Returns:
    function: The wrapped function with execution time measurement.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time: {execution_time:.4f} seconds")  # Print the execution time
        return result  # Return the result of the original function

    return wrapper  # Return the wrapper function

# Example usage of the decorator
@timer_decorator
def example_function(n):
    """
    A sample function that simulates a time-consuming task.
    
    Parameters:
    n (int): The number of seconds to wait.
    """
    time.sleep(n)  # Simulate a delay

if __name__ == "__main__":
    print("Starting the example function...")
    example_function(2)  # Call the decorated function with a 2-second delay