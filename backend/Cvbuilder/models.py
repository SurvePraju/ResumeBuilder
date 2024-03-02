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

    def __str__(self):
        return self.id

    def get_member_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "fullName": self.name,
            "email": self.email,
            "userName": self.username,
            "contact": self.contact,
            "website": self.website,
            "designation": self.designation,
            "skills": self.skills,
            "interest": self.interest
        }


class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_title = db.Column(db.String(100))
    work_description = db.Column(db.String(1000))

    start_date = db.Column(db.Date)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "work_title": self.work_title,
            "work_description": self.work_description,
            # Convert date to string for JSON serialization
            "start_date": str(self.start_date),
            "member_id": self.member_id
        }


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String(100))
    project_description = db.Column(db.String(100))
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "project_title": self.project_title,
            "project_description": self.project_description,
            "member_id": self.member_id
        }


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    graduated_from = db.Column(db.String(200))
    starting_date = db.Column(db.Integer)
    ending_date = db.Column(db.Integer, nullable="True")
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "graduated_from": self.graduated_from,
            # Convert date to string for JSON serialization
            "starting_date": str(self.starting_date),
            # Convert date to string or None
            "ending_date": str(self.ending_date) if self.ending_date else None,
            "member_id": self.member_id
        }
