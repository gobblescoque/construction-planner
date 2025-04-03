# Overall plan:
# Needs to take addresses and store them
# Dole out addresses to various crews/people
# Should track the states that the projects are in
import os
import sqlite3


class Site:
	def __init__(self, builder: str, type: str, address: str, state: str):
		self.builder: str = builder
		self.type: str = type
		self.address: str = address
		self.state: str = state


class infoGetter:
    def __init__(self):
        pass
    def retrieve():
        address = input("Please enter an address: \n");
        unit_type = input("Please specify type of home (eg single, multi)\n")
        builder = input("Please specify the builder\n")
        return address
    

if __name__ == "__main__":

    test = infoGetter.retrieve()
    print(test)
	# connection = sqlite3.connect("../database/data.db")

    	

	# a1 = Site("198 Saddlemead Green NE", "Not dug")
	# a1.state = "Dug"

	# states = ["Start", "Dug", "Footing", "Wall", "Poured"]

	# a1.state = states[1]
	# print(a1.state)

	# con = sqlite3.connect("../database/data.db")
	# cur = con.cursor()


	# res = cur.execute("SELECT name FROM sqlite_master")
	# res.fetchone()
