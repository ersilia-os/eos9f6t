"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os, sys
from chemprop.train import chemprop_predict

#intermediate features file created
features_file = sys.argv[-1]

if __name__ == '__main__':
    chemprop_predict()
    #Remove intermediate features file after making predictions
    os.remove(features_file)
