from run import db,  League, Division, Team

#db.drop_all()
#db.create_all()

nfc = League(id=0, league_name='National')
afc = League(id=1, league_name='American')

nfc_north = Division(id=0, division_name='North', league_id=0, league_name='National')
nfc_south = Division(id=1, division_name='South', league_id=0, league_name='National')
nfc_west = Division(id=2, division_name='West', league_id=0, league_name='National')
nfc_east = Division(id=3, division_name='East', league_id=0, league_name='National')

afc_north = Division(id=4, division_name='North', league_id=1, league_name='American')
afc_south = Division(id=5, division_name='South', league_id=1, league_name='American')
afc_west = Division(id=6, division_name='West', league_id=1, league_name='American')
afc_east = Division(id=7, division_name='East', league_id=1, league_name='American')


packers = Team(id=0, team_name='Packers', city='Green Bay', league_id=0, league_name='National', division_id=0, division_name='North')
bears = Team(id=1, team_name='Bears', city='Chicago', league_id=0, league_name='National', division_id=0, division_name='North')
vikings = Team(id=2, team_name='Vikings', city='Minnesota', league_id=0, league_name='National', division_id=0, division_name='North')
lions = Team(id=3, team_name='Lions', city='Detroit', league_id=0, league_name='National', division_id=0, division_name='North')

cowboys = Team(id=4, team_name='Cowboys', city='Dallas', league_id=0, league_name='National', division_id=3, division_name='East')
giants = Team(id=5, team_name='Giants', city='New York', league_id=0, league_name='National', division_id=3, division_name='East')
eagles = Team(id=6, team_name='Eagles', city='Philadelphia', league_id=0, league_name='National', division_id=3, division_name='East')
commanders = Team(id=7, team_name='Commanders', city='Washington', league_id=0, league_name='National', division_id=3, division_name='East')

falcons = Team(id=8, team_name='Falcons', city='Atlanta', league_id=0, league_name='National', division_id=1, division_name='South')
panthers = Team(id=9, team_name='Panthers', city='Carolina', league_id=0, league_name='National', division_id=1, division_name='South')
saints = Team(id=10, team_name='Saints', city='New Orleans', league_id=0, league_name='National', division_id=1, division_name='South')
buccaneers = Team(id=11, team_name='Buccaneers', city='Tampa Bay', league_id=0, league_name='National', division_id=1, division_name='South')

cardinals = Team(id=12, team_name='Cardinals', city='Arizona', league_id=0, league_name='National', division_id=2, division_name='West')
rams = Team(id=13, team_name='Rams', city='Los Angeles', league_id=0, league_name='National', division_id=2, division_name='West')
niners = Team(id=14, team_name='49ers', city='San Francisco', league_id=0, league_name='National', division_id=2, division_name='West')
seahawks = Team(id=15, team_name='Seahawks', city='Seattle', league_id=0, league_name='National', division_id=2, division_name='West')

ravens = Team(id=16, team_name='Ravens', city='Baltimore', league_id=1, league_name='American', division_id=4, division_name='North')
bengals = Team(id=17, team_name='Bengals', city='Cincinnati', league_id=1, league_name='American', division_id=4, division_name='North')
browns = Team(id=18, team_name='Browns', city='Cleveland', league_id=1, league_name='American', division_id=4, division_name='North')
steelers = Team(id=19, team_name='Steelers', city='Pittsburgh', league_id=1, league_name='American', division_id=4, division_name='North')

bills = Team(id=20, team_name='Bills', city='Buffalo', league_id=1, league_name='American', division_id=7, division_name='East')
dolphins = Team(id=21, team_name='Dolphins', city='Miami', league_id=1, league_name='American', division_id=7, division_name='East')
patriots = Team(id=22, team_name='Patriots', city='New England', league_id=1, league_name='American', division_id=7, division_name='East')
jets = Team(id=23, team_name='Jets', city='New York', league_id=1, league_name='American', division_id=7, division_name='East')

texans = Team(id=24, team_name='Texans', city='Houston', league_id=1, league_name='American', division_id=5, division_name='South')
colts = Team(id=25, team_name='Colts', city='Indianapolis', league_id=1, league_name='American', division_id=5, division_name='South')
jaguars = Team(id=26, team_name='Jaguars', city='Jacksonville', league_id=1, league_name='American', division_id=5, division_name='South')
titans = Team(id=27, team_name='Titans', city='Tennessee', league_id=1, league_name='American', division_id=5, division_name='South')

broncos = Team(id=28, team_name='Broncos', city='Denver', league_id=1, league_name='American', division_id=6, division_name='West')
chiefs = Team(id=29, team_name='Chiefs', city='Kansas City', league_id=1, league_name='American', division_id=6, division_name='West')
raiders = Team(id=30, team_name='Raiders', city='Las Vegas', league_id=1, league_name='American', division_id=6, division_name='West')
chargers = Team(id=31, team_name='Chargers', city='Los Angeles', league_id=1, league_name='American', division_id=6, division_name='West')



db.session.add(nfc)
db.session.add(afc)

db.session.add(nfc_north)
db.session.add(nfc_west)
db.session.add(nfc_east)
db.session.add(nfc_south)
db.session.add(afc_east)
db.session.add(afc_west)
db.session.add(afc_north)
db.session.add(afc_south)

db.session.add(packers)
db.session.add(bears)
db.session.add(lions)
db.session.add(vikings)
db.session.add(falcons)
db.session.add(panthers)
db.session.add(saints)
db.session.add(buccaneers)
db.session.add(cardinals)
db.session.add(rams)
db.session.add(niners)
db.session.add(seahawks)
db.session.add(cowboys)
db.session.add(giants)
db.session.add(commanders)
db.session.add(eagles)

db.session.add(broncos)
db.session.add(chiefs)
db.session.add(raiders)
db.session.add(chargers)
db.session.add(texans)
db.session.add(colts)
db.session.add(jaguars)
db.session.add(titans)
db.session.add(bills)
db.session.add(dolphins)
db.session.add(patriots)
db.session.add(jets)
db.session.add(ravens)
db.session.add(bengals)
db.session.add(browns)
db.session.add(steelers)

db.session.commit()