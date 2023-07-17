"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os
from chemprop.train import chemprop_predict

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
features_file =  os.path.abspath(os.path.join(root, "..","features.npz"))

if __name__ == '__main__': 
    chemprop_predict() 
    #Remove features file after
    os.remove(features_file)
