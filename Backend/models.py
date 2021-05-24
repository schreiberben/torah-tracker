from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sefer(db.Model):  # e.g Tanach

    name = db.Column(db.String(), primary_key=True)
    total_items = db.Column(db.Integer(), nullable=False)
    total_completed = db.Column(db.Integer(), default=0)

    def __repr__(self) -> str:
        pass


class SeferSub1(db.Model):  # e.g Torah

    name = db.Column(db.String(), primary_key=True)
    parent_name = db.Column(db.String(), db.ForeignKey('Sefer.name'))
    total_items = db.Column(db.Integer(), nullable=False)
    total_completed = db.Column(db.Integer(), default=0)

    def __repr__(self) -> str:
        pass


class SeferSub2(db.Model):  # e.g Sh'mot

    name = db.Column(db.String(), primary_key=True)
    parent_name = db.Column(db.String(), db.ForeignKey('SeferSub1.name'))
    total_items = db.Column(db.Integer(), nullable=False)
    total_completed = db.Column(db.Integer(), default=0)

    def __repr__(self) -> str:
        pass


class ChapterPage(db.Model):  # e.g Perek

    number = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(), db.ForeignKey('SeferSub2.name'))
    chapter_page_type = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean(), default=False)

    def __repr__(self) -> str:
        pass
