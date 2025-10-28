# Student Form Filling App

def fill_form():
    print("\n===== STUDENT FORM FILLING APP =====")

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    dept = input("Enter Department: ")
    gender = input("Enter Gender (Male/Female): ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")

    # Store data in file
    with open("student_form_data.txt", "a") as file:
        file.write(f"Name: {name}, Roll No: {roll}, Department: {dept}, Gender: {gender}, Email: {email}, Phone: {phone}\n")

    print("\n✅ Student details saved successfully!\n")


# Main Program
while True:
    fill_form()
    again = input("Do you want to fill another form? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you! All data saved in 'student_form_data.txt'.")
        break
