#
#Used for connecting to DB and updating scores for player at end of song
#

import MySQLdb

#Opening database connection. Do not give this information out freely to anyone!!
db = MySQLdb.connect("REDACTED","REDACTED","REDACTED","musicGameDB" )


#defining local variables
#user = .upper()
#score = 
#songArtist =.upper()
#songName = .upper()
#songLength =
foundSong = False
greatScore = False

# Going to execute query to find user in Highscores DB
cursor = db.cursor()
cursor.execute("SELECT * FROM Highscores WHERE PlayerName = " + user + " AND ArtistName = " + songArtist + " AND SongName = " + songName )

data = cursor.fetchall()
for row in data:
	if row[3] == user:
		if (songLength - 10) <= row[2]:
			if row[2] <= (songLength + 10):
				if row[4] < score:
					foundSong = True
					greatScore = True
# If user is found in the table w/ song, do an update to song score. If not, insert user into Highscores DB according to song
if foundSong == True:
	if greatScore == True:
		cursor.execute("UPDATE Highscores SET Score = " + score + " WHERE SongName = " + songName)
else:
	cursor.execute("INSERT INTO Highscores (ArtistName, SongName, SongLength, PlayerName, Score) VALUES (" + songArtist +", " + songName + ", " + songLength + ", " + user + ", " + score +")")
	
# commit and disconnect from server
db.commit()
db.close()
