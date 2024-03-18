import datetime
import psycopg # PostgreSQL adapter for Python


# Retrieves and displays all records from the students table.
def getAllStudents():
    # Prints the headers (with the under line "------")
    columnNames = ["student_id", "first_name", "last_name", "email", "enrollment_date"]
    columnsizes = [12, 20, 20, 30, 17]
    header = "|"
    headerLine = "|"

    for i in range(len(columnNames)):
        header = header + columnNames[i].center(columnsizes[i]) + "|"
        for j in range(columnsizes[i]):
            headerLine = headerLine + "-"
        headerLine = headerLine + "|"
    
    print(header)
    print(headerLine)

    # Prints the data
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students;")
        for record in cursor:
            recordString = "|"
            columnNumber = -1
            for entry in record:
                entry = str(entry) # Ensures that entry is a string
                columnNumber = columnNumber + 1
                entry = entry.center(columnsizes[columnNumber])
                recordString = recordString + entry + "|"
            print(recordString)
    
    print("")


# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))

    conn.commit()

    print(f"The new record (first_name: {first_name}, last_name: {last_name}, email: {email}, enrollment_date: {enrollment_date.strftime("%Y-%m-%d")}) has been added successfully.\n")


# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))

    conn.commit()

    print(f"The email for student_id: {student_id} has been updated to {new_email} successfully.\n")


# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))

    conn.commit()

    print(f"Student_id: {student_id} has been deleted successfully.\n")


# Prints the menu prompt.
def printPrompt():
    print("Please select an operation:")
    print("1- getAllStudents()")
    print("2- addStudent(first_name, last_name, email, enrollment_date)")
    print("3- updateStudentEmail(student_id, new_email)")
    print("4- deleteStudent(student_id)")
    print("0- Quit")


# This is the prompt loop where it asks the user to select an option.
def promptLoop():
    while (True):
        printPrompt()

        userInput = input("Please enter the number corresponding to your choice: ")
        print("")

        if (userInput == "0"):
            exit(0)

        elif (userInput == "1"):
            getAllStudents()

        elif (userInput == "2"):
            firstName = input("Please enter the student's first name: ")
            lastName = input("Please enter the student's last name: ")
            email = input("Please enter the student's email: ")
            enrollyear = int(input("Please enter the student's enrollment year: "))
            enrollmonth = int(input("Please enter the student's enrollment month: "))
            enrollday = int(input("Please enter the student's enrollment day: "))
            enrollDate = datetime.datetime(enrollyear, enrollmonth, enrollday)
            print("")
            addStudent(firstName, lastName, email, enrollDate)

        elif (userInput == "3"):
            id = input("Please enter the student's id that you wish to modify the email for: ")
            email = input("Please enter the student's new email: ")
            print("")
            updateStudentEmail(id, email)

        elif (userInput == "4"):
            id = input("Please enter the student's id that you wish to delete: ")
            print("")
            deleteStudent(id)

        else:
            print("Not a valid option!\n")


# The main function where the connection to the database is established. It then calls the promptLoop() function.
# The conn variable is made global so it can be used by the other functions.
def main():
    try:
        global conn
        conn = psycopg.connect("dbname=A3Q1 user=postgres password=postgres host=localhost port=5432")
        promptLoop()

    except psycopg.OperationalError as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()