from flask import Blueprint, request
from Cvbuilder.models import *
from datetime import datetime
from flask import jsonify
api_views = Blueprint("api_views", __name__)


@api_views.route("/", methods=["POST"])
def fill_user_data():
    member = Member(
        description="Description",
        name="John Doe",
        email="john@example.com",
        username="john_doe",
        contact=1234567890,
        website="example.com",
        designation="Software Engineer",
        skills="Python, JavaScript, SQL",
        interest="Machine Learning, Web Development"
    )

    # Create WorkExperience instance
    work_experience = WorkExperience(
        work_title="Software Engineer",
        work_description="Worked on various projects",
        start_date=datetime(2018, 1, 1),  # Example date
        member=member  # Associate with the member
    )

    # Create Project instance
    project = Project(
        project_title="Project Title",
        project_description="Project Description",
        member=member  # Associate with the member
    )

    # Create Education instance
    education = Education(
        graduated_from="University XYZ",
        starting_date=datetime(2014, 9, 1),  # Example date
        ending_date=datetime(2018, 6, 1),  # Example date
        member=member  # Associate with the member
    )

    # Add instances to the session and commit changes
    db.session.add(member)
    db.session.add(work_experience)
    db.session.add(project)
    db.session.add(education)
    db.session.commit()

    return jsonify({"message": "New Member Created."}), 201


@api_views.route("/<user>", methods=["GET"])
def get_all_members(user):
    try:
        # Retrieve member from the database
        member = Member.query.filter_by(username=user).first()

        # Retrieve associated work experience and education
        work_experiences = WorkExperience.query.filter_by(
            member_id=member.id).all()
        educations = Education.query.filter_by(member_id=member.id).all()
        projects = Project.query.filter_by(member_id=member.id).all()

        # Serialize member, work experience, and education data
        serialized_member = member.get_member_json() if member else None

        serialized_projects = [project.to_dict()
                               for project in projects] if projects else None

        serialized_work_experience = [experience.to_dict()
                                      for experience in work_experiences] if work_experiences else None

        serialized_education = [education.to_dict()
                                for education in educations] if educations else None

        # Combine member, work experience, and education data into a single dictionary
        response_data = {
            "member": serialized_member,
            "work_experience": serialized_work_experience,
            "education": serialized_education,
            "project": serialized_projects
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"Error": str(e)}), 500
