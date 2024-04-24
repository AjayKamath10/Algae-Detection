import pandas as pd
import argparse
from sentinel import fetch_sentinel_image
from preprocess import preprocess_image
from algorithm import estimate_cyanobacteria_density

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df[['latitude', 'longitude', 'date']]

def save_metadata_and_predictions(df, predictions, keep_metadata):
    if keep_metadata:
        df.to_csv('metadata.csv', index=False)
        pd.DataFrame(predictions, columns=['Estimated Cyanobacteria Density']).to_csv('preds.csv', index=False)
    else:
        pd.DataFrame(predictions, columns=['Estimated Cyanobacteria Density']).to_csv('preds.csv', index=False)

def main():
    parser = argparse.ArgumentParser(description='Predict cyanobacteria density from satellite images.')
    parser.add_argument('file', type=str, help='Path to the CSV file containing latitude, longitude, and date.')
    parser.add_argument('--keep-metadata', action='store_true', help='Save metadata and predictions to separate CSV files.')
    
    args = parser.parse_args()
    
    data = read_csv_file(args.file)
    
    images = []
    preprocessed_images = []
    
    for (latitude, longitude, date) in data:
        images.append(fetch_sentinel_image((latitude, longitude, date)))
    
    predictions = []
    
    for image in images:
        preprocessed_images.append(preprocess_image(image))
    
    save_metadata_and_predictions(data, predictions, args.keep_metadata)
    
    

if __name__ == '__main__':
    main()