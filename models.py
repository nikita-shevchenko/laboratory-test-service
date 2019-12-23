from db import db
class Library(db.Model):
    library_name = db.Column(db.String(500), primary_key=True)
    library_address = db.Column(db.String(500))
    record_book = db.Column(db.String(6), primary_key=True)
    group_year = db.Column(db.Integer, primary_key=True)
    library_city = db.Column(db.String(500), primary_key=True)
    library_country = db.Column(db.String(500), primary_key=True)
    __table_args__ = (db.ForeignKeyConstraint(('record_book', 'group_year'),
                                              ('student.record_book', 'student.group_year')), {})

    def __init__(self, library_name, library_address, record_book, library_city, library_country):
        self.library_name = library_name
        self.library_address = library_address
        self.record_book = record_book
        self.library_city = library_city
        self.library_country = library_country


