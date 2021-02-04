# import dependencies
from flask import Flask, render_template, jsonify
# import data
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# #################################################
# # Database Setup
# #################################################
engine = create_engine("postgresql://postgres:postgres@localhost:5432/MLB_DB")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())
# Save reference to the table
mlb_data = Base.classes.mlb_data
teams = Base.classes.teams
salaries = Base.classes.salaries

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/team')
def viz1():
    return render_template('Teamapp.html')

@app.route('/year')
def viz2():
    return render_template('Yearapp.html')

@app.route('/mlb')
def viz3():
    return render_template('mlb.html')

@app.route('/final_thoughts')
def endpoint():
    return render_template('end.html')


@app.route('/mlb_data', methods=['GET'])
def get_mlb_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all dates and precipitation
    results = session.query(mlb_data.year, 
                            mlb_data.team, 
                            mlb_data.team_salary, 
                            mlb_data.avg_player_salary, 
                            mlb_data.median_player_salary, 
                            mlb_data.wins, 
                            mlb_data.cost_per_win, 
                            mlb_data.championship).all()

    session.close()

    # Convert to Dictionary
    mlb = []
    for year, team, team_salary, avg_player_salary, median_player_salary, wins, cost_per_win, championship in results:
        mlb_dict = {}
        mlb_dict["year"] = year
        mlb_dict["team"] = team
        mlb_dict["team_salary"] = team_salary
        mlb_dict["avg_player_salary"] = avg_player_salary
        mlb_dict["median_player_salary"] = median_player_salary
        mlb_dict["wins"] = wins
        mlb_dict["cost_per_win"] = cost_per_win
        mlb_dict["championship"] = championship
        mlb.append(mlb_dict)

    return jsonify(mlb)

@app.route('/teams', methods=['GET'])
def get_teams():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all dates and precipitation
    results = session.query(teams.yearID, 
                            teams.lgID, 
                            teams.teamID, 
                            teams.franchID, 
                            teams.divID, 
                            teams.Ranks, 
                            teams.Gs, 
                            teams.Ghome,
                            teams.W,
                            teams.L,
                            teams.DivWin,
                            teams.WCWin,
                            teams.LgWin,
                            teams.WSWin,
                            teams.R,
                            teams.AB,
                            teams.H,
                            teams.two_B,
                            teams.three_B,
                            teams.HR,
                            teams.BB,
                            teams.SO,
                            teams.SB,
                            teams.CS,
                            teams.HBP,
                            teams.SF,
                            teams.RA,
                            teams.ER,
                            teams.ERA,
                            teams.CG,
                            teams.SHO,
                            teams.SV,
                            teams.IPouts,
                            teams.HA,
                            teams.HRA,
                            teams.BBA,
                            teams.SOA,
                            teams.E,
                            teams.DP,
                            teams.FP,
                            teams.team_name,
                            teams.park,
                            teams.attendance,
                            teams.BPF,
                            teams.PPF,
                            teams.teamIDBR,
                            teams.teamIDlahman45,
                            teams.teamIDretro).all()

    session.close()

    # Convert to Dictionary
    team_list = []
    for yearID, lgID, teamID, franchID, divID, Ranks, Gs, Ghome,\
         W, L, DivWin, WCWin, LgWin, WSWin, R, AB, H, two_B, three_B,\
             HR, BB, SO, SB, CS, HBP, SF, RA, ER, ERA, CG, SHO, SV, IPouts,\
                 HA, HRA, BBA, SOA, E, DP, FP, team_name, park, attendance, BPF,\
                     PPF, teamIDBR, teamIDlahman45, teamIDretro in results:
        team_dict = {}
        team_dict["yearID"] = yearID
        team_dict["lgID"] = lgID
        team_dict["teamID"] = teamID
        team_dict["franchID"] = franchID
        team_dict["divID"] = divID
        team_dict["Ranks"] = Ranks
        team_dict["Gs"] = Gs
        team_dict["Ghome"] = Ghome
        team_dict["W"] = W
        team_dict["L"] = L
        team_dict["DivWin"] = DivWin
        team_dict["WCWin"] = WCWin
        team_dict["LgWin"] = LgWin
        team_dict["WSWin"] = WSWin
        team_dict["R"] = R
        team_dict["AB"] = AB
        team_dict["H"] = H
        team_dict["two_B"] = two_B
        team_dict["three_B"] = three_B
        team_dict["HR"] = HR
        team_dict["BB"] = BB
        team_dict["SO"] = SO
        team_dict["SB"] = SB
        team_dict["CS"] = CS
        team_dict["HBP"] = HBP
        team_dict["SF"] = SF
        team_dict["RA"] = RA
        team_dict["ER"] = ER
        team_dict["ERA"] = ERA
        team_dict["CG"] = CG
        team_dict["SHO"] = SHO
        team_dict["SV"] = SV
        team_dict["IPouts"] = IPouts
        team_dict["HA"] = HA
        team_dict["HRA"] = HRA
        team_dict["BBA"] = BBA
        team_dict["SOA"] = SOA
        team_dict["E"] = E
        team_dict["DP"] = DP
        team_dict["FP"] = FP
        team_dict["team_name"] = team_name
        team_dict["park"] = park
        team_dict["attendance"] = attendance
        team_dict["BPF"] = BPF
        team_dict["PPF"] = PPF
        team_dict["teamIDBR"] = teamIDBR
        team_dict["teamIDlahman45"] = teamIDlahman45
        team_dict["teamIDretro"] = teamIDretro
        team_list.append(team_dict)

    return jsonify(team_list)

@app.route('/salaries', methods=['GET'])
def get_salaries():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all dates and precipitation
    results = session.query(salaries.yearid, 
                            salaries.teamid, 
                            salaries.lgid, 
                            salaries.playerid, 
                            salaries.salary).all()
    
    session.close()

    # Convert to Dictionary
    salary_list = []
    for yearid, teamid, lgid, playerid, salary in results:
        salary_dict = {}
        salary_dict["yearid"] = yearid
        salary_dict["teamid"] = teamid
        salary_dict["lgid"] = lgid
        salary_dict["playerid"] = playerid
        salary_dict["salary"] = salary
        salary_list.append(salary_dict)
                            
    return jsonify(salary_list)

if __name__ == '__main__':
    app.run(debug=True)
    
