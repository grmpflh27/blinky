from PIL import Image
import numpy as np


BELLY_COLOR = (216, 216, 216)
BELLY_DARK = (164, 161, 126)


if __name__ == "__main__":
    im = Image.open('totoroOrig.jpg')
    orig = np.asarray(im)
    
    
    edit = np.copy(orig)

    #r, g, b = orig[:, :, 0], orig[:, :, 1], orig[:, :, 2] 

    for i in range(orig.shape[0]):
        for j in range(orig.shape[1]):
            if np.array_equal(orig[i, j, :], BELLY_COLOR):
                edit[i, j, :] = [33, 150, 243]

    Image.fromarray(edit).save('totoroBlue.jpg')

    
