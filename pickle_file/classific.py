import os
import pickle
import random

import numpy as np
import pandas as pd
import sklearn.model_selection as ms

class Classific:
    
    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.model_rf = pickle.load(open(os.path.join(curr_dir, 'rf_model.pkl'), 'rb'))
        #self.model_dt = pickle.load(open(os.path.join(curr_dir, 'dt_model.pkl'), 'rb'))
        #self.model_svc = pickle.load(open(os.path.join(curr_dir, 'svc_model.pkl'), 'rb'))
        
    def classify_rf(self, data: pd.DataFrame):
        return self.model_rf.predict(data)
    
    #def classify_dt(self, data: pd.DataFrame):
    #    return self.model_dt.predict(data)
        
    #def classify_rf(self, data: pd.DataFrame):
    #    return self.model_svc.predict(data)
        
    def classify(self, **kwargs):
        data = {
            "gender":      [kwargs['gender']],
            "age":         [kwargs['age']],
            "height":      [kwargs['height']],
            "weight":      [kwargs['weight']],
            "bmi":         [kwargs['bmi']],
            "employ_info": [kwargs['employ_info']],
            "insur_info":  [kwargs['insur_info']],
            "fam_hist":    [kwargs['fam_hist']],
            "med_hist":    [kwargs['med_hist']],
            "med_key":     [kwargs['med_key']]
        }
        data = pd.DataFrame(data)
        
        result_rf = self.classify_rf(data)
        #result_dt = self.classify_dt(data)
        #result_svc = self.classify_svc(data)
                
        return result_rf#, result_dt, result_svc
        
        