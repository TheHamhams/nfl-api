
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import os


app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
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
    division_name = db.Column(db.String(30), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)
    league_name = db.Column(db.String(30))
    teams = db.relationship('Team', backref=db.backref('league', lazy='joined'), lazy='select')

    
    
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    league_id = db.Column(db.Integer)
    league_name = db.Column(db.String(30))
    division_id = db.Column(db.Integer, db.ForeignKey('division.id'), nullable=False)
    division_name = db.Column(db.String(30))
    
    def __repr__(self):
        return f'Team(name={self.name}, city={self.city}, league={self.league}, division={self.division})'
    
USER_DATA = {
    'admin': SECRET_KEY
}
#db.drop_all()
#db.create_all()

league_put_args = reqparse.RequestParser()
league_put_args.add_argument('league_name', type=str, help='League name required', required=True)

league_patch_args = reqparse.RequestParser()
league_patch_args.add_argument('league_name', type=str, help='League name required', required=True)

division_put_args = reqparse.RequestParser()
division_put_args.add_argument('division_name', type=str, help='Division name required', required=True)
division_put_args.add_argument('league_id', type=int, help='League ID required', required=True)

team_put_args = reqparse.RequestParser()
team_put_args.add_argument('team_name', type=str, help='Team name required', required=True)
team_put_args.add_argument('city', type=str, help='Team city required', required=True)
team_put_args.add_argument('league_id', type=int, help='Team league ID required', required=True)
team_put_args.add_argument('division_id', type=int, help='Team division ID required', required=True)


league_resource_fields = {
    'id': fields.Integer,
    'league_name': fields.String,
    'divisions': fields.List(fields.String(attribute='division_name'))
}

division_resource_fields = {
    'id': fields.Integer,
    'division_name': fields.String,
    'league_id': fields.Integer,
    'league_name': fields.String,
    'teams': fields.List(fields.String(attribute='team_name'))
}

team_resource_fields = {
    'id': fields.Integer,
    'team_name': fields.String,
    'city': fields.String,
    'league_id': fields.Integer,
    'league_name': fields.String,
    'division_id': fields.Integer,
    'division_name': fields.String
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class LeagueR(Resource):
    @marshal_with(league_resource_fields)
    def get(self, league_id):
        result = League.query.filter_by(id=league_id).first()
        if not result:
            abort(404, message='Could not find league with that ID')
        return result
    
    @auth.login_required
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
    
    @auth.login_required
    @marshal_with(league_resource_fields)
    def patch(self, league_id):
        args = league_patch_args.parse_args()
        result = League.query.filter_by(id=league_id).first()
        if not result:
            abort(404, message='League ID does not exist, cannot update')
        result.league_name = args.league_name
        db.session.commit()
        return result
    
    @auth.login_required
    @marshal_with(league_resource_fields)
    def delete(self, league_id):
        result = League.query.filter_by(id=league_id).first()
        if not result:
            abort(404, message="League ID doesn't exist, cannot delete")
        db.session.delete(result)
        db.session.commit()
        return '', 204
    
class DivisionR(Resource):
    @marshal_with(division_resource_fields)
    def get(self, division_id):
        result = Division.query.filter_by(id=division_id).first()
        if not result:
            abort(404, message='Could not find division with that ID')
        return result
    
    @auth.login_required
    @marshal_with(division_resource_fields)
    def put(self, division_id):
        args = division_put_args.parse_args()
        result = Division.query.filter_by(id=division_id).first()
        if result:
            abort(409, message='Division ID already exists')
        league = League.query.filter_by(id=args.league_id).first()
        division = Division(id=division_id, division_name=args.division_name, league_id=args.league_id, league_name=league.league_name)
        db.session.add(division)
        db.session.commit()
        return division, 201
    
    @auth.login_required
    @marshal_with(division_resource_fields)
    def delete(self, division_id):
        result = Division.query.filter_by(id=division_id).first()
        if not result:
            abort(404, message="Division ID doesn't exist, cannot delete")
        db.session.delete(result)
        db.session.commit()
        return '', 204



class TeamR(Resource):
    @marshal_with(team_resource_fields)
    def get(self, team_id):
        result = Team.query.filter_by(id=team_id).first()
        if not result:
            abort(404, message='Could not find team with that ID')
        return result
    
    @auth.login_required
    @marshal_with(team_resource_fields)
    def put(self, team_id):
        args=team_put_args.parse_args()
        result = Team.query.filter_by(id=team_id).first()
        if result:
            abort(409, message='Team ID already exists')
        
        league = League.query.filter_by(id=args.league_id).first()
        if not league:
            abort(404, message='Could not find league with that ID')
        
        division = Division.query.filter_by(id=args.division_id).first()
        if not division:
            abort(404, message='Could not find division with that ID')
        
        team = Team(id=team_id, team_name=args.team_name, city=args.city, league_id=league.id, league_name=league.league_name, division_id=division.id, division_name=division.division_name)
        db.session.add(team)
        db.session.commit()
        return team, 201
    
    @auth.login_required
    @marshal_with(team_resource_fields)
    def delete(self, team_id):
        result = Team.query.filter_by(id=team_id).first()
        if not result:
            abort(404, message="Team ID doesn't exist, cannot delete")
        db.session.delete(result)
        db.session.commit()
        return '', 204
        
api.add_resource(LeagueR, '/league/<int:league_id>')
api.add_resource(DivisionR, '/division/<int:division_id>')
api.add_resource(TeamR, '/team/<int:team_id>')

if __name__ == '__main__':
    app.run()