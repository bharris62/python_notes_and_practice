# Use a while loop to solve the following problem: A slow, but determined, walker sets off from
# Leicester to cover the 102 miles to London at 2 miles per hour. Another walker sets off from
# London heading to Leicester going at 1 mile per hour. Where do they meet?


not_met = True
from_leicester = 102
from_london = 0

while True:
    from_leicester -= 2
    from_london += 1

    if from_leicester == from_london:
        print("The two walkers met at {} mile from London and {} mile from Leicester".format(from_london,
                                                                                             (102 - from_leicester)))
        break
