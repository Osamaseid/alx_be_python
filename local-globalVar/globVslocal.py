# Define a variable in the global scope
global_variable = "I am in the global scope."

def enclosing_function():
    # Define a variable with the same name in the enclosing scope
    global_variable = "I am in the enclosing scope."

    # Access the global variable and the enclosing variable
    print(f"Global variable: {global_variable}")
    print(f"Enclosing variable: {global_variable}")

    def local_function():
        # Define a variable with the same name in the local scope
        local_variable = "I am in the local scope."
        print(f"Local variable: {local_variable}")

    local_function()

# Call the enclosing function
enclosing_function()