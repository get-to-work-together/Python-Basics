
shopping_list = ['eggs', 'butter']

shopping_list.append('milk')
shopping_list.append('bread')

shopping_list.insert(0, 'beer')
shopping_list.insert(1, 'wine')

print( shopping_list )

print( f"Don't forget {shopping_list[0]}!" )
print( f"Don't forget {shopping_list[-1]}!" )

shopping_list.sort()
print( shopping_list )

shopping_list.extend(['cola', '7-up', 'orangejuice', 'cola', 'cola'])
shopping_list = shopping_list + ['cola', '7-up', 'orangejuice', 'cola', 'cola']

# print( shopping_list.pop() )
# print( shopping_list.pop(3) )
# print( shopping_list )

shopping_list.remove('butter')
# shopping_list.remove('butter')  # does not work
print( shopping_list )

print( shopping_list.index('bread') )

