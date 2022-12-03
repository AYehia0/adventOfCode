# A for Rock, B for Paper, and C for Scissors.
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# + (0 if you lost, 3 if the round was a draw, and 6 if you won).

rules = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

rules2 = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def play_status(opp_play, my_play):
    """Win, lose, or draw"""
    if opp_play == "A" and my_play == "X" or opp_play == "B" \
            and my_play == "Y" or opp_play == "C" and my_play == "Z":
        return 3
    # lose
    if opp_play == "A" and my_play == "Z" or opp_play == "C" \
            and my_play == "Y" or opp_play == "B" and my_play == "X":
        return 0
    # win
    return 6


def calculate_score(opp_play, my_play):
    return rules[my_play] + play_status(opp_play, my_play)


def what_to_play(opp_play, des):
    """
    X means you need to lose, Y means you need to end the round in a draw,
    and Z means you need to win. Good luck!
    """
    lose = {
        "A": "Z",
        "C": "Y",
        "B": "X"
    }
    draw = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }
    win = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }
    if des == "X":
        return lose[opp_play]
    if des == "Y":
        return draw[opp_play]
    return win[opp_play]


with open("input.txt") as df:
    data = df.read()

    total_score1 = 0
    total_score2 = 0
    for play in data.split("\n")[:-1]:
        opp_play, my_play = play.split()

        total_score1 += calculate_score(opp_play, my_play)
        total_score2 += rules[what_to_play(opp_play, my_play)] \
            + rules2[my_play]

    print(f"Part 1 : {total_score1}")
    print(f"Part 2 : {total_score2}")
