import glob
from dominate import document
from dominate.tags import *
import sys

# Script that creates an html file that displays all images of a specified folder.
# Styles could be supplied via styles.css file.
# -----------------------
# prerequisite: dominate
# pip install dominate OR pip install --no-cache-dir -r requirements.txt
# -----------------------
# inputs:
# 1: input directory (folder containing images)
# 2: document title (header displayed on top)

inputDirectory = "../../Assets/Illustrations"
documentTitle = "The Liberators Illustrations"

if len(sys.argv) == 3:
    print('Using custom input directory and document title')
    inputDirectory = sys.argv[1]
    documentTitle = sys.argv[2]

print('Input Directory: ', inputDirectory)
print('Document Title: ', documentTitle)

images = glob.glob(inputDirectory + '/*')

with document(title=documentTitle) as doc:
    h1(documentTitle)
    for path in images:
        span(img(src=path, style="width:30%"), _class='photo')

with doc.head:
    link(rel='stylesheet', href='style.css')


with open('index.html', 'w') as f:
    f.write(doc.render())