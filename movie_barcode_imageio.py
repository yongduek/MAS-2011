#
import numpy as np
import imageio
import os 
from pathlib import Path
import skimage 

cwd = os.path.dirname(__file__)
print('cwd: ', cwd)

filename = Path(cwd) / 'pixels/time-lapse-video-of-sunset-by-the-sea-854400.mp4'
print(filename)

reader = imageio.get_reader(filename)
print('len:', reader.get_length())
print(reader.get_meta_data())

columns = []
for i, frame in enumerate(reader):

    array = frame # just rename, nothing

    # Collapse down to a column.
    column = array.mean(axis=1)
    if i < 3: print(column.shape)

    # Convert to bytes, as the `mean` turned our array into floats.
    column = column.clip(0, 255).astype('uint8')

    # Get us in the right shape for the `hstack` below.
    column = column.reshape(-1, 1, 3)

    if i < 3: 
        print(i, frame.shape, type(frame), column.shape)

    columns.append(column)
#
full_array = np.hstack(columns)
print(len(columns), full_array.shape)

from skimage import transform
full_array = transform.resize(full_array, (200,800))
print(full_array.dtype)

from skimage import util 
full_array = util.img_as_ubyte(full_array)

imageio.imwrite('barcode_imageio.jpg', full_array)