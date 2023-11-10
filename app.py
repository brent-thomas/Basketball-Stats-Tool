from constants import PLAYERS, TEAMS

##display a welcome message to the user
def welcome_message():
    print(f"""
{'#' * 39}

Welcome to the Basketball Stats Tool!
Easily view and manage team statistics.

{'#' * 39}
    """)


    
#display menu to proceed or quit, followed by team selection
def display_menu(teams):
    print("V) View Team Stats")
    print("Q) Quit")
    while True:
        option = input("\nEnter an option (V/Q): ").upper()
        if option == "V":
            print('\n-----\nTeams\n-----')
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for index,team in enumerate(teams):
                print(f"{alphabet[index]}) {team['name']}")
            while True:
                selected_team = input('\nEnter an option: ').upper()
                if selected_team in alphabet[:len(teams)]:
                    return teams[alphabet.index(selected_team)]
                else:
                    print("Invalid selection. Try again")
        elif option == "Q":
            print('Goodbye')
            break
        else:
            print("Please select a valid option")



#clean the player data
#conver height to an int, experience to a Boolean, and guardians to a list
def clean_data(players):
    cleaned_players_list = []
    for player in players:
        cleaned_player = {}
        cleaned_player['name'] = player['name']
        cleaned_player['height'] = int(player['height'].split(" ")[0])
        cleaned_player['experience'] = True if player['experience'] == 'YES' else False
        cleaned_player['guardians'] = player['guardians'].split(" and ")
        cleaned_players_list.append(cleaned_player)
    return cleaned_players_list



#calculate the avg teams height
def calculate_avg_height(players):
    sum_height = 0
    avg_height = 0
    for player in players:
        sum_height += player['height']
    avg_height = round(sum_height/len(players),1)
    return avg_height



#balance teams 6 players per team, and 3 experienced and inexperienced players on each team
def balance_teams(teams,players):
    balanced_teams = []
    for team in teams:
        team_data = {
            'name': team,
            'experienced_players': 0,
            'inexperienced_players':0,
            'average_height': 0,
            'number_of_players': 0,
            'players': []
        }
        for player in players[:]:
            if player['experience'] == True and team_data['experienced_players'] < 3:
                team_data['players'].append(player)
                team_data['experienced_players'] += 1
                players.remove(player)
            elif player['experience'] == False and team_data['inexperienced_players'] < 3:
                team_data['players'].append(player)
                team_data['inexperienced_players'] += 1
                players.remove(player)
        team_data['average_height'] = calculate_avg_height(team_data['players'])
        balanced_teams.append(team_data)
    return balanced_teams



#join the guardians of each players into a string
def join_guardians(players):
    guardian_names = []
    for player in players:
        guardian_names.extend(player['guardians'])
    joined_names = ', '.join(guardian_names)
    return joined_names

#join the player names into a string
def join_players(players):
    player_names = []
    for player in players:
        player_names.append(f"{player['name']} ({player['height']} in)")
    joined_names = ', '.join(player_names)
    return joined_names



#display team stats
def display_team_stats(team):
    print(f"\nTeam: {team['name']}")
    print('-' * 20)
    print(f"Total Players: {len(team['players'])}")
    print(f"Total experienced: {team['experienced_players']}")
    print(f"Total inexperienced: {team['inexperienced_players']}")
    print(f"Average height: {team['average_height']} ")
    print("\nPlayers on Team:")
    #sort players by height
    sorted_players = sorted(team['players'], key=lambda player: player['height'])
    print(join_players(sorted_players))
    print('\nGuardians:')
    print(join_guardians(team['players']))
    print('\n')



def main():
    cleaned_players_list = clean_data(PLAYERS)
    balanced_teams = balance_teams(TEAMS, cleaned_players_list)
    welcome_message()
    while True:
        selected_team = display_menu(balanced_teams)
        if selected_team:
            display_team_stats(selected_team)
        else:
            break
            


if __name__ == "__main__":
    main()