"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os
from chemprop.train import chemprop_predict

if __name__ == '__main__':
    print('now predicting')
    chemprop_predict()
    print('done predicting')
    #Remove features file after
    # os.remove('features.npz')
