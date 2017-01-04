import subprocess
import glob2
import os
import sys

root = "site/content"
prefix = "t190_"
types = ('**/*.png', '**/*.jpg', '**/*.jpeg' ) # the tuple of file types
abs_path = os.path.abspath(sys.path[0])

print os.getcwd()

files = []
for pattern in types:
    files.extend(glob2.glob(os.path.join( root, pattern )))
    
for image in files:
    source_file = os.path.join( abs_path, image )
    target_file = os.path.join( abs_path, os.path.dirname( image ), prefix + os.path.basename(image) )
    print source_file, " -> ", target_file

    params = ['/usr/local/bin/convert', '-thumbnail', '190', source_file, target_file]
    subprocess.check_call(params)
#
# find . -iname *.jpg -o -iname *.png -o -iname *.jpeg
#
# convert -thumbnail 190 infile outfile