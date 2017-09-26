import re 



pat = "RT-17515 RT-17014 RT-17013"
patten = r'RT-[0-9]{5}'
match = re.findall(patten,pat)
print(match)

