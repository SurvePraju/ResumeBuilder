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
        member=member.id  # Associate with the member by setting member_id
    )

    # Create Project instance
    project = Project(
        project_title="Project Title",
        project_description="Project Description",
        member_id=member.id
    )

    # Create Education instance
    education = Education(
        graduated_from="University XYZ",
        starting_date=datetime(2014, 9, 1),  # Example date
        ending_date=datetime(2018, 6, 1),  # Example date
        member_id=member.id
    )

    # Add instances to the session and commit changes
    db.session.add(member)
    db.session.add(work_experience)
    db.session.add(project)
    db.session.add(education)
    db.session.commit()

    return jsonify({"message": "New Member Created."}), 201


@api_views.route("/<email>", methods=["GET"])
def get_all_members(email):

    # return jsonify({"message": "Thats Great"})
    try:
        # Test -get all members from db
        member = Member.query.filter_by(email=email).first()
        work_experience = WorkExperience.query.filter_by(
            member_id=member).first()

        # Flask needs json serialied data
        if member:
            serialized_member = member.get_member_json()
        else:
            return jsonify({"message": "NO such Email Create a New!"})
        # Return the list of members as JSON response
        return jsonify(serialized_member), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500
