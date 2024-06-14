import numpy as np

#シミュレーションパラメータ
num_simulations = 250000
teams_group1 = ['GEN', 'TS', 'T1', 'GE', 'BLD']
teams_group2 = ['DRX', 'PRX', 'TLN', 'RRQ', 'ZETA', 'DFM']
teams = teams_group1 + teams_group2

#Stage1までの戦績(ラウンド取得数は省略)
initial_stats = {
    'GEN': {'wins': 3, 'losses': 3, 'Map_wins': 9, 'Map_losses': 6},
    'TS': {'wins': 3, 'losses': 3, 'Map_wins': 8, 'Map_losses': 8},
    'T1': {'wins': 2, 'losses': 4, 'Map_wins': 6, 'Map_losses': 9},
    'GE': {'wins': 2, 'losses': 4, 'Map_wins': 6, 'Map_losses': 9},
    'BLD': {'wins': 1, 'losses': 5, 'Map_wins': 4, 'Map_losses': 11},
    'DRX': {'wins': 5, 'losses': 0, 'Map_wins': 10, 'Map_losses': 2},
    'PRX': {'wins': 4, 'losses': 1, 'Map_wins': 8, 'Map_losses': 3},
    'TLN': {'wins': 4, 'losses': 1, 'Map_wins': 8, 'Map_losses': 5},
    'RRQ': {'wins': 3, 'losses': 2, 'Map_wins': 6, 'Map_losses': 6},
    'ZETA': {'wins': 2, 'losses': 3, 'Map_wins': 6, 'Map_losses': 8},
    'DFM': {'wins': 1, 'losses': 4, 'Map_wins': 5, 'Map_losses': 9},
}

#各チームが6位以内に入る回数をカウント
top6_counts = {team: 0 for team in teams}

#シミュレーションをnum_simulations分行う
for _ in range(num_simulations):
    stats = {team: initial_stats[team].copy() for team in teams}
    
    #GroupAlphaの試合
    for i in range(len(teams_group1)):
        for j in range(i + 1, len(teams_group1)):
            team1 = teams_group1[i]
            team2 = teams_group1[j]
            outcome = np.random.choice(['2-0', '2-1', '0-2', '1-2'], p=[0.25, 0.25, 0.25, 0.25])
            if outcome == '2-0':
                stats[team1]['wins'] += 1
                stats[team2]['losses'] += 1
                stats[team1]['Map_wins'] += 2
                stats[team2]['Map_losses'] += 2
            elif outcome == '2-1':
                stats[team1]['wins'] += 1
                stats[team2]['losses'] += 1
                stats[team1]['Map_wins'] += 2
                stats[team2]['Map_wins'] += 1
                stats[team1]['Map_losses'] += 1
                stats[team2]['Map_losses'] += 2
            elif outcome == '0-2':
                stats[team2]['wins'] += 1
                stats[team1]['losses'] += 1
                stats[team2]['Map_wins'] += 2
                stats[team1]['Map_losses'] += 2
            elif outcome == '1-2':
                stats[team2]['wins'] += 1
                stats[team1]['losses'] += 1
                stats[team2]['Map_wins'] += 2
                stats[team1]['Map_wins'] += 1
                stats[team2]['Map_losses'] += 1
                stats[team1]['Map_losses'] += 2

    #GroupOmegaの試合
    for i in range(len(teams_group2)):
        for j in range(i + 1, len(teams_group2)):
            team1 = teams_group2[i]
            team2 = teams_group2[j]
            outcome = np.random.choice(['2-0', '2-1', '0-2', '1-2'], p=[0.25, 0.25, 0.25, 0.25])
            if outcome == '2-0':
                stats[team1]['wins'] += 1
                stats[team2]['losses'] += 1
                stats[team1]['Map_wins'] += 2
                stats[team2]['Map_losses'] += 2
            elif outcome == '2-1':
                stats[team1]['wins'] += 1
                stats[team2]['losses'] += 1
                stats[team1]['Map_wins'] += 2
                stats[team2]['Map_wins'] += 1
                stats[team1]['Map_losses'] += 1
                stats[team2]['Map_losses'] += 2
            elif outcome == '0-2':
                stats[team2]['wins'] += 1
                stats[team1]['losses'] += 1
                stats[team2]['Map_wins'] += 2
                stats[team1]['Map_losses'] += 2
            elif outcome == '1-2':
                stats[team2]['wins'] += 1
                stats[team1]['losses'] += 1
                stats[team2]['Map_wins'] += 2
                stats[team1]['Map_wins'] += 1
                stats[team2]['Map_losses'] += 1
                stats[team1]['Map_losses'] += 2

    #ランキング計算
    sorted_teams = sorted(teams, key=lambda t: (
        stats[t]['wins'],
        -stats[t]['losses'],
        stats[t]['Map_wins'],
        -stats[t]['Map_losses']
    ), reverse=True)
    
    #各チームが上位6チームに入るか?
    for i in range(6):
        top6_counts[sorted_teams[i]] += 1

#確率計算
top6_probabilities = {team: top6_counts[team] / num_simulations for team in teams}
top6_probabilities
