#
#Used for fetching all players (possible top five) from the highScores database
#

import MySQLdb

#Opening database connection. Do not give this information out freely to anyone!!
db = MySQLdb.connect("www.savagews6.ares.feralhosting.com:31135","root","JSpLwCwY7hkRVhsE","musicGameDB" )

#defining local variables
#user = .upper()
#songArtist =.upper()
#songName = .upper()
#songLength =
count = 0

# Going to execute query to find user in Highscores DB
cursor = db.cursor()
cursor.execute("SELECT * FROM Highscores WHERE ArtistName = " + songArtist + " AND SongName = " + songName + " AND (" + (songLength-10) +" <= SongLength AND SongLength <= " + (songLength+10) +")" )

data = cursor.fetchall()
for row in data:
	if row[3] == user:
		#Display in a highlight format to signal this is current user
		count++
		if count == 5:
			break
	else:
		#display every user who has played the song, create scroll bar.. Not sure if break will work after five
		count++
		if count == 5:
			break
		
# commit and disconnect from server
db.commit()
db.close()