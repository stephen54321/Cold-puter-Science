import random
numAttemps = random.randint(1,100)
attempts = numAttemps
print (attempts)
numBased = random.sample(range(-1000000, 1000000), attempts)
result = numBased
print (result)
answer = 0
for number in result:
    if int(number) < 0:
        answer += 1
print (answer)