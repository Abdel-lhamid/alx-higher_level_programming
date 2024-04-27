#!/usr/bin/python3
import MySQLdb
import sys

def select_states(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query to fetch all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)
    finally:
        # Close database connection
        if db:
            db.close()

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call select_states function with provided arguments
    select_states(username, password, database)

