import os

def escapeSpace(fileName):
  i = 0
  retFileName = ""
  while i < len(fileName):
    if (fileName[i] == " "):
      retFileName += "\\"
    retFileName += fileName[i]
    i += 1
  return retFileName

os.chdir('/tmp')
os.system('git clone https://${GH_OAUTH_TOKEN}@github.com/${GH_USER_NAME}/${GH_PROJECT_NAME} pdfs 2>&1')
os.chdir('pdfs/')

travisBuildDir = os.environ["TRAVIS_BUILD_DIR"]
pasteInfoLines = open(travisBuildDir + "/pasteInfo.txt", "r").readlines()

i = 0
while i < len(pasteInfoLines):
  dir = pasteInfoLines[i]
  if (i + 1 >= len(pasteInfoLines)):
    break
  fileName = pasteInfoLines[i + 1]
  fileName = escapeSpace(fileName)
  print("Copying filename: ", fileName, " to the directory: ", dir, "\n")

  os.system("mkdir -p " + dir)
  if (os.path.exists(travisBuildDir + "/" + fileName)):
    print("Executing: ", "cp $TRAVIS_BUILD_DIR/" + fileName + " ./" + dir + "/" + fileName)
    os.system("cp $TRAVIS_BUILD_DIR/" + fileName + " ./" + dir + "/" + fileName)
  i += 2


os.system('git config --global user.name $GIT_AUTHOR_NAME')
os.system('git config --global user.email $GIT_AUTHOR_EMAIL')
os.system('git config --global push.default matching')

os.system('git add -A')
os.system('git commit -m \"Adding latest build of pdf to pdfs repo\"')
os.system('git push https://${GH_OAUTH_TOKEN}@github.com/${GH_USER_NAME}/${GH_PROJECT_NAME} 2>&1')
