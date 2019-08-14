import os
import pypandoc
import sys
from PyPDF2 import PdfFileMerger

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

def removeDoubleSlash(filename):
  filetmpName = filename + ".tmp"
  filetmp = open(filetmpName, "w+")
  lines = open(filename, "r").readlines()
  for line in lines:
    filetmp.write(line.replace('\\\\', '\\'))

sidebars = open("website/sidebars.json").readlines()
pasteInfo = open("pasteInfo.txt", "w+")
for i in range(len(sidebars)):
  line = sidebars[i]
  if ("[" in line):
    filename = removeQuotes(line)
    i += 1
    print(filename)
    merger = PdfFileMerger()
    toPutNewPdfDir = ""
    while ("]" not in sidebars[i]):
      dir = removeQuotes(sidebars[i])
      noDocsDir = dir
      dir = "docs/" + dir
      if toPutNewPdfDir == "":
        rdir = noDocsDir[::-1]
        j = 0
        while j < len(rdir):
          if (rdir[j] == '/'):
            j += 1
            while j < len(rdir):
              toPutNewPdfDir += rdir[j]
              j += 1
          j += 1
        toPutNewPdfDir = toPutNewPdfDir[::-1]
        print ("-------New Dir------\n")
        print (toPutNewPdfDir, '\n')
        pasteInfo.write(toPutNewPdfDir + "\n")
      # Replace double slash (\\) with single one (\).
      removeDoubleSlash(dir + ".md")
      inFile = dir + ".md.tmp"
      outFile = dir + ".pdf"
      # --------- To use built pypandoc ----------
      # output = pypandoc.convert_file(inFile, format = 'md', to = 'pdf', outputfile = outFile)
      # print("-------------\n")
      # print(output)
      # print("-------------\n")
      # assert output == ""
      # -------- To use standard terminal ------------
      s = 'pandoc --pdf-engine=xelatex -s ' + inFile + " -o " + outFile 
      print(s)
      there = os.system(s)
      print("---- Return Value ------- ", there)
      if os.path.exists(inFile):
        os.remove(inFile)
      assert there == 0
      merger.append(outFile)
      # print(os.getcwd())
      i += 1
      merger.write(filename + ".pdf")
      pasteInfo.write(filename + ".pdf" + "\n")
    merger.close()
