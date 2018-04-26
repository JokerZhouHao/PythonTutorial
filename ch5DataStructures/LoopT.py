



exit(0)

#dict循环
knight  = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knight.items():
    print(k, v)

#sequence循环
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#zip loop
questions = ['name', 'quest']
answers = ('zhou', 'an')
for qu, an in zip(questions, answers):
    print(qu, an)


#reversed/sorted循环
for i in range(5):
    print(i)






