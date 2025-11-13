import os
import sys
import pickle

from src.exception import StudentPerformanceException
from src.logger import logging
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        
        # 'wb': signifies opening a file for writing in binary mode.
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise StudentPerformanceException(e,sys)

def evaluate_models(X_train, y_train, X_test,y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            # Perform GridSearchCV
            gs = GridSearchCV(model, para, cv=3)
            # Run the grid search / 
            gs.fit(X_train,y_train)
            
            # Applying/Updating the best parameters to the model
            model.set_params(**gs.best_params_)
            # Train the model with best parameters
            model.fit(X_train,y_train)

            # Prediction
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Evaluate the model wiht R2 Error Score
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

            return report
        
    except Exception as e:
        raise StudentPerformanceException(e,sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise StudentPerformanceException(e,sys)
    

