import rasterio
import numpy as np
from datetime import datetime

def select_image_with_min_clouds(image_paths, cloud_threshold=0.05):
    min_cloud_image = None
    min_cloud_percentage = 1.0 # Start with a high value

    for path in image_paths:
        with rasterio.open(path) as src:
            # Assuming the cloud mask band is the last band
            cloud_mask = src.read(src.count)
            cloud_pixels = np.count_nonzero(cloud_mask)
            total_pixels = cloud_mask.size
            cloud_percentage = cloud_pixels / total_pixels

            if cloud_percentage < min_cloud_percentage:
                min_cloud_percentage = cloud_percentage
                min_cloud_image = path

    return min_cloud_image #most recent image with less than 5% cloud coverage.


def filter_water_pixels(image_path, scl_band_value=9): #Filter Pixels to Water Area Using the Scene Classification (SCL) Band
    with rasterio.open(image_path) as src:
        scl_band = src.read(1) # Assuming SCL band is the first band
        water_mask = scl_band == scl_band_value
        return water_mask

