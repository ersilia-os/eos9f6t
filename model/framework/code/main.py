# Entry point for eos9f6t: runs the same two steps as run.sh (RDKit 2D features, then
# chemprop prediction) with the intermediate features file in a temporary directory,
# so the model works from any working directory, including a read-only one (e.g. Apptainer).
import os
import shutil
import subprocess
import sys
import tempfile

input_file = os.path.abspath(sys.argv[1])
output_file = os.path.abspath(sys.argv[2])

root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

tmp_dir = tempfile.mkdtemp()
features_path = os.path.join(tmp_dir, "features")
try:
    subprocess.run(
        [
            sys.executable, os.path.join(root, "save_features.py"),
            "--data_path", input_file,
            "--save_path", features_path,
            "--features_generator", "rdkit_2d_normalized",
        ],
        check=True,
    )
    # argument order matters: predict.py reads the output path from sys.argv[7]
    # and the features file from sys.argv[-1]
    subprocess.run(
        [
            sys.executable, os.path.join(root, "predict.py"),
            "--no_features_scaling",
            "--test_path", input_file,
            "--checkpoint_dir", checkpoints_dir,
            "--preds_path", output_file,
            "--features_path", features_path + ".npz",
        ],
        check=True,
    )
finally:
    shutil.rmtree(tmp_dir, ignore_errors=True)
