import requests
from bs4 import BeautifulSoup
import string
from pprint import pprint
import pandas as pd
import numpy as np

class Fighter:
	number_of_fighters = 0


	def __init__(self, fighter_data):
		self.first_name, self.last_name = fighter_data[0], fighter_data[1]
		self.record = fighter_data[2]
		self.nickname = fighter_data[3]
		self.height = fighter_data[4]
		self.weight = fighter_data[5]
		self.reach = fighter_data[6]
		self.stance = fighter_data[7]
		self.birth_date = fighter_data[8]
		self.sig_strikes_per_min = fighter_data[9]
		self.sig_strikes_accur = fighter_data[10]
		self.sig_strikes_absrb_min = fighter_data[11]
		self.sig_strikes_defnce = fighter_data[12]
		self.take_down_avg = fighter_data[13]
		self.take_down_accur = fighter_data[14]
		self.take_down_def = fighter_data[15]
		self.sub_avg = fighter_data[16]
		Fighter.number_of_fighters += 1
	
	def parseName(self, name):
		if name is None:
			return None
		else:
			name = name.split()
			return (name[0], name[1])
	def parseRecord(self, record):
		record_list = record.split("Record: ", 10)[1].split("-")
		if "NC" in record_list[2]:
			tmp = record_list[2].split(" (")
			draws = int(tmp[0])
			no_contests = int(tmp[1][0:2].strip())
		else:
			draws = int(record_list[2])
			no_contests = 0
		wins = int(record_list[0])
		losses = int(record_list[1])
		return (wins, losses, draws, no_contests)
	def parseHeight(self, height):
		height_list = height.split("\' ")
		feet = int(height_list[0][0:1])
		inches = int(height_list[1].split("\"")[0])
		return (feet*12) + inches
	def parseBirthday(self, birthday):
		birthday = birthday.split(" ")
		day = int(birthday[1][:-1])
		year = int(birthday[2])
		dic = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}
		month = dic[str(birthday[0].strip())]
		#print(str(day) + " " + str(month) + " " + str(year))
		birthday = (day, month, year)
		return birthday
		


	def describe(self):
		pprint(vars(self))


def getFighterData(fighter_URL):
	webpage = requests.get(fighter_URL)
	soup = BeautifulSoup(webpage.content, 'lxml')
	fighter_data = []

	head_data = soup.find('h2',  class_="b-content__title")
	name_and_record = head_data.find_all('span')
	name = name_and_record[0].text.strip()
	record = name_and_record[1].text.strip()
	nickname = soup.find('p',  class_="b-content__Nickname").text.strip()
	fighter_data.extend((name, record, nickname))
	for item in soup.find_all('li', class_ = 'b-list__box-list-item b-list__box-list-item_type_block'):
		fighter_data.append(item.i.next_sibling.strip())
	return fighter_data

def parseName(name):
	try:
		name = name.split()
		return (name[0], name[1])
	except:
		return (None, None)

def parseRecord(record):
	try:
		record_list = record.split("Record: ", 10)[1].split("-")
		if "NC" in record_list[2]:
			tmp = record_list[2].split(" (")
			draws = int(tmp[0])
			no_contests = int(tmp[1][0:2].strip())
		else:
			draws = int(record_list[2])
			no_contests = 0
		wins = int(record_list[0])
		losses = int(record_list[1])
		return (wins, losses, draws, no_contests)
	except:
		return (None, None, None, None)

def parseHeight(height):
	try:
		height_list = height.split("\' ")
		feet = int(height_list[0][0:1])
		inches = int(height_list[1].split("\"")[0])
		return (feet*12) + inches
	except:
		return None

def parseBirthday(birthday):
	try:
		birthday = birthday.split(" ")
		day = int(birthday[1][:-1])
		year = int(birthday[2])
		dic = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}
		month = dic[str(birthday[0].strip())]
		#print(str(day) + " " + str(month) + " " + str(year))
		birthday = (day, month, year)
		return birthday
	except: 
		return (None, None, None)

def parse(fighter_meta_data):
	first_name, last_name = parseName(fighter_meta_data[0])
	record = parseRecord(fighter_meta_data[1])
	height = parseHeight(fighter_meta_data[3])
	birth_date = parseBirthday(fighter_meta_data[7])
	nickname = fighter_meta_data[2]
	try:
		weight = int(fighter_meta_data[4].split(" lbs.")[0])
	except: 
		weight = None
	try:
		reach = int(fighter_meta_data[5][:-1])
	except:
		reach = None
	stance = fighter_meta_data[6]
	sig_strikes_per_min = float(fighter_meta_data[8])
	sig_strikes_accur = float(fighter_meta_data[9][:-1])/100
	sig_strikes_absrb_min = float(fighter_meta_data[10])
	sig_strikes_defnce = float(fighter_meta_data[11][:-1])/100
	take_down_avg = float(fighter_meta_data[13])
	take_down_accur = float(fighter_meta_data[14][:-1])/100
	take_down_def = float(fighter_meta_data[15][:-1])/100
	sub_avg = float(fighter_meta_data[16])
	return [first_name, last_name, record, nickname, height, weight, reach, stance, birth_date, sig_strikes_per_min, sig_strikes_accur, sig_strikes_absrb_min, sig_strikes_defnce, take_down_avg, take_down_accur, take_down_def, sub_avg]
	#retun dict?
	#return {"first_name" : first_name, "last_name" : last_name, "record" : record, "height" : height, "birth_date" : birth_date,"nickname" : nickname, "weight" : weight, "reach" : reach, "stance" : stance, "SSPM" : sig_strikes_per_min, "SSA" : sig_strikes_accur, "SSAPM" : sig_strikes_absrb_min, "SSD" : sig_strikes_defnce, "TDAV" : take_down_avg,"TDAC" : take_down_accur, "TDD" : take_down_def}

def main():
	fighter_url1 = 'http://ufcstats.com/fighter-details/93fe7332d16c6ad9'
	fighter_url2 = 'http://ufcstats.com/fighter-details/fa6796c55d6c5440'
	Fighter_Object_List = []
	Fighter_Meta_Data1 = getFighterData(fighter_url1)
	Fighter_Meta_Data2 = getFighterData(fighter_url2)
	Fighter_Object_List.append(Fighter(parse(Fighter_Meta_Data1)))
	Fighter_Object_List.append(Fighter(parse(Fighter_Meta_Data2)))
	pprint(vars(Fighter_Object_List[0]))
	pprint(vars(Fighter_Object_List[1]))
	#print(parse(Fighter_Meta_Data1))
	#print()
	#print(parse(Fighter_Meta_Data2))
	#Abdurakihmov = Fighter(Fighter_Meta_Data1)
	#Blaydes = Fighter(Fighter_Meta_Data2)
	#for i in range(0, len(fighter_urls)):
	#for i in range(0, 20):
		#Fighter_Object_List.append(Fighter(getFighterData(fighter_urls[i])))
	#	Fighter_Meta_Data.append(getFighterData(fighter_urls[i]))
	#	Fighter_Object_List.append(Fighter(formatMetaData(Fighter_Meta_Data[i])))	
	#print ('# OF FIGHTERS: ' + str(Fighter.number_of_fighters))
	#Abdurakihmov.describe()
	#Blaydes.describe()
	#df = dataFrameConstruction(Fighter_Object_List)

if __name__ == "__main__":
	main()