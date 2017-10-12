# -*- coding: utf-8 -*-
#https://www.jokecamp.com/blog/guide-to-football-and-soccer-data-and-apis/
#http://www.football-data.co.uk/data.php

import csv

files = {'SP1-17.csv', 'SP1-16.csv', 'SP1-15.csv', 'SP1-14.csv', 'SP1-13.csv', 'SP1-12.csv'}
#teams = {'Valencia','Eibar','Barcelona','Malaga', 'La Coruna', 'Betis', 'Villarreal', 'Espanol', 'Alaves', 'Ath Madrid', 'Sevilla'}

def previousYears(t):	
	probs = [0, 0, 0] #Wins, Draws, Loses
	for f in files:
		with open(f) as csvfile:
			reader = csv.DictReader(csvfile)
			matches = 0
			data = [0, 0, 0]#Wins, Draws, Loses
			for row in reader:
				if row['HomeTeam'] == t:
					matches += 1
					if row['FTR'] == 'H':
						data[0] += 1
					if row['FTR'] == 'D':
						data[1] += 1
					if row['FTR'] == 'A':
						data[2] += 1
				if row['AwayTeam'] == t:
					matches += 1
					if row['FTR'] == 'A':
						data[0] += 1
					if row['FTR'] == 'D':
						data[1] += 1
					if row['FTR'] == 'H':
						data[2] += 1
			
			split = f.split('-')
			season = int(split[1][:2])
			if season == 17:
				magicnumber = 0.3
			else: 
				if season == 16:
					magicnumber = 0.22
				else: 
					if season == 15:
						magicnumber = 0.18
					else: 
						if season == 14:
							magicnumber = 0.14
						else: 
							if season == 13:
								magicnumber = 0.1
							else: 
								if season == 12:
									magicnumber = 0.06
			if matches != 0:						
				probs[0] += data[0]/float(matches)*magicnumber
				probs[1] += data[1]/float(matches)*magicnumber
				probs[2] += data[2]/float(matches)*magicnumber
	return probs
	
def head2head(t1, t2):
	probs = [0, 0, 0] #Wins, Draws, Loses
	for f in files:
		with open(f) as csvfile:
			reader = csv.DictReader(csvfile)
			matches = 0
			data = [0, 0, 0]#Wins, Draws, Loses
			for row in reader:
				if row['HomeTeam'] == t1 and row['AwayTeam'] == t2:
					matches += 1
					if row['FTR'] == 'H':
						data[0] += 1
					if row['FTR'] == 'D':
						data[1] += 1
					if row['FTR'] == 'A':
						data[2] += 1
						
				if row['HomeTeam'] == t2 and row['AwayTeam'] == t1:
					matches += 1
					if row['FTR'] == 'H':
						data[2] += 1
					if row['FTR'] == 'D':
						data[1] += 1
					if row['FTR'] == 'A':
						data[0] += 1
	
			split = f.split('-')
			season = int(split[1][:2])
			if season == 17:
				magicnumber = 0.3
			else: 
				if season == 16:
					magicnumber = 0.22
				else: 
					if season == 15:
						magicnumber = 0.18
					else: 
						if season == 14:
							magicnumber = 0.14
						else: 
							if season == 13:
								magicnumber = 0.1
							else: 
								if season == 12:
									magicnumber = 0.06
			if matches != 0:
				probs[0] += data[0]/float(matches)*magicnumber
				probs[1] += data[1]/float(matches)*magicnumber
				probs[2] += data[2]/float(matches)*magicnumber
			else:
				relegation = 1
				with open(f) as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:
						if row['HomeTeam'] == t1 or row['AwayTeam'] == t1:
							relegation = 2
							break
						if row['HomeTeam'] == t2 or row['AwayTeam'] == t2:
							relegation = 1
							break
					if relegation == 1:
						probs[2] += 2/float(2.0)*magicnumber
					else:
						probs[0] += 2/float(2.0)*magicnumber
	return probs
	
def last5games(t1, t2):	
	with open('SP1-17.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		matches1 = 0
		matches2 = 0
		results = [[0, 0, 0], [0, 0, 0]] #Wins, Draws, Loses, #Wins, Draws, Loses
		for row in reversed(list(reader)):
			if row['HomeTeam'] == t1 and matches1 < 5:
				matches1 += 1
				if row['FTR'] == 'H':
					results[0][0] += 1
				if row['FTR'] == 'D':
					results[0][1] += 1
				if row['FTR'] == 'A':
					results[0][2] += 1
					
			if row['AwayTeam'] == t1 and matches1 < 5:
				matches1 += 1
				if row['FTR'] == 'H':
					results[0][2] += 1
				if row['FTR'] == 'D':
					results[0][1] += 1
				if row['FTR'] == 'A':
					results[0][0] += 1
					
			if row['HomeTeam'] == t2 and matches2 < 5:
				matches2 += 1
				if row['FTR'] == 'H':
					results[1][0] += 1
				if row['FTR'] == 'D':
					results[1][1] += 1
				if row['FTR'] == 'A':
					results[1][2] += 1
					
			if row['AwayTeam'] == t2 and matches2 < 5:
				matches2 += 1
				if row['FTR'] == 'H':
					results[1][2] += 1
				if row['FTR'] == 'D':
					results[1][1] += 1
				if row['FTR'] == 'A':
					results[1][0] += 1
	
	for i in range(0,2):		
		for j in range(0,3):
			results[i][j] = results[i][j]/5.0
	return results
	
teams = ['Las Palmas', 'Celta']
preyears = {}
for t in teams:
	preyears[t] = previousYears(t)

heads = {}
heads = head2head(teams[0], teams[1])

last5 = {}
last5 = last5games(teams[0], teams[1])

probWinT1 = (preyears[teams[0]][0]*0.4 + heads[0]*0.3 + last5[0][0]*0.3)*100/2
probWinT2 = (preyears[teams[1]][0]*0.4 + heads[2]*0.3 + last5[1][0]*0.3)*100/2

probDrawT1 = (preyears[teams[0]][1]*0.4 + heads[1]*0.3 + last5[0][1]*0.3)*100/2
probDrawT2 = (preyears[teams[1]][1]*0.4 + heads[1]*0.3 + last5[1][1]*0.3)*100/2

probLossT1 = (preyears[teams[0]][2]*0.4 + heads[2]*0.3 + last5[0][2]*0.3)*100/2
probLossT2 = (preyears[teams[1]][2]*0.4 + heads[0]*0.3 + last5[1][2]*0.3)*100/2

print 'Probability win ' + teams[0] + ' ' + str(probWinT1+probLossT2) + ' %'
print 'Probability draw ' + str(probDrawT1+probDrawT2) + ' %'
print 'Probability win ' + teams[1] + ' ' + str(probWinT2+probLossT1) + ' %'
print '---'

print probWinT1 + probDrawT1 + probLossT1 + probWinT2 + probDrawT2 + probLossT2
