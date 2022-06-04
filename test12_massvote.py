"""
find the winner of the election
"""

def MassVote(candidates: int, votes: list) -> str:
    """
    - winner > 50% of votes - "majority winner" + №
    - winner hase most votes and <= 50% of the votes - "minority winner" + No.
    - several winners with the same number of votes identified - no winner
    :param candidates: number of candidates N >= 1
    :param votes: array containing N votes
    :return: winner's type and No
    """
    summa = 0
    value_max = 0
    dictionary = []
    key_max = 0
    flag = False
    # Count SUM of votes
    for vote in range(candidates):
        summa += votes[vote]

    # Fill array with %.
    for vote in votes:
        dictionary.append(round(vote * 100 / summa, 3))

    for i, value in enumerate(dictionary):
        if value == value_max:  # There are repetitions.
            flag = True
        if value > value_max:  # Find the maximum.
            value_max = value
            key_max = i  # Candidate number with maximum.
            flag = False

    if value_max > 50:
        return "majority winner " + str(key_max + 1)
    if value_max <= 50 and not flag:
        return "minority winner " + str(key_max + 1)

    return "no winner"
