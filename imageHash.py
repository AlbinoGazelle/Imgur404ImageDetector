from PIL import Image
import imagehash
import os
import json
#hash of imgur404 images
badHash = 'c0fcfffefe00e040'
def find_images(userpaths, hashfunc = imagehash.average_hash):
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or \
                f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or '.jpg' in f

    image_filenames = []
    for userpath in userpaths:
        image_filenames += [os.path.join(userpath, path) for path in os.listdir(userpath) if is_image(path)]
    for img in sorted(image_filenames):
        try:
            hash = hashfunc(Image.open(img))
            hash = str(hash)
        except Exception as e:
            print('Problem:', e, 'with', img)
        if hash in badHash:
            print('Deleting:', img, 'Because it has bad hash!')
            os.remove(img)

#for testing
#still need to add config file support
path = ['C:\\Test']
find_images(path)
