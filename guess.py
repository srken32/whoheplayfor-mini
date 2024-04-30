import getpass
import oracledb
import cx_Oracle

u = input("Input username: ")
pw = getpass.getpass("Enter password: ")

dsn_tns = cx_Oracle.makedsn('csdb.csc.villanova.edu', '1521', 'orcl')

connection = oracledb.connect(
    #user="skenney",
    user = u,
    password= pw,
    dsn=dsn_tns)

print("Successfully connected to Oracle Database")

cursor = connection.cursor()
score = 0

while True:
    table = input("Enter number 1-4, 1 for players, 2 for coaches, 3 for mascots, 4 to end game: ")
    team = ''
    if table == '1':
        cursor.execute('select * from (select * from player order by dbms_random.value) where rownum = 1')
        for row in cursor:
            team = row[2]
            print('What team does he play for? Name:',  row[0], row[1], 'Number:', row[3], 'Age:', row[4], 'Height (in):', row[5])
        guess = input("Guess the team name here (no location, caps sensitive):")
        if guess == team:
            score += 1
            print("You got it! Score:", score)
        else:
            score -= 1
            print('Wrong answer, correct is', team, 'Score: ', score)
    elif table == '2':
        cursor.execute('select * from (select * from coach order by dbms_random.value) where rownum = 1')
        for row in cursor:
            team = row[2]
            print('What team do they coach? Name:',  row[0], row[1], 'Age:', row[3])
        guess = input("Guess the team name here (no location, caps sensitive):")
        if guess == team:
            score += 1
            print("You got it! Score:", score)
        else:
            score -= 1
            print('Wrong answer, correct is', team, 'Score: ', score)
    elif table == '3':
        cursor.execute('select * from (select * from mascot order by dbms_random.value) where rownum = 1')
        for row in cursor:
            team = row[1]
            print('What team do they work for? Name:',  row[0], 'Type:', row[2])
        guess = input("Guess the team name here (no location, caps sensitive):")
        if guess == team:
            score += 1
            print("You got it! Score:", score)
        else:
            score -= 1
            print('Wrong answer, correct is', team, 'Score: ', score)
    elif table == '4':
        print('Game Over. Final Score: ', score)
        break
    else:
        print("You did not enter a number 1-4, please try again.")