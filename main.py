import random
from teams import *
from groups import *
from functions import *
from time import sleep


print('********************************************************')
print('World Cup 2022')
print('********************************************************')
print('')
print('Stage first!')
print('')
sleep(2)

stage_first('Group A', team_A, team_B, team_C, team_D)
sleep(.5)
stage_first('Group B', team_E, team_F, team_G, team_H)
sleep(.5)
stage_first('Group C', team_I, team_J, team_K, team_L)
sleep(.5)
stage_first('Group D', team_M, team_N, team_O, team_P)
sleep(.5)
stage_first('Group E', team_Q, team_R, team_S, team_T)
sleep(.5)
stage_first('Group F', team_U, team_V, team_W, team_X)
sleep(.5)
stage_first('Group G', team_Y, team_Z, team_AA, team_AB)
sleep(.5)
stage_first('Group H', team_AC, team_AD, team_AE, team_AF)
sleep(.5)
sleep(2)



team1 = stage_first('Group A', team_A, team_B, team_C, team_D)[0][0]
team2 = stage_first('Group B', team_E, team_F, team_G, team_H)[1][0]
team3 = stage_first('Group C', team_I, team_J, team_K, team_L)[0][0]
team4 = stage_first('Group D', team_M, team_N, team_O, team_P)[1][0]
team5 = stage_first('Group B', team_E, team_F, team_G, team_H)[0][0]
team6 = stage_first('Group A', team_A, team_B, team_C, team_D)[1][0]
team7 = stage_first('Group D', team_M, team_N, team_O, team_P)[0][0]
team8 = stage_first('Group C', team_I, team_J, team_K, team_L)[1][0]
team9 = stage_first('Group E', team_Q, team_R, team_S, team_T)[0][0]
team10 = stage_first('Group F', team_U, team_V, team_W, team_X)[1][0]
team11 = stage_first('Group G', team_Y, team_Z, team_AA, team_AB)[0][0]
team12 = stage_first('Group H', team_AC, team_AD, team_AE, team_AF)[1][0]
team13 = stage_first('Group F', team_U, team_V, team_W, team_X)[0][0]
team14 = stage_first('Group E', team_Q, team_R, team_S, team_T)[1][0]
team15 = stage_first('Group H', team_AC, team_AD, team_AE, team_AF)[0][0]
team16 = stage_first('Group G', team_Y, team_Z, team_AA, team_AB)[1][0]

print('--------------------------------------------------------')
print("\nRanked teams:\n")
print(team1)
sleep(.5)
print(team2)
sleep(.5)
print(team3)
sleep(.5)
print(team4)
sleep(.5)
print(team5)
sleep(.5)
print(team6)
sleep(.5)
print(team7)
sleep(.5)
print(team8)
sleep(.5)
print(team9)
sleep(.5)
print(team10)
sleep(.5)
print(team11)
sleep(.5)
print(team12)
sleep(.5)
print(team13)
sleep(.5)
print(team14)
sleep(.5)
print(team15)
sleep(.5)
print(team16)
sleep(.5)

print("")
print("--------------------------------------------------------")
print('Round of 16:\n')

team01 = roundOf16(team1, team2)
sleep(.5)
team02 = roundOf16(team3, team4)
sleep(.5)
team03 = roundOf16(team5, team6)
sleep(.5)
team04 = roundOf16(team7, team8)
sleep(.5)
team05 = roundOf16(team9, team10)
sleep(.5)
team06 = roundOf16(team11, team12)
sleep(.5)
team07 = roundOf16(team13, team14)
sleep(.5)
team08 = roundOf16(team15, team16)
sleep(.5)


print("")
print("--------------------------------------------------------")
print('Round of 8:\n')



team001 = roundOf8(team01, team02)
sleep(.5)
team002 = roundOf8(team03, team04)
sleep(.5)
team003 = roundOf8(team05, team06)
sleep(.5)
team004 = roundOf8(team07, team08)
sleep(.5)

print("")
print("--------------------------------------------------------")
print('Round of 4:\n')


team0001 = roundOf4(team001, team002)
sleep(.5)
print("")
team0002 = roundOf4(team003, team004)

print("")
print('---------------------------------------')
print('Finals:\n')
print("")
sleep(1)
finals(team0001, team0002)

