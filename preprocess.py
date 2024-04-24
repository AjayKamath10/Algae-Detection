import rasterio
import numpy as np
from sklearn.cluster import KMeans
from rasterio.plot import show
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
        


def kmeans_lake_detection(image_path, num_clusters=2):
    # Read the image
    with rasterio.open(image_path) as src:
        image = src.read(1) # Assuming the image is single-band
    
    # Preprocess the image if necessary
    # For example, normalize pixel values
    image = image / np.max(image)
    
    # Reshape the image to be compatible with KMeans
    image = image.reshape(-1, 1)
    
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(image)
    
    # Filter the image to keep only the lake area
    # Assuming the lake is the largest cluster
    lake_label = np.argmax(np.bincount(kmeans.labels_))
    lake_mask = kmeans.labels_ == lake_label
    
    # Reshape the mask back to the original image shape
    lake_mask = lake_mask.reshape(src.shape[0], src.shape[1])
    
    # Return the filtered image
    return lake_mask
    
def preprocess_image(image):
    MinCloudImage = filter_water_pixels(select_image_with_min_clouds(image))
    lake_mask = kmeans_lake_detection(MinCloudImage)
    return np.array(lake_mask)

