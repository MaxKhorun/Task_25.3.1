"""
list = ['Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×', 'Pet Friend N1', 'friend', '2', '×']
# print(len(list))
# print(list, '\n',
#       list[1::4], '\n',
#       list[2::4], '\n',
#       list[3::4], '\n',
#       list[::4], '\n')

# dict_with_pets = {
#         'names': [list_of_pets[it].text for it in range(0, len(list_of_pets), 4)],
#         'breed': [list_of_pets[it].text for it in range(0, len(list_of_pets), 1)]
#                       }

dict_with_pets = {
        'names': list[::4],
        'breed': list[1::4]
                      }
print(dict_with_pets['names'], '\n',
      dict_with_pets['breed'])
# print(set(dict_with_pets['names']))
"""

lis = {'names': [i for i in range(10)]}
print(lis['names'])
print(set(lis['names']))

print(len(lis['names']) == len(set(lis['names'])))
print(lis['names'] == len(set(lis['names'])))