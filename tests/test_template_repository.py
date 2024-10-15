from lib.template_repository import TemplateRepository
from lib.template import Template


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/students_table.sql") 
    repository = TemplateRepository(db_connection)

    students = repository.all() 

    assert students == [
        Template("Kelly Howes", "Sept 2024 foundations ra"),
        Template("Kimiko Dogue", "Walkies"),
        Template("Twyla Kitty", "Purrfect"),
        Template("Yuki Snake", "Cornucopia"),
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/students_table.sql")
    repository = TemplateRepository(db_connection)

    student = repository.find("Kelly Howes")
    assert student == Template("Kelly Howes", "Sept 2024 foundations ra")

def test_create_record(db_connection):
    db_connection.seed("seeds/students_table.sql")
    repository = TemplateRepository(db_connection)

    repository.create(Template("Kiyomi Dogue", "Barker"))

    result = repository.all()
    assert result == [
        Template("Kelly Howes", "Sept 2024 foundations ra"),
        Template("Kimiko Dogue", "Walkies"),
        Template("Twyla Kitty", "Purrfect"),
        Template("Yuki Snake", "Cornucopia"),
        Template("Kiyomi Dogue", "Barker")
    ]

def test_update_record(db_connection):
    db_connection.seed("seeds/students_table.sql")
    repository = TemplateRepository(db_connection)
    repository.update("Mini Panther", 3) # Will change Twyla to Mini

    student = repository.find("Mini Panther")
    assert student == Template("Mini Panther", "Purrfect")


def test_delete_record(db_connection):
    db_connection.seed("seeds/students_table.sql")
    repository = TemplateRepository(db_connection)
    repository.delete(3) # Will delete Mini

    result = repository.all()
    assert result == [
        Template("Kelly Howes", "Sept 2024 foundations ra"),
        Template("Kimiko Dogue", "Walkies"),
        Template("Yuki Snake", "Cornucopia"),
    ]