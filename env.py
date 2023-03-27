import os
import sys
from google.colab import drive


def drive_env(env_name: str = 'drive_env')-> None:
    drive.mount('/content/mnt', force_remount=True)
    nb_path = '/content/notebooks'
    os.symlink(f'/content/mnt/My Drive/Colab Notebooks/{env_name}/', nb_path)
    sys.path.insert(0, nb_path)
