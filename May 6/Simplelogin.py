# Stored username and password (you can change these)
correct_username = "admin"
correct_password = "1234"

# Get input from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful! Welcome,", username)
elif username != correct_username and password != correct_password:
    print("Both username and password are incorrect.")
elif username != correct_username:
    print("Incorrect username.")
else:
    print("Incorrect password.")
