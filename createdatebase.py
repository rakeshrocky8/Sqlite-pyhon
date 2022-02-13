import sqlite3

connection = sqlite3.connect("myDatabase.db")

cursor = connection.cursor()


myQuery_1 = ''' CREATE TABLE Movies(
                  Name TEXT,
                  Actor TEXT,
                  Actress TEXT,
                  Director TEXT,
                  ReleaseYear TEXT
                  );
            '''

cursor.execute(myQuery_1)

Records=[ ("Moonfall                       ","Patrick Wilson ","Halle Berry     ","Roland Emmerich       ","2021"),
          ("Spider-Man: Homecoming         ","Tom Holland    ","Zendaya         ","Jon Watts             ","2017"),
          ("Mission: Impossible – Fallout  "," Tom Cruise    ","  Vanessa Kirby ","Christopher McQuarrie ","2018"),
          (" Hitman's Wife's Bodyguard     ","Ryan Reynolds  ","Salma Hayek     ","Patrick Hughes        ","2021"),
          ("Angel Has Fallen               ","Gerard Butler  ","Piper Perabo    ","Ric Roman Waugh       ","2019") ]

cursor.executemany('INSERT INTO Movies VALUES(?,?,?,?,?);',Records);

connection.commit()
connection.close()