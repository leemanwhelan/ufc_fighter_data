#taken from link below:
#https://stackoverflow.com/questions/50882547/storing-a-list-of-objects-as-csv-in-python
import datetime
import csv
def to_csv(Fighters):
	with open('full_data.csv', 'w', newline = '') as csvfile:
		writer = csv.writer(csvfile)
		#writer.writerow(['first_name', 'last_name', 'wins', 'losses', 'draws', 'no_contests', 'nickname', 'height', 'weight', 'reach', 'stance', 'birth_date', 'sig_strikes_per_min', 'sig_strikes_accur', 'sig_strikes_absrb_min', 'sig_strikes_defnce', 'take_down_avg', 'take_down_accur', 'take_down_def', 'sub_avg'])
		for fighter in Fighters:
		#parse record
			try:
				bd = datetime.datetime(fighter.birth_date[2], fighter.birth_date[1], fighter.birth_date[0])
			except:
				bd = None
			writer.writerow([fighter.first_name, fighter.last_name, fighter.getWins(), fighter.getLosses(), fighter.getDraws(), fighter.getNoContests(), fighter.nickname, fighter.height, fighter.weight, fighter.reach, fighter.stance, bd, fighter.sig_strikes_per_min, fighter.sig_strikes_accur, fighter.sig_strikes_absrb_min, fighter.sig_strikes_defnce, fighter.take_down_avg,	fighter.take_down_accur, fighter.take_down_def, fighter.sub_avg])
			#fuck!
			#handle date

def to_csv_simple(Fighters):
	with open('data_simple.csv', 'w', newline = '') as csvfile:
		writer = csv.writer(csvfile)
		#writer.writerow(['first_name', 'last_name', 'wins', 'losses', 'draws', 'no_contests', 'nickname', 'height', 'weight', 'reach', 'stance', 'birth_date', 'sig_strikes_per_min', 'sig_strikes_accur', 'sig_strikes_absrb_min', 'sig_strikes_defnce', 'take_down_avg', 'take_down_accur', 'take_down_def', 'sub_avg'])
		for fighter in Fighters:
		#parse record
			writer.writerow([fighter.first_name, fighter.last_name, fighter.getWins(), fighter.getLosses(), fighter.getDraws(), fighter.getNoContests()])
			#fuck!
			#handle date
