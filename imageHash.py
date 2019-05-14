from PIL import Image
import imagehash
import os
import json
import sys
import hashlib
from threading import Thread, Lock
#imgur404 image hash
badHash = 'c0fcfffefe00e040'
#define walk_dir as argument user gave when running script
walk_dir = sys.argv[1]
def find_images(userpaths, hashfunc = imagehash.average_hash):
    #only get hash of images
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or \
                f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or '.jpg' in f
    for root, subdirs, files in os.walk(walk_dir):
        for filename in files:
            result = is_image(filename)
            #if file is an image
            if result:
                try:
                    #define file_path
                    file_path = os.path.join(root, filename)
                    #get hash of file and convert to str
                    hash = str(hashfunc(Image.open(file_path)))
                    if hash in badHash:
                        print('Deleting Imgur404 Image!', file_path)
                        #delete file
                        os.remove(file_path)
                #for corrupted files(maybe in future delete those file? still need to do more testing)
                except Exception as e:
                    print('Problem', e, 'with', file_path, 'Maybe Corrupt File?')

find_images(walk_dir)
