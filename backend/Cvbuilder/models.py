from . import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    contact = db.Column(db.Integer, unique=True)
    website = db.Column(db.String(100), unique=True)
    designation = db.Column(db.String(100))
#  create seperate Table for Skills
    skills = db.Column(db.String(1000))
    work_experience = db.relationship(
        'WorkExperience', uselist=False, backref='member', lazy=True)
    project = db.relationship(
        'Project', uselist=False, backref='member', lazy=True)
    education = db.relationship(
        'Education', uselist=False, backref='member', lazy=True)
    interest = db.Column(db.String(200))

    def get_member_json(self):
        return {"id": self.id, "fullName": self.name, "email": self.email, "userName": self.username}


class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_title = db.Column(db.String(100))
    work_description = db.Column(db.String(1000))
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))
    start_date = db.Column(db.Date)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String(100))
    project_description = db.Column(db.String(100))
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    graduated_from = db.Column(db.String(200))
    starting_date = db.Column(db.Integer)
    ending_date = db.Column(db.Integer, nullable="True")
