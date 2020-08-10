import requests
from bs4 import BeautifulSoup
import string
from pprint import pprint
import pandas as pd
import numpy as np

class Fighter:
	number_of_fighters = 0

	def __init__(self, fighter_data):
		self.name = fighter_data[0]
		self.record = fighter_data[1]
		self.nickname = fighter_data[2]
		self.height = fighter_data[3]
		self.weight = fighter_data[4]
		self.reach = fighter_data[5]
		self.stance = fighter_data[6]
		self.birth_date = fighter_data[7]
		self.sig_strikes_per_min = fighter_data[8]
		self.sig_strikes_accur = fighter_data[9]
		self.sig_strikes_absrb_min = fighter_data[10]
		self.sig_strikes_defnce = fighter_data[11]
		self.take_down_avg = fighter_data[13]
		self.take_down_accur = fighter_data[14]
		self.take_down_def = fighter_data[15]
		self.sub_avg = fighter_data[16]
		Fighter.number_of_fighters += 1
	
	def describe(self):
		pprint(vars(self))

	def getName(self):
		return self.name
	def getRecord(self):
		return self.record
	def getNickname(self):
		return self.nickname
	def getHeight(self):
		return self.height
	def getWeight(self):
		return self.weight
	def getReach(self):
		return self.reach
	def getStance(self):
		return self.stance
	def getBirthDate(self):
		return self.birth_date	 
	def getSigStrikesPerMin(self):
		return self.sig_strikes_per_min
	def getSigStrikesAccur(self):
		return self.sig_strikes_accur	
	def getSigStrikesAbsbPerMin(self):
		return self.sig_strikes_defnce
	def getTakeDownAvg(self):
		return self.take_down_avg
	def getTakeDownAccur(self):
		return self.take_down_accur
	def getTakeDownDef(self):
		return self.take_down_def
	def subAvg(self):
		return self.sub_avg

def describeRequest(requestObject):
	print("HEADERS:")
	print(requestObject.headers)
	print("END REQUEST OBJ HEADERS")

def describeSoup(bsObject):
	print(bsObject.prettify())

#Returns a list of links to individual fighter pages at http://ufcstats.com/statistics/fighters?char={%char}&page=all'
def getFighterUrls():
	URL_PRE = 'http://ufcstats.com/statistics/fighters?char='
	URL_POST = '&page=all'
	alphabet = string.ascii_lowercase
	fighter_url_list = []
	for c in alphabet:
		URL = URL_PRE + c + URL_POST
		webpage = requests.get(URL)
		soup = BeautifulSoup(webpage.content, 'lxml')
		for item in soup.find_all('a'):
			if item.parent.name == 'td':
				fighter_url_list.append(item['href'])
	#slice off every 2nd and 3rd string
	fighter_url_list=  fighter_url_list[::3]
	return fighter_url_list

#takes a figher's webpage url and returns a list with the fighter's metadata
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

#takes a list of fighter objects and creates and returns data frame
def dataFrameConstruction(FighterObjectList):
	columns = ['name', 'record', 'nickname', 'height', 'weight', 'reach', 'stance', 'birth_date', 'sig_strikes_per_min', 'sig_strikes_accur', 'sig_strikes_absrb_min', 'sig_strikes_defnce', 'take_down_avg', 'take_down_accur', 'take_down_def', 'sub_avg']
	index = [n for n in range(len(FighterObjectList))]
	df = pd.DataFrame([vars(f) for f in FighterObjectList])
	#If you want to print whole dataframe
	#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	#	print(df)
	#otherwise print shorthand
	#print(df)
	return df


def main():
	fighter_urls = getFighterUrls()
	Fighter_Object_List = []
	for i in range(0, len(fighter_urls)):
		Fighter_Object_List.append(Fighter(getFighterData(fighter_urls[i])))	
	print ('# OF FIGHTERS: ' + str(Fighter.number_of_fighters))
	df = dataFrameConstruction(Fighter_Object_List)

if __name__ == "__main__":
	main()