from faker import Faker
import pyodbc

# Initialize Faker
fake = Faker()

# Generate fake data with sequential IDs
def generate_fake_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        record = {
            "Id": i,
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "Company": fake.company(),
            "Address": fake.address(),
            "City": fake.city(),
            "Phone": fake.random_number(digits=10),
            "Email": fake.email()
        }
        data.append(record)
    return data

# Connect to MSSQL using Windows Authentication
def connect_to_mssql(server, database):
    conn_str = (
        f"DRIVER={{SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

# Insert data into MSSQL
def insert_data_to_mssql(conn, data):
    cursor = conn.cursor()
    for record in data:
        cursor.execute("""
            INSERT INTO cus1_new_1 (Id, FirstName, LastName, Company, Address, City, Phone, Email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, record["Id"], record["FirstName"], record["LastName"], record["Company"],
            record["Address"], record["City"], record["Phone"], record["Email"])
    conn.commit()

# Main function
def main():
    server = 'AB-LPT-HYD-125'
    database = 'SampleDatabase'

    num_records = 10000 # Number of records to generate
    data = generate_fake_data(num_records)

    conn = connect_to_mssql(server, database)
    insert_data_to_mssql(conn, data)
    conn.close()

if __name__ == "__main__":
    main()
