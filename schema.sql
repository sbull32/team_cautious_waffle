CREATE TABLE nfl2020 (
  name TEXT,
  completed_passes INTEGER,
  attempted_passes INTEGER,
  passing_yards INTEGER,
  passing_touchdowns INTEGER,
  interceptions_thrown INTEGER,
  times_sacked INTEGER,
  yards_lost_from_sacks INTEGER,
  longest_pass INTEGER,
  quarterback_rating FLOAT,
  rush_attempts INTEGER,	
  rush_yards INTEGER,
  rush_touchdowns INTEGER,
  longest_rush INTEGER,
  times_pass_target INTEGER,
  receptions INTEGER,
  receiving_yards INTEGER,
  receiving_touchdowns INTEGER,
  longest_reception INTEGER,
  fumbles INTEGER,
  fumbles_lost INTEGER,
  fumbles_recovered_for_touchdown INTEGER,
  kickoff_return_touchdown INTEGER,	
  punt_return_touchdown INTEGER,
  position TEXT,
  fantasy_points FLOAT
);

CREATE TABLE nfl2020team (
  name TEXT,
  team TEXT
);

-- Joining  nfl2020 table with nfl2020team table
SELECT nfl.name,
  nfl.completed_passes,
  nfl.attempted_passes,
  nfl.passing_yards,
  nfl.passing_touchdowns,
  nfl.interceptions_thrown,
  nfl.times_sacked,
  nfl.yards_lost_from_sacks,
  nfl.longest_pass,
  nfl.quarterback_rating,
  nfl.rush_attempts,	
  nfl.rush_yards,
  nfl.rush_touchdowns,
  nfl.longest_rush,
  nfl.times_pass_target,
  nfl.receptions,
  nfl.receiving_yards,
  nfl.receiving_touchdowns,
  nfl.longest_reception,
  nfl.fumbles,
  nfl.fumbles_lost,
  nfl.fumbles_recovered_for_touchdown,
  nfl.kickoff_return_touchdown,	
  nfl.punt_return_touchdown,
  nfl.position,
  nfl.fantasy_points,
  team.team
INTO nfl2020final
FROM nfl2020 as nfl
LEFT JOIN nfl2020team as team
ON nfl.name = team.name;
	