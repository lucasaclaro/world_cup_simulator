import random
from teams import *
from groups import *
from time import sleep




def stage_first(group, teamA, teamB, teamC, teamD):

    goals = [0, 1, 2, 3, 4, 5]


    team_A_points = 0
    team_B_points = 0
    team_C_points = 0
    team_D_points = 0



    print('--------------------------------------------------------')
    print(group)
    print('')
    team_A_goals = random.choice(goals)
    team_B_goals = random.choice(goals)
    if team_A_goals > team_B_goals:
        team_A_points += 3
    elif team_B_goals > team_A_goals:
        team_B_points += 3
    elif team_A_goals == team_B_goals:
        team_A_points += 1
        team_B_points += 1
    print(f"{teamA}: {team_A_goals} X {teamB}: {team_B_goals}.")
    print("")





    team_C_goals = random.choice(goals)
    team_D_goals = random.choice(goals)
    if team_C_goals > team_D_goals:
        team_C_points += 3
    elif team_D_goals > team_C_goals:
        team_D_points += 3
    elif team_C_goals == team_D_goals:
        team_C_points += 1
        team_D_points += 1
    print(f"{teamC}: {team_C_goals} X {teamD}: {team_D_goals}.")
    print("")




    team_A_goals = random.choice(goals)
    team_C_goals = random.choice(goals)
    if team_A_goals > team_C_goals:
        team_A_points += 3
    elif team_C_goals > team_A_goals:
        team_C_points += 3
    elif team_A_goals == team_C_goals:
        team_A_points += 1
        team_C_points += 1
    print(f"{teamA}: {team_A_goals} X {teamC}: {team_C_goals}.")
    print("")




    team_B_goals = random.choice(goals)
    team_D_goals = random.choice(goals)
    if team_B_goals > team_D_goals:
        team_B_points += 3
    elif team_D_goals > team_B_goals:
        team_D_points += 3
    elif team_B_goals == team_D_goals:
        team_B_points += 1
        team_D_points += 1
    print(f"{teamB}: {team_B_goals} X {teamD}: {team_D_goals}.")
    print("")



    team_A_goals = random.choice(goals)
    team_D_goals = random.choice(goals)
    if team_A_goals > team_D_goals:
        team_A_points += 3
    elif team_D_goals > team_A_goals:
        team_D_points += 3
    elif team_A_goals == team_D_goals:
        team_A_points += 1
        team_D_points += 1
    print(f"{teamA}: {team_A_goals} X {teamD}: {team_D_goals}.")
    print("")




    team_B_goals = random.choice(goals)
    team_C_goals = random.choice(goals)
    if team_B_goals > team_C_goals:
        team_B_points += 3
    elif team_C_goals > team_B_goals:
        team_C_points += 3
    elif team_A_goals == team_B_goals:
        team_B_points += 1
        team_C_points += 1
    print(f"{teamB}: {team_B_goals} X {teamC}: {team_C_goals}.")
    print("")


    print(" ")
    print(f">>>>Classification {group}:<<<<")
    print("")
    print(f"{teamA}: {team_A_points} points.")
    print(f"{teamB}: {team_B_points} points.")
    print(f"{teamC}: {team_C_points} points.")
    print(f"{teamD}: {team_D_points} points.")
    print("")

    dic = {teamA: team_A_points, teamB: team_B_points, teamC: team_C_points, teamD:team_D_points}

    sort = sorted(dic.items(), key=lambda x: x[1])

    print(f">>>>Classified:<<<<\n First: {sort[3][0]}\n Second: {sort[2][0]}")

    group_A_classified = [sort[3], sort[2]]

    return group_A_classified



def roundOf16(teamA, teamB):
    goals = [0, 1, 2, 3, 4, 5]

    team_A_goals = random.choice(goals)
    team_B_goals = random.choice(goals)
    team_classificated = ''
    teams = [teamA, teamB]
    penalty_shootout = random.choice(teams)
    print(f"{teamA}: {team_A_goals} X {teamB}: {team_B_goals}.")
    if team_A_goals > team_B_goals:
        print(f"{teamA} Classified\n")
        team_classificated = teamA
    elif team_B_goals > team_A_goals:
        print(f"{teamB} Classified\n")
        team_classificated = teamB
    else:
        print(f"(penalty shootout) > {penalty_shootout} Classified!\n")
        team_classificated = penalty_shootout

    return team_classificated



def roundOf8(teamA, teamB):
    goals = [0, 1, 2, 3, 4, 5]

    team_A_goals = random.choice(goals)
    team_B_goals = random.choice(goals)
    team_classificated = ''
    teams = [teamA, teamB]
    penalty_shootout = random.choice(teams)
    print(f"{teamA}: {team_A_goals} X {teamB}: {team_B_goals}.")
    if team_A_goals > team_B_goals:
        print(f"{teamA} Classified\n")
        team_classificated = teamA
    elif team_B_goals > team_A_goals:
        print(f"{teamB} Classified\n")
        team_classificated = teamB
    else:
        print(f"(penalty shootout) > {penalty_shootout} Classified!\n")
        team_classificated = penalty_shootout


    return team_classificated



def roundOf4(teamA, teamB):
    goals = [0, 1, 2, 3, 4, 5]

    team_A_goals = random.choice(goals)
    team_B_goals = random.choice(goals)
    team_classificated = ''
    teams = [teamA, teamB]
    penalty_shootout = random.choice(teams)
    print(f"{teamA}: {team_A_goals} X {teamB}: {team_B_goals}.")
    if team_A_goals > team_B_goals:
        print(f"{teamA} Classified\n")
        team_classificated = teamA
    elif team_B_goals > team_A_goals:
        print(f"{teamB} Classified\n")
        team_classificated = teamB
    else:
        print(f"(penalty shootout) > {penalty_shootout} Classified!\n")
        team_classificated = penalty_shootout


    return team_classificated



def finals(teamA, teamB):
    goals = [0, 1, 2, 3, 4, 5]

    team_A_goals = random.choice(goals)
    team_B_goals = random.choice(goals)
    team_classificated = ''
    teams = [teamA, teamB]
    penalty_shootout = random.choice(teams)
    print(f"{teamA}: {team_A_goals} X {teamB}: {team_B_goals}.")
    if team_A_goals > team_B_goals:
        print(f"{teamA} Champion!\n")
        print('##############################')
        team_classificated = teamA
    elif team_B_goals > team_A_goals:
        print(f"{teamB} Champion!\n")
        print('##############################')
        team_classificated = teamB
    else:
        print(f"(penalty shootout) > {penalty_shootout} Champion!!!!!\n")
        team_classificated = penalty_shootout


    return team_classificated


