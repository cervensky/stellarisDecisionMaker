import os
import msvcrt
import time
import xml.etree.ElementTree as ET

# parse data.xml
tree = ET.parse('data.xml')
root = tree.getroot()

# loads all empire data into appropriate data dictionaries
def load_data(data, path):
	for tag in root.findall(path):
		data[tag.get("name")] = False

def load_weight_data(weight_data, path):
	for data in root.findall(path):
		#weight_data[data.]
		pass

def display_presenter():
	print("=*=*=*=*=*=*=*=*=*=*=*=*=")
	print("|-   *           *     -|\n| Stellaris AI Emulator |")
	print("|*   *           *   *  |\n*=*=*=*=*=*=*=*=*=*=*=*=*")
	print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿")
	print("⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿")
	print("⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿")
	print("⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿")
	print("⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿")
	print("⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿")
	print("⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼")
	print("⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼")
	print("⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿")
	print("⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿")
	print("⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿")
	print("⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿")
	print("⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿")
	print("⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉")
	time.sleep(1.5)

	os.system("cls")

def interactive_options(title, data):

	# length of decorational line
	line = "=" * len(title)

	# main loop
	while True:

		# display options menu
		print("Choose " + str(title) + ":\n========" + str(line) + "\n")
		i = 0

		# let user choose category
		if title == "Category":
			data = ["Galactic Community", "Placeholder"]
			for value in data:
				print(options[i] + " - " + value)
				i += 1

		# let user choose ethics, civics, etc.
		else:
			for value in data:
				print(options[i] + " - " + "[] " + value ) if data[value] == False else print(options[i] + " - " + "[x] " + value )
				i += 1
			print("\n0 - Continue")

		# get user input (!!! only works on windows, might have to look for alternatives to make script work cross-platform)
		inp = msvcrt.getch()
		inp = inp.decode("utf-8")

		# refresh screen
		os.system("cls")

		# modify data
		i = 0
		if title == "Category":
			for value in data:
				if inp == options[i]:
					return data[i]
				else:
					i += 1
		else:
			# continue options menu (jump out of function and continue to next menu)
			if inp == "0":
				break	
			for value in data:
				if inp == options[i]:
					data[value] = not data[value]
				i += 1 

def calculator(categories):
	while True:
		load_weight_data(galactic_community_weight_data, "./WeightingCategories/GalacticCommunity")


options = {0 : "1", 1 : "2", 2 : "3", 3 : "4", 4 : "5", 5 : "6", 6 : "7", 7 : "8", 8 : "9", 9 : "a",\
10 : "b", 11 : "c", 12 : "d", 13 : "e", 14 : "f", 15 : "g", 16 : "h", 17 : "i", 18 : "j", 19 : "k", \
20 : "l", 21 : "m", 22 : "n", 23 : "o", 24 : "p", 25 : "q", 26 : "r", 27 : "s", 28 : "t", 29 : "u", \
30 : "v", 31 : "w", 32 : "x", 33 : "y", 34 : "z", 35 : "A", 36 : "B", 37 : "C", 38 : "D", 39 : "E", \
40 : "F", 41 : "G", 42 : "H", 43 : "I", 44 : "J", 45 : "K", 46 : "L", 47 : "M", 48 : "N", 49 : "O"}

ethic_user_data = {}
authority_user_data = {}
civic_user_data = {}
corp_civic_user_data = {}
categories = []
galactic_community_weight_data = {}

os.system("cls")
load_data(ethic_user_data, "./EmpireData/Ethic")
load_data(authority_user_data, "./EmpireData/Authority")
load_data(civic_user_data, "./EmpireData/Civic")
load_data(corp_civic_user_data, "./EmpireData/CorpCivic")

# :D
display_presenter()

interactive_options("Ethics", ethic_user_data,)
interactive_options("Authority", authority_user_data)
if authority_user_data["Corporate"] == True:
	interactive_options("Corporation Civics", corp_civic_user_data)
else:
	interactive_options("Civics", civic_user_data)
category = interactive_options("Category", categories)

#calculator(categories)