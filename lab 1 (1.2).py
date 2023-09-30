
sequence = [4, 8, 15, 16, 23, 42]

try:
    formatted_output = ' '.join(map(str, sequence))
    print(formatted_output)
except Exception as e:
    print(f"An error occurred: {e}")
