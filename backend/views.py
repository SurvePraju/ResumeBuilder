from flask import Blueprint, request
from models import Member, db
from flask import jsonify
api_views = Blueprint("api_views", __name__)


@api_views.route("/", methods=["POST"])
def fill_user_data():

    username = request.json.get("userName")
    name = request.json.get("fullName")
    email = request.json.get("email")
    contact = request.json.get("contact")
    print(name, email, contact, username)
    new_member = Member(name=name, username=username,
                        contact=contact, email=email)
    try:

        db.session.add(new_member)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "New Member Created ."}), 201


@api_views.route("/", methods=["GET"])
def get_all_members():
    try:
        # Query all records from the Member model
        members = Member.query.all()

        # Convert the query result to a list of dictionaries
        member_list = []
        for member in members:
            member_dict = {
                'id': member.id,
                'name': member.name,
                'username': member.username,
                'email': member.email,
                'contact': member.contact
                # Add more fields as needed
            }
            member_list.append(member_dict)

        # Return the list of members as JSON response
        return jsonify(member_list), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500
