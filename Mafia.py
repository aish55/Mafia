#Mafia
import random
names = ["Grant","Christopher","Chelsy","Regina","Stacey","Louie","Scott","Kristy","Emilee","Lacey","Jorden","Chandler","Robin","Pheobe","Naylor","Felicia","Elisabeth","Sloan","Devin","Valerie","Mckinney","Hilary","Patterson","Ember","Hayward","Alexandre","Edge","Jeanette","Hawkins"]

playerName = input("Please type in your name to start playing: ")
names.append(playerName)
namesUnused=names
for x in names:
	print(x)
civilians = [ ]
doctors = [ ]
detectives = [ ]
robots = [ ]
random.shuffle(names)
for i in range(15): 
	selected = random.choice(namesUnused)
	civilians.append(selected)
	names.remove(selected)
for i in range(5):
	selected = random.choice(namesUnused)
	doctors.append(selected)
	names.remove(selected)
for i in range(5):
	selected = random.choice(namesUnused)
	detectives.append(selected)
	names.remove(selected)
for i in range(5):
	selected = random.choice(namesUnused)
	robots.append(selected)


	names.remove(selected)
random.shuffle(names)
for i in civilians:
	if playerName == i:
		print("You are a civilian")
		playerType = "civilian"
for i in doctors:
	if playerName == i:
		print("You are a doctor")
		playerType = "doctor"
for i in detectives:
	if playerName == i:
		playerType = "detective"
		print("You are a detective")

for i in robots:
	if playerName == i:
		playerType = "robot"
		print("You are a robot")
count = 0
while True and count < 25:
	print("Here are all of the possible people")
	print(civilians + doctors + detectives + robots)
	if playerType == "robot":
		print("These are your robot compadres")
		print(robots)
		chosen = input("Who will you chooose to die?")
		for i in civilians:
			if chosen == i:
				civilians.remove(chosen)
		count += 1
		#for i in range (len(doctors))
	elif playerType == "civilian":
		print("You can't do anythihng this night.")
		count += 1
	elif playerType == "doctor":
		protected = input("who are you going to protect tonight?")
		for x in civilians:
			if protected == x:
				print("That was a civilain")
		for x in robots:
		    if protected == x:
			    print("That was a robot")
		for x in doctors:
		    if protected == x:
			    print("That was a doctor")
		for x in detectives:
		    if protected == x:
			    print("That was a detective")
		count += 1
	elif playerType == "detective":
		asking = input("Who do you think is a robot?")
		for i in robots:
			if asking == i:
				robots.remove(asking)
		count += 1

	elif count >= 25:
		print("here are the standings:")
		print("Doctors left:")
		print(len(doctors))
		print("Robots left:")
		print(len(robots))
		print("detectives left:")
		print(len(detectives))
		print("civilains left:")
		print(len(civilains))
		break
	else:
		print("Whoops that wasn't a robot.")


	if len(robots) == 0:
		print("You won!")
	print("It's the next day. Here's everyone left")
	print(robots + detectives + civilians + doctors)






