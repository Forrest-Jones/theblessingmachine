from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User, Donation, Organization, SuccessStory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/users')
def get_users():
    users = User.query.all()
    results = []

    for user in users:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        results.append(user_data)

    return jsonify(results)

@app.route('/users/<int:id>', methods=['GET', 'DELETE'])
def user_by_id(id):
    user = User.query.get(id)

    if user:
        if request.method == 'GET':
            user_dict = user.to_dict()

            response = make_response(
                jsonify(user_dict),
                200
            )
        elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()

            response = make_response(
                {},
                200
            )
    else:
        response = make_response(
            {"error": "User not found"},
            404
        )

    return response

@app.route('/donations', methods=['GET'])
@login_required # assuming you have implemented Flask-Login for user authentication
def donations():
    # get the limit query parameter from the request, default to 10 if not specified
    limit = int(request.args.get('limit', 10))

    # query the database for the specified number of donations
    donations = Donation.query.limit(limit).all()
    donations_dict = [donation.to_dict() for donation in donations]

    response = make_response(
        jsonify(donations_dict),
        200
    )

    return response





if __name__ == '__main__':
    app.run(debug=True)
