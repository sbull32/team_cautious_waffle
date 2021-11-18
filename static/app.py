#IMPORT NECESSARY LIBRARIES
import joblib  #for importing your machine learning model
from flask import Flask, render_template, request, jsonify, make_response
import pandas as pd 
# import plotly.graph_objects as go


# SQLALCHEMY SETUP
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2

#os allows you to call in environment variables
# we will set the remote environment variables in heroku 
from dotenv import load_dotenv
import os 

load_dotenv()


#################################################
# Database Setup
#################################################

#make sure you have your own .env on your computer
#comment out when you plan to deploy from heroku

url = 'postgresql://postgres:password@localhost:5432/app-local'
# # postgresql://postgres:password@localhost/app-local
# # postgres://postgres:password@localhost:5432/app-local
# # #uncomment line below when you want to deploy to heroku
# # # url = os.environ.get("URL")


engine = create_engine(url)


# # # reflect an existing database into a new model
Base = automap_base()

# # reflect the tables
Base.prepare(engine, reflect=True)

# # Save reference to the table
# 
# FantasyTable = Base.classes.nfl2020final
# create instance of Flask app
app = Flask(__name__)

# FantasyData = session.query(FantasyTable).all()
myData = []

# for x in FantasyData:

#         fullFantasyData = {}

#         fullFantasyData = {
#             # "Week": x.week_id,
#             "Team":x.team,
#             "Player Name":x.name_,
#             "Position":x.position,
#             "Current Points":x.fantasy_points,
            # "Passing Touchdowns":x.passing_touchdowns,
            # "Passing Yards":x.passing_yards,
            # "Interceptions Thrown":x.interceptions_thrown,
            # "Rush Touchdowns":x.rush_touchdowns,
            # "Rush Yards":x.rush_yards,
            # "Receiving Touchdowns":x.receiving_touchdowns,
            # "Receiving Yards":x.receiving_yards,
            # "Receptions":x.receptions,
            # "Punt Return Touchdowns":x.punt_return_touchdown
            # "Fumbles Recovered For Touchdowns":x.fumbles_recovered_for_touchdown,
            # "Kickoff Return Touchdowns":x.kickoff_return_touchdown,
        # }

#         myData.append(fullFantasyData)
# #Line below will load your machine learning model
# #model = joblib.load("<filepath to saved model>")



# create route that renders index.html template
@app.route("/", methods=["GET","POST"])
def home():
    outcome = 'Predicted Fantasy Points' 
    #If you have the user submit a form
    if request.method == 'POST': 
        
        #get the contents of the input field. This is referenced by the name argument
        #in the input html
        Name = request.form.get("dropdown")
        print(Name)
        Position = request.form.get("dropdown2")
        print(Position)
        Team = request.form.get("dropdown3")
        print(Team)
        #all forms return a string, if you want your input to convert to numeric check
        #that the input is numeric and then convert. Skip if you need string inputs for your model
        query = f"select fantasy_points from nfl2020final where name = {Name} and position {Position} and team = {Team}"
        # FantasyData = session.query(Player_Stats).all()
        result = db.engine.execute(query)
        #This ensures that if a non numeric input is passed, nothing happens
        outcome = query
    return render_template("index.html", outcome=outcome)

if __name__ == '__main__':
    app.run(debug=True)



# fig = go.Figure(go.Indicator(
#     mode = "gauge+number+delta",
#     value = 420,
#     domain = {'x': [0, 1], 'y': [0, 1]},
#     title = {'text': "Is this a viable pick?", 'font': {'size': 36}},
#     delta = {'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
#     gauge = {
#         'axis': {'range': [None, 0], 'tickwidth': 1, 'tickcolor': "darkblue"},
#         'bar': {'color': "darkblue"},
#         'bgcolor': "white",
#         'borderwidth': 2,
#         'bordercolor': "gray",
#         'steps': [
#             {'range': [0, 5], 'color': 'Red'},
#             {'range': [5, 10], 'color': 'Yellow'},
#             {'range': [10, 30], 'color': 'lightgreen'},
#             {'range': [30, 600], 'color': 'green'}],
#         'threshold': {
#             'line': {'color': "red", 'width': 4},
#             'thickness': 0.75,
#             'value': 490}}))

# fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

# fig.show()