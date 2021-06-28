import os

from keras.models import model_from_json
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import joblib
import numpy as np

#silence tensorflow compiler
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
import json
from pkg_resources import resource_filename


class Evx:
  json_model_path = resource_filename(__name__, 'neuwo_model.json') 
  model_weights_path = resource_filename(__name__, 'my_model_weights.h5') 
  model_scaler_path = resource_filename(__name__, 'scaler.gz') 


  def __init__(self,*args):
  	self.model_scaler_path = model_scaler_path

  @classmethod
  def loadmodel(cls):
    json_file = open(f'{cls.json_model_path}', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(f'{cls.model_weights_path}')
    return loaded_model


  @classmethod
  def prepareInput(cls,opening,closing,volume):
  	#scaler = cls.model_scaler_path
  	ask_ind = opening*volume/(opening + closing)
  	bid_ind = closing*volume/(opening + closing)
  	testdata = np.array([[ask_ind,bid_ind]])
  	scaler = joblib.load(f'{cls.model_scaler_path}')
  	testdata = scaler.transform(testdata)

  	return testdata


  @classmethod
  def buySignalGenerator(cls,opening,closing,volume,alpha):
    scalledInput = cls.prepareInput(opening,closing,volume)
    return (cls.loadmodel().predict(scalledInput) > alpha).astype("int32")[0][0]
    
  @classmethod
  def sellSignalGenerator(cls,opening,closing,volume,alpha):
    scalledInput = cls.prepareInput(opening,closing,volume)
    return (cls.loadmodel().predict(scalledInput) <= alpha).astype("int32")[0][0]



