import random

random.seed(42)
rand_nums = random.sample(range(10000000), 5000000)

with open('./data/prime.txt', 'w') as f:
    for num in rand_nums:
        f.write(str(num) + '\n')
