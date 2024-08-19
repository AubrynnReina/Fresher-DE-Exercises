import random

random.seed(42)
rand_nums = random.sample(range(30000000), 10000000)

with open('./data/prime.txt', 'w') as f:
    for num in rand_nums:
        f.write(str(num) + '\n')
