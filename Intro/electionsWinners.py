def electionsWinners(votes, k):
    if k == 0:
        max_votes = max(votes)
        if votes.count(max_votes) > 1:
            return 0
        else:
            return 1
    else:
        wins = 0
        max_votes = max(votes)
        for can in votes:
            if (can + k) > max_votes:
                wins += 1
        return wins


votes = [4, 1, 2, 2]
k = 0


print(electionsWinners(votes, k))