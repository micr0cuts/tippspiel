'''
Created on 31.01.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

adaptation for the euro 2021:
adaptation started on 2021-06-11
@author: Simon Vandieken
'''

import suds
import sys

def get_euro_results():
    # Wird scheinbar doppelt in die Datenbank eingepflegt
    LEAGUE_NAME = 'uefa-em-2020'
    #LEAGUE_NAME = 'em20'
    LEAGUE_SAISON = '2020'

    ## SOAP Interface
    URL = "http://www.openligadb.de/Webservices/Sportsdata.asmx?WSDL"

    ## Create client
    client = suds.client.Client(URL)

    ## Get Current Group
    try:
        group = client.service.GetCurrentGroup(LEAGUE_NAME).groupOrderID
    except AttributeError:
        print(f'Error getting LEAGUE_NAME {LEAGUE_NAME}')
        sys.exit(1)

    ## Get Match-List
    try:
        matches = client.service.GetMatchdataByGroupLeagueSaison(group, LEAGUE_NAME, LEAGUE_SAISON).Matchdata
    except AttributeError:
        print(f'Error getting match data.')
        sys.exit(1)

    ## iteration
    for match in matches:
        if match.matchResults:
            goals =  "[{0}:{1}]".format(match.matchResults.matchResult[0].pointsTeam1, match.matchResults.matchResult[0].pointsTeam2)
        else:
            goals = "[N/A]"
        print("""{start_time} - {goals} - {team1} vs. {team2}""".format(team1=match.nameTeam1,
            team2=match.nameTeam2, 
            goals=goals, start_time=match.matchDateTime.strftime("%a, %H:%M Uhr")))

    return matches

if __name__ == '__main__':
    get_euro_results()
