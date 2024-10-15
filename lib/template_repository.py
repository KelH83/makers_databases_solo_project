from lib.template import Template

class TemplateRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, student):
        self._connection.execute('INSERT INTO students (full_name, cohort) VALUES (%s, %s)', [
                                student.full_name, student.cohort])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from students')
        students = []
        for row in rows:
            item = Template(row["full_name"], row["cohort"])
            students.append(item)
        return students
    

    def find(self, student_name):
        rows = self._connection.execute(
            'SELECT * from students WHERE full_name = %s', [student_name])
        row = rows[0]
        return Template(row["full_name"], row["cohort"])
    
    # UPDATE
    def update(self, new_name, student_id):
        rows = self._connection.execute('UPDATE students SET full_name = %s WHERE id = %s', [new_name, student_id])
        row = rows[0]
        return Template(row["full_name"], row["cohort"])
    
    # DELETE
    def delete(self, student_id):
        self._connection.execute(
            'DELETE FROM students WHERE id = %s', [student_id])
        return None