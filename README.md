# Predict algae density using data from satellite images 

This repository contains the code and instructions for using the Algae Detection tool. The tool is designed to predict the presence of algae in a given location and date using satellite imagery and machine learning models.

## Usage

Follow these steps to set up and use the Algae Detection tool:

```bash
# Clone the Repository
git clone https://github.com/AjayKamath10/Algae-Detection
```

# Install Conda
Conda is a package management system that allows you to install and manage software packages and their dependencies. 
Download and install Conda from the official website.

# Create a Conda Environment
Create a new Conda environment with Python 3.10. Replace `envname` with the name you want to give to your environment.
```
conda create -n envname python=3.10
```
# Deactivate the Current Environment
Before activating the new environment, deactivate the current Conda environment if you are in one.
```
conda deactivate
```

# Activate the New Environment
Activate the newly created Conda environment.
```
conda activate envname
```

# Predicting a Point
To predict the presence of algae at a specific point, use the `cyfi predict-point` command with the latitude, longitude, and date as arguments.
```
cyfi predict-point --lat 41.2 --lon -73.2 --date 2023-09-14
```

# Predict from CSV
To predict the presence of algae for multiple points listed in a CSV file, use the `cyfi predict` command with the CSV file path and the `--keep-metadata` option.
```
cyfi predict sample_points.csv --keep-metadata
```

# Visualize Results
To visualize the results of your predictions, use the `cyfi visualize` command followed by the folder name containing the prediction results.
```
cyfi visualize foldername/
```
