import os


def removeQuotes(line):
  start = False
  filename = ""
  for c in line:
    if (c == "\"" and not start):
      start = True
      continue
    if (c == "\""):
      break
    if start:
      filename += c
  return filename

sidebars = open("website/sidebars.json").readlines()
for i in range(len(sidebars)):
  line = sidebars[i]
  if ("[" in line):
    filename = removeQuotes(line)
    i += 1
    print(filename)
    while ("]" not in sidebars[i]):
      dir = removeQuotes(sidebars[i])
      dir = "docs/" + dir
      s = 'pandoc -s ' + dir + ".md" + " -o " + dir + ".pdf"
      print(s)
      os.system(s)
      # print(os.getcwd())
      i += 1

# os.system('pandoc -s docs/courses.md -o docs/courses.pdf')