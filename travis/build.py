import os

sidebars = open("website/sidebars.json").readlines()
for line in sidebars:
  print(line)

# os.system('pandoc -s docs/courses.md -o docs/courses.pdf')