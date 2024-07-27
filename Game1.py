#snake, water and gun game
import random
def swg(computer,mine):
    if (computer == mine):
        return None    
    if (computer == 'snake' and mine=='gun'):
        return True
    elif (computer == 'water' and mine=='snake'):
        return True
    elif (computer == 'gun' and mine=='water'):
        return True
    else:
        return False


choice=('snake','water','gun')
computer=random.randint(0,2)
computer=choice[computer]
mine=input('choose either snake, water or gun:')
win=swg(computer,mine)
if win is None:
    print("Match Drawn")
if win:
    print("you win")
else:
    print(f"you chose {mine} and the computer chose {computer}")
    print("you lose")
