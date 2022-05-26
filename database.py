from run import db,  League, Division, Team

nfc = League(id=0, league_name='National')
nfc_north = Division(id=0, division_name='North', league_id=0, league_name='National')
packers = Team(id=0, team_name='Packers', city='Green Bay', league_id=0, league_name='National', division_id=0, division_name='North')
bears = Team(id=1, team_name='Bears', city='Chicago', league_id=0, league_name='National', division_id=0, division_name='North')

db.session.add(nfc)
db.session.add(nfc_north)
db.session.add(packers)
db.session.add(bears)
db.session.commit()