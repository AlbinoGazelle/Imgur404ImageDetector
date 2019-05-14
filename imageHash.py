from PIL import Image
import imagehash
import os
#first get filenames in directory(done)
#then calculate the hash for each file(done)
#compare bad hash to list of all hashes
#delete any files that has bad hash
def find_images(userpaths, hashfunc = imagehash.average_hash):
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or \
                f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or '.jpg' in f

    image_filenames = []
    for userpath in userpaths:
        image_filenames += [os.path.join(userpath, path) for path in os.listdir(userpath) if is_image(path)]
    images = {}
    for img in sorted(image_filenames):
        try:
            hash = hashfunc(Image.open(img))
            print('Image:', img, 'Hash:', hash)
        except Exception as e:
            print('Problem:', e, 'with', img)
        if hash in images:
            print(img, ' already exists')

path = ['C:\\Test']
find_images(path)
