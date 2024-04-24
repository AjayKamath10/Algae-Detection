import pandas as pd
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_algae_detection_models(sat_csv_path, elevation_csv_path, coun_csv_path, target_column):
    # Load data
    sat_data = pd.read_csv(sat_csv_path)
    elevation_data = pd.read_csv(elevation_csv_path)
    coun_data = pd.read_csv(coun_csv_path)
    
    # Merge data
    data = pd.merge(sat_data, elevation_data, on=['latitude', 'longitude'], how='inner')
    data = pd.merge(data, coun_data, on=['latitude', 'longitude'], how='inner')
    
    # Prepare features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train CatBoost model
    cat_boost_model = CatBoostClassifier(verbose=0)
    cat_boost_model.fit(X_train, y_train)
    cat_boost_model.save_model('cat_boost_model.cbm')
    
    # Train LightGBM model
    lgb_model = LGBMClassifier()
    lgb_model.fit(X_train, y_train)
    lgb_model.save_model('lgb_model.txt')
    
    # Train XGBoost model
    xgb_model = XGBClassifier()
    xgb_model.fit(X_train, y_train)
    xgb_model.save_model('xgb_model.json')
    
    accuracy_dict = {}
    
    # Evaluate models

    for model, model_name in zip(models, model_names):
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        

        uid_accuracy_df = pd.DataFrame({'uid': X_test['uid'], 'accuracy': [accuracy] * len(X_test)})

        uid_accuracy_df = uid_accuracy_df.groupby('uid').mean().reset_index()
        accuracy_dict[model_name] = uid_accuracy_df.to_dict('records')
    
    # Write the accuracy dictionary to the output file
    with open(output_file, 'w') as f:
        f.write(str(accuracy_dict))


