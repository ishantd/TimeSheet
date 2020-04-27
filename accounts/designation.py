list = """Corporate
Finance
Business Development
Human Resource
Library
Document Control
Information Technology
Planning
Administration
Process
Quality
Mechanical
Projects
Instrumentation
Civil Structural
Procurement
Electrical
Piping
"""

list = list.split("\n")

final_string = ""

for i in list:
    single = "('"+i+"', '"+i+"'),"
    final_string = final_string + single

print(final_string)