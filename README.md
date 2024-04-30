# whoheplayfor-mini

How to execute:
1. Open an SQL server (in the case of CSC4480, we use Villanova's CSDB server)
2. input the nba_schema.sql file
3. input the nba_teams.sql file (need teams first because all other entities reference team in the foreign key)
4. input nba_players.sql, nba_mascots.sql, and nba_coaches.sql
5. Download the oracledb and cx_Oracle libraries in your working directory commands: "python -m pip install oracledb" & "python -m pip install cx_Oracle"
6. Open guess.py in your preferred IDE or run in console (I used VSCode)
7. Run the guess.py file and log in to the database using your username and password
8. Play the game! Right answers earn 1 point, wrong answers deduct 1 point.
