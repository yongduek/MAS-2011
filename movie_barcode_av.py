# see https://pyav.org/docs/stable/cookbook/numpy.html

from PIL import Image
import numpy as np

import av
import av.datasets
from numpy.core.numeric import full

filename = av.datasets.curated('pexels/time-lapse-video-of-sunset-by-the-sea-854400.mp4')
print('filename:', filename)
container = av.open(filename)
container.streams.video[0].thread_type = 'AUTO'  # Go faster!

columns = []
for i, frame in enumerate(container.decode(video=0)):

    if i < 4:
        print(i, frame)

    array = frame.to_ndarray(format='rgb24')

    # Collapse down to a column.
    column = array.mean(axis=1)

    # Convert to bytes, as the `mean` turned our array into floats.
    column = column.clip(0, 255).astype('uint8')

    # Get us in the right shape for the `hstack` below.
    column = column.reshape(-1, 1, 3)

    columns.append(column)

# Close the file, free memory
container.close()

full_array = np.hstack(columns)
print(full_array.shape, columns[0].shape)

full_img = Image.fromarray(full_array, 'RGB')
full_img = full_img.resize((800, 200))
full_img.save('barcode.jpg', quality=85)