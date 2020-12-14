from kaggle_environments import make

env = make("mab", debug=True)
env.reset()
env.configuration['episodeSteps'] = 1
result = env.run(['submission.py', 'random_agent.py'])
print('-------------------')
print('FINAL RESULTS')
print('-------------------')
print('Agent 0: %i rewards' % result[-1][0]['reward'])
print('Agent 1: %i rewards' % result[-1][1]['reward'])
if result[-1][0]['reward'] > result[-1][1]['reward']:
    print('\nAgent 0 is the winner!!!')
elif result[-1][0]['reward'] < result[-1][1]['reward']:
    print('\nAgent 1 is the winner!!!')
else:
    print('\nIts a tie!!!')