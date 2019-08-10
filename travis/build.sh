#!/bin/bash
echo '######################################'
echo '#                Build               #'
echo '#              - START -             #'
echo '######################################'

pandoc -s docs/courses.md -o docs/courses.pdf

echo '######################################'
echo '#                Build               #'
echo '#            - FINISHED -            #'
echo '######################################'