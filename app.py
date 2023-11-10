from constants import PLAYERS, TEAMS

def clean_players(players):
    cleaned_players_list = []
    for player in PLAYERS:
        cleaned_player = {}
        cleaned_player['height'] = int(player['height'].split(" ")[0])
        cleaned_player['experience'] = True if player['experience'] == 'YES' else False
        cleaned_player['guardians'] = player['guardians'].split(" and ")
        cleaned_players_list.append(cleaned_player)
    print(cleaned_players_list)


def main():
    clean_players(PLAYERS)

if __name__ == "__main__":
    main()