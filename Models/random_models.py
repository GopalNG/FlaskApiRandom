from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class GenerateModel(db.Model):
    __tablename__ = 'generate'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_id = db.Column(db.Integer)
    data = db.Column(db.Text())
    values = db.Column(db.String(80))

    def __init__(self, values, file_id, data):
        self.values = values
        self.file_id = file_id
        self.data = data

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.flush()
        db.session.refresh(self)
        return self.file_id

    @classmethod
    def find_by_file_id(cls, file_id):
        return cls.query.filter_by(file_id=file_id).first()

    @classmethod
    def get_file_data(cls, file_id):
        query_data = cls.query.filter_by(file_id=file_id).first()
        if query_data:
            return query_data.data
        return query_data

    def json(self):
        """Return object data in easily serializable format"""
        return {
            'file_id': self.file_id,
            'values': self.values,
            'data': self.data
        }
