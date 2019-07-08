def reachNextLevel(experience, threshold, reward):
    return experience + reward >= threshold


experience = 10
threshold = 15
reward = 4

print(reachNextLevel(experience, threshold, reward))