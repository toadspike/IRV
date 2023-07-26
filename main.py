'''
This is a program to calculate the results of Instant Runoff Voting.
Ballots should be inputted as a nested list.
Each ballot is a list of the names of candidates in order of preference, from highest to lowest.
These are then combined into a large list in any order and inputted to the countVotes() function.
Results will be printed to the console.
This program doesn't break ties, so it may be unsuitable for very small elections.
26.07.2023
'''

def countVotes(ballots):
    tally = {}
    for i in ballots:
        if i[0] in tally:
            tally[i[0]] += 1
        else:
            tally[i[0]] = 1
    print("The tally is: " + str(tally).replace("'",""))
    if len(tally) == 2:
        winner = max(tally, key=tally.get)
        print(winner + " has won the election!")
        return(winner)
    else:
        eliminate(tally,ballots)

def eliminate(tally, ballots):
    elimCand = min(tally, key=tally.get) #https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
    for i in ballots:
        i.remove(elimCand)
    print(elimCand + " was eliminated.")
    countVotes(ballots)

if __name__ == '__main__':
    testBallots = [["Joe", "Sam", "Anne"], ["Joe", "Sam", "Anne"], ["Sam", "Joe", "Anne"], ["Anne", "Sam", "Joe"],
               ["Anne", "Joe", "Sam"]]
    countVotes(testBallots)