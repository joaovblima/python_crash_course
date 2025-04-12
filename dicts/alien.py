alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}")
point_value = alien_0.get('points', "no have point field")
print(point_value)