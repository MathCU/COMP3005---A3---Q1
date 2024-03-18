Prerequisites:
1 - Install the most recent version of Python (3.12).
    a - Install psychopg with the following command: pip install "psycopg[binary]"
2 - Install the most recent version of PostgreQSL (16).
    a - Ensure that the following are used in PostgreSQL:
        - User: postgres
        - Password: postgres
        - Database name: A1Q3
        - host: localhost (this program will only work if it is used on the same computer as the database)
        - Port: 5432
4 - Run the "CreateStudentsTable.sql" file in the "A1Q3" database to create the table.
5 - Run the "InitialData.sql" file in the "A1Q3" database to add some initial data to the table.

To run the application:
1 - Start CDM or PowerShell.
2 - Navigate to the directory where the "DatabaseApp.py file is.
3 - Run the "DatabaseApp.py" program by entering "py ./DatabaseApp.py" command.
4 - Follow the instructions from the program (in the terminal).