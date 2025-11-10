def calculate_square(number):
    """
    Calculate the square of a given number
    """
    return number ** 2

def greet(name):
    """
    Return a greeting message
    """
    return f"Hello, {name}!"

# Example usage
if __name__ == "__main__":
    # Test the square function
    result = calculate_square(5)
    print(f"Square of 5 is: {result}")
    
    # Test the greeting function
    message = greet("World")
    print(message)