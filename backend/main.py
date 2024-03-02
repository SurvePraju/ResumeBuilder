from config import db, app
from views import api_views


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.register_blueprint(api_views, url_prefix="/")
    app.run(debug=True)
