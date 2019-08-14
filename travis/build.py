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

sidebars = open("website/sidebars.tmp.json").readlines()
pasteInfo = open("pasteInfo.txt", "w+")
currentDir = os.getcwd()
for i in range(len(sidebars)):
  line = sidebars[i]
  if ("[" in line):
    filename = removeQuotes(line)
    i += 1
    print("Working on: ", filename, "\n")
    merger = PdfFileMerger()
    toPutNewPdfDir = ""
    while ("]" not in sidebars[i]):
      dir = removeQuotes(sidebars[i])
      noDocsDir = dir
      dir = "docs/" + dir
      fileToConvert = ""
      if toPutNewPdfDir == "":
        rdir = noDocsDir[::-1]
        j = 0
        while j < len(rdir):
          if (rdir[j] == '/'):
            j += 1
            while j < len(rdir):
              toPutNewPdfDir += rdir[j]
              j += 1
          else:
            fileToConvert += rdir[j]
          j += 1
        fileToConvert = fileToConvert[::-1]
        toPutNewPdfDir = toPutNewPdfDir[::-1]
        print ("------- New Dir where file will be saved ------\n")
        print (toPutNewPdfDir, '\n')
        pasteInfo.write(toPutNewPdfDir + "\n")
        print ("------- Converting file ------\n")
        print (fileToConvert, '\n')
        os.chdir("docs/" + toPutNewPdfDir)
      # Replace double slash (\\) with single one (\).
      removeDoubleSlash(fileToConvert + ".md")
      inFile = fileToConvert + ".md.tmp"
      outFile = fileToConvert + ".pdf"
      # --------- To use built pypandoc ----------
      output = pypandoc.convert_file(inFile, format = 'md', to = 'pdf', outputfile = outFile)
      print("------ Output Begin -------\n")
      print(output)
      print("------ Output End ------\n")
      assert output == ""
      # -------- To use standard terminal ------------
      # s = 'pandoc --pdf-engine=xelatex -s ' + inFile + " -o " + outFile 
      # print(s)
      # there = os.system(s)
      # print("---- Return Value ------- ", there)
      if os.path.exists(inFile):
        os.remove(inFile)
      # assert there == 0
      merger.append(outFile)
      # print(os.getcwd())
      i += 1
    os.chdir(currentDir)
    merger.write(filename + ".pdf")
    pasteInfo.write(filename + ".pdf" + "\n")
    merger.close()
