def oddDiscord(balls):
    runs = 0
    con = 0
    for x in balls:
        if x%2 == 0:
            runs = runs + x
            con = con + 1
        else:
            runs = runs + x
            con = con + 1
            break
    del balls[0:con]
    return runs
balls = [1,2,3,2,1]

player1 = 0
player2 = 0
for y in range(6):
    if balls != []:
        p1 = oddDiscord(balls)
        player1 = player1 + p1
        p2 = oddDiscord(balls)
        player2 = player2 + p2

print('player1 runs is:', player1)
print('player2 runs is:', player2)