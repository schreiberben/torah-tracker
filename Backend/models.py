from flask_sqlalchemy import SQLAlchemy
from typing import Dict

db = SQLAlchemy()


class Section(db.Model):
    __tablename__ = 'section'

    name = db.Column(db.String(50), primary_key=True)
    parent_name = db.Column(db.String(50), db.ForeignKey('section.name'))
    children = db.relationship("Section")
    total_completed = db.Column(db.Integer, default=0)
    num_items = db.Column(db.Integer, nullable=False)
    section_type = db.Column(db.String(50), nullable=False)
    is_lowest = db.Column(db.Boolean, default=False, nullable=False)  # Is the lowest Sefer section before reaching ChapterPage?

    def __repr__(self) -> str:
        return f'Section(name={self.name}, parent_name={self.parent_name})'

    def serialize(self) -> Dict[str, db.Column]:
        return {
            "name" : self.name,
            "parent_name" : self.parent_name,
            "children" : self.children,
            "total_completed" : self.total_completed,
            "num_items" : self.num_items,
            "section_type" : self.section_type,
            "is_lowest" : self.is_lowest,
        }


class ChapterPage(db.Model):  # e.g Perek/Daf
    __tablename__ = 'chapter_page'

    number = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(50), db.ForeignKey('sefer.name'))
    page_type = db.Column(db.String(), nullable=False)
    is_completed = db.Column(db.Boolean(), default=False)

    def __repr__(self) -> str:
        return f'ChapterPage({self.page_type} {self.number}, completed={self.is_completed}'

    def __str__(self) -> str:
        return self.page_type + ' ' + str(self.number)

    def serialize(self) -> Dict[str, db.Column]:
        return {
            "number" : self.number,
            "parent_name" : self.parent_name,
            "page_type" : self.page_type,
            "is_completed" : self.is_completed,
        }
