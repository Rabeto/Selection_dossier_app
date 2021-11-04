from django.apps import AppConfig
import os
import joblib
from django.conf import settings

class CrudappConfig(AppConfig):
    name = 'CrudApp'
    MODEL_FILE = os.path.join(os.path.join('ml/model'), "ML_KNeighborsModel-1.joblib")
    model = joblib.load(MODEL_FILE)
