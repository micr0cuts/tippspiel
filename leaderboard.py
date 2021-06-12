import pandas as pd
from euro_results import get_euro_results

teams = pd.read_csv('data/teams.csv')
players = pd.read_csv('data/players.csv')

matches = get_euro_results()

leaderboard = dict.fromkeys(x for x in players.columns if x != 'score_criterion')

for match in matches:
    if match.matchResults:
        team1 = match.nameTeam1
        team2 = match.nameTeam2
        # for some reason there is a matchResults[1]
        # no idea what it's for
        goals1 = match.matchResults.matchResult[0].pointsTeam1
        goals2 = match.matchResults.matchResult[0].pointsTeam1
        for player_name in leaderboard.keys():
            pass

        print(f'Finished match results {team1} - {team2}')
