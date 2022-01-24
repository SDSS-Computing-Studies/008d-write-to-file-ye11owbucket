import json
f = open("zzhomework.txt", "w")
grade1 = 80
grade2 = 80
grade3 = 80
grade4 = 80
grade5 = 80
grade6 = 80
grade7 = 80
grade8 = 80
grade1n = 'French'
grade2n = 'Gym' 
grade3n = 'Math' 
grade4n = 'Science'
grade5n = 'Socials'
grade6n = 'English'
grade7n = 'Computer'
grade8n = 'WorkStudies' 
gradeGrades = [grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8]
gradeNames = [grade1n,grade2n,grade3n,grade4n,grade5n,grade6n,grade7n,grade8n]
on = json.dumps(gradeNames)
og = json.dumps(gradeGrades)
f.write(on)
f.write('\n')
f.write(og)