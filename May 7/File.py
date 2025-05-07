# Step 1: Ask the user for input
user_input = input("Enter text: ")

# Step 2: Save the input to a file using the 'with' statement
with open('user_input.txt', 'w', encoding='utf-8') as file:
    file.write(f"User input: {user_input}\n")

# Step 3: Display the content of the file
with open('user_input.txt', 'r', encoding='utf-8') as file:
    print("\nFile content:")
    print(file.read())
