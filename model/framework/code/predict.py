"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os, sys
import pandas as pd
from chemprop.train import chemprop_predict



#intermediate features file created
features_file = sys.argv[-1]
output_file = sys.argv[7]

if __name__ == '__main__':
    chemprop_predict()
    df = pd.read_csv(output_file)
    df = df[["activity"]]
    df.to_csv(output_file, index=False)
    #Remove intermediate features file after making predictions
    os.remove(features_file)
