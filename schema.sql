CREATE TABLE offense (
  player_id TEXT PRIMARY KEY NOT NULL,
  passing_touchdowns INTEGER,
  passing_yards INTEGER,
  interceptions_thrown INTEGER,
  rush_touchdowns INTEGER,
  rush_yards INTEGER,
  receiving_touchdowns INTEGER,
  receiving_yards INTEGER,
  receptions INTEGER,
  punt_return_touchdown INTEGER,
  fumbles_recovered_for_touchdown INTEGER,	
  kickoff_return_touchdown INTEGER,
  fumbles_lost INTEGER	
);

