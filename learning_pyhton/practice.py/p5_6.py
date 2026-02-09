import random

def get_cpu_choice():
    choices = ["グー", "チョキ", "パー"]
    return random.choice(choices)

def determine_winner(user, cpu):
    if user == cpu:
        return "あいこ"
    elif (
    (user == "グー" and cpu == "チョキ")
    or (user == "チョキ" and cpu == "パー")
    or (user == "パー" and cpu == "グー")
    ):
        return "ユーザ"
    else:
        return "CPU"

user_wins = 0
cpu_wins = 0
round_count = 0

while user_wins < 2 and cpu_wins < 2:
    user_hand = input("グー、チョキ、パーのいずれかを入力: ")
    if user_hand not in ["グー", "チョキ", "パー"]:
        print("正しい手を入力してください")
    else:
        cpu_hand = get_cpu_choice()
    print(f"ユーザ: {user_hand}, CPU: {cpu_hand}")
    result = determine_winner(user_hand, cpu_hand)

    if result == "あいこ":
        print("あいこです")
    elif result == "ユーザ":
        print("ユーザの勝ち")
        user_wins += 1
        round_count += 1
    else:
        print("CPU の勝ち")
        cpu_wins += 1
        round_count += 1
    print(f"現在のスコア - ユーザ: {user_wins}勝, CPU: {cpu_wins}勝")
    print()

if user_wins == 2:
    print("ユーザの勝ち")
else:
    print("CPU の勝ち")