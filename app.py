from lib.database_connection import DatabaseConnection
from lib.item_repository import TemplateRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/students_table.sql")

# # Retrieve all studentss
student_repository = TemplateRepository(connection)
students = student_repository.all()

# # List them out
for student in students:
    print(student)