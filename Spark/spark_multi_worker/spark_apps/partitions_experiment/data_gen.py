import random

random.seed(42)
rand_nums = random.sample(range(5000000), 5000000)

with open('./data/prime_5tr.txt', 'w') as f:
    for num in rand_nums:
        f.write(str(num) + '\n')
