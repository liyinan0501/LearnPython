"""
TODO Case-Rock paper scissors
"""
import random

player = int(input("Select: 0--rock, 1--scissor or 2--paper "))
computer = random.randint(0, 2)
print(f"Computer: {computer} - Player:{player}")

# 玩家获胜的可能性：
if (
    ((player == 0) and (computer == 1))
    or ((player == 1) and (computer == 2))
    or ((player == 2) and (computer == 0))
):
    print("Player wins!!")
# 平局：
elif player == computer:
    print("Tie! Play again!")
# 电脑获胜：
else:
    print("Computer wins!!")
