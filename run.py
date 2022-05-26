from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league_name = db.Column(db.String(30), nullable=False)
    divisions = db.relationship('Division', backref=db.backref('league', lazy='joined'), lazy='select')
    

class Division(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    div_name = db.Column(db.String(30))
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))
    
    

class TeamModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    
    
    def __repr__(self):
        return f'Team(name={self.name}, city={self.city}, league={self.league}, division={self.division})'
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    def __repr__(self) -> str:
        return f"User('{self.username}')"

db.drop_all()
db.create_all()

nfc = League(id=0, league_name='National')
db.session.add(nfc)
db.session.commit()

league_put_args = reqparse.RequestParser()
league_put_args.add_argument('league_name', type=str, help='League name required', required=True)
    
team_put_args = reqparse.RequestParser()
team_put_args.add_argument('name', type=str, help='Team name required', required=True)
team_put_args.add_argument('city', type=str, help='Team city required', required=True)
team_put_args.add_argument('league', type=str, help='Team league required', required=True)
team_put_args.add_argument('division', type=str, help='Team division required', required=True)

team_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'league': fields.String,
    'division': fields.String
}

league_resource_fields = {
    'id': fields.Integer,
    'league_name': fields.String,
    'divisions': fields.List(fields.String)
}

@auth.verify_password
def verify(username, password):
    user = User.query.filter_by(name=username).first()
    if not user:
        return False
    user_password = user.password
    return user_password == password

class LeagueR(Resource):
    @marshal_with(league_resource_fields)
    def get(self, league_id):
        result = League.query.filter_by(id=league_id).first()
        if not result:
            abort(404, message='Could not find league with that ID')
        return result
    
    @marshal_with(league_resource_fields)
    def put(self, league_id):
        args = league_put_args.parse_args()
        result = League.query.filter_by(id=league_id).first()
        if result:
            abort(409, message='League ID already exists')
        league = League(id=league_id, league_name=args.league_name)
        db.session.add(league)
        db.session.commit()
        return league, 201



class Team(Resource):
    def get(self):
        return {'message': 'Hello'}
    
api.add_resource(Team, '/')
api.add_resource(LeagueR, '/league/<int:league_id>')

if __name__ == '__main__':
    app.run(debug=True)