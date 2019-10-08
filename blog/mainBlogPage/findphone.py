import shelve
with shelve.open("red.txt") as o:
	o["findPhone"] = "https://findclone.ru/";

with shelve.open("red.txt") as r:
		print(r.get("findPhone"))

input() 
