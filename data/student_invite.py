import sys
sys.path.insert(1, '/data')
import sqlalchemy as sql
from sqlalchemy import orm
from sqlalchemy import Column as Cl
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class StudentInvite(SqlAlchemyBase, SerializerMixin):  # От ученика к учителю
    __tablename__ = 'student_invites'

    id = Cl(sql.Integer, primary_key=True, autoincrement=True)
    teacher_id = Cl(sql.Integer, sql.ForeignKey('teachers.id'))
    teacher = orm.relation('Teacher')
    student_id = Cl(sql.Integer, sql.ForeignKey('students.id'))
    student = orm.relation('Student')
    status = Cl(sql.Boolean, default=1)

    def __repr__(self):
        return f'{self.student.surname} {self.student.name} просит стать вашим учеников'