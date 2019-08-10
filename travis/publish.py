import os

os.chdir('/tmp')
os.system('git clone https://${GH_OAUTH_TOKEN}@github.com/${GH_USER_NAME}/${GH_PROJECT_NAME} pdfs 2>&1')
os.chdir('pdfs/')

# os.system('mkdir -p dist')
os.system('cp $RESULT_PDF_PATH ./courses.pdf')

os.system('git config --global user.name $GIT_AUTHOR_NAME')
os.system('git config --global user.email $GIT_AUTHOR_EMAIL')
os.system('git config --global push.default matching')

os.system('git add -A')
os.system('git commit -m \"Adding latest build of pdf to pdfs repo\"')
os.system('git push https://${GH_OAUTH_TOKEN}@github.com/${GH_USER_NAME}/${GH_PROJECT_NAME} 2>&1')