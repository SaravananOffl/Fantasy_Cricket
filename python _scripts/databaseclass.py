import sqlite3


class databasefunc:
    def __init__(self):
        pass



    def update_roaster(self,player_name):
        query = "DELETE FROM "+"cricketers" +" WHERE player = "+"'"+player_name+"'"
        connec = sqlite3.connect('cricket')
        result = connec.execute(query)
        print(result)
        connec.commit()
        connec.close()
        return result

    def add_player(self,player_name):
        query = " INSERT INTO " + self.table_name +" SELECT * FROM cricketers WHERE player = '" +player_name+ "'"
        connec = sqlite3.connect('cricket')
        connec.execute(query)
        connec.commit()
        connec.close()

    def new_team_members(self):
        connec = sqlite3.connect('cricket')
        c = connec.cursor()
        query2 = "SELECT player FROM %s" % self.table_name
        returned_players = c.execute(query2)
        returned_players = returned_players.fetchall()
        connec.close()
        return returned_players

    def bat_btn(self,ctg):

        query = "SELECT player FROM cricketers where ctg= '%s' "%ctg
        print(query)
        connection = sqlite3.connect('cricket')
        c =connection.cursor()
        result = c.execute(query)
        result = c.fetchall()
        connection.close()

        return result

    def remove_player(self,player_selected):
        query = "DELETE FROM cricketers WHERE player= "+ "'"+player_selected+"'"
        connection = sqlite3.connect('cricket')
        c = connection.cursor()
        result = connection.execute(query)
        print(result)
        result = c.fetchall()
        print(result)
        connection.close()
        return result

    def create_team(self, team_name):
        connec = sqlite3.connect('cricket')
        query = """ CREATE TABLE IF NOT EXISTS %s (
            	`Player`	TEXT NOT NULL,
            	`Scored`	INTEGER,
            	`Faced`	INTEGER,
            	`fours`	INTEGER,
            	`sixes`	INTEGER,
            	`bowled`	INTEGER,
            	`maiden`	INTEGER,
            	`given`	INTEGER,
            	`wkts`	INTEGER,
            	`catches`	INTEGER,
            	`stumping`	INTEGER,
            	`ro`	INTEGER,
            	`value`	INTEGER,
            	`matches`	INTEGER,
            	`runs`	INTEGER,
            	`100s`	INTEGER,
            	`50s`	INTEGER,
            	`ctg`	TEXT NOT NULL,
            	PRIMARY KEY(`Player`)
            )""" % (team_name)
        connec.execute(query)
        connec.commit()
        connec.close()

    def player_score_calc(self,team_name):
        connection = sqlite3.connect('cricket')
        query = "SELECT player FROM %s "%team_name
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        print(result)

    def list_all_tables(self):
        query = "    SELECT * FROM sqlite_master where type='table'"
        connection = sqlite3.connect('cricket')
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        print("CAME ")
        print(result)
        return result

