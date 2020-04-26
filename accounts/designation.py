list = """Office Boy
Driver
Draftman
Assistant
Sr Assistant
Secreatary
Executive
Sr Executive
Engineer
Graduate Trainee
GTE
Lead Engineer
Sr Engineer
Manager
Assistant Manager
Deputy Manager
Sr Manager
Chief Manager
General Manager
AVP
VP
DP
CEO
CMD
"""

list = list.split("\n")

final_string = ""

for i in list:
    single = "('"+i+"', '"+i+"'),"
    final_string = final_string + single

print(final_string)