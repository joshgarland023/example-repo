2.
# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Open the file in write mode (will create it if it doesn't exist)
with open("reg_form.txt", "w") as file:
    # Loop for each student
    for i in range(num_students):
        student_id = input(f"Enter student ID number for student {i + 1}: ")
        file.write(student_id + "\n")   # Write the student ID
        file.write("." * 40 + "\n")     # Dotted line for signing

print("Registration complete. Data saved to reg_form.txt.")