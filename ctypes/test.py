import ctypes

# Load the shared library
lib = ctypes.CDLL('./libexample.dylib')

# Define the argument and return types of the function
lib.add_numbers.argtypes = (ctypes.c_int, ctypes.c_int)
lib.add_numbers.restype = ctypes.c_int

# Call the C++ function
result = lib.add_numbers(3, 4)
print(result)