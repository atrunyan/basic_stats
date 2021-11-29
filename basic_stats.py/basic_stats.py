def basic_stats(x): #Input is a list x
    
    import matplotlib
    import matplotlib.pyplot as plt
    import random

    ## Create a variable with length of list x
    N = 0
    for n in x:
        N += 1

    mu = sum(x)/N

    squares = []
    for n in x:
        diff = n - mu
        sq = diff**2
        squares.append(sq)

    sumofSq = sum(squares)

    sigma = sumofSq**(1/2)/N-1

    plot = plt.hist(x)

    return(mu, sigma, plot) #outputs are mean (mu) and standard deviation (sigma)

    
