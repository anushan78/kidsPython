import random

easy_list = ['apple','ball','paper','talk','sleep','lines','dots']
hard_list = ['conventions','talkative','communication','taxonomy','independent','enormous','resilience']
random_word = random.choice(easy_list)
print(random_word)
answer = input('please type the above word')
print('you typed:', answer)
