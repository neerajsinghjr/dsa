from enum import Enum


class Season(Enum):
	spring = 1
	winter = 2
	autumn = 3
	summer_x = 4
	summer_y = 4

print("key:", Season.spring)
print("key: ", Season['summer_x'])
print("value: ", Season['summer_y'].value)
print("type: ", type(Season.spring))
print("repr: ", repr(Season.spring))

season_list = list(Season)
print("list in season: ", season_list)	
print("Season Obj: ", Season)

print("access key based on values : ", Season(4).name)
print("list in Season : ", (Season))

# Looping Season Values;;
for season in Season:
	print(season.name, "<->", season.value)