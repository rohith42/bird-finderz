import os
from pathlib import Path
import urllib.request as request
import zipfile
from classifier import logger
from classifier.entity.config_entity import TrainedModelConfig
from classifier.utils.common import get_size, tqdmHook
from tqdm import tqdm

class GetTrainedModel:
    def __init__(self, config: TrainedModelConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            downloadfile = self.config.source.split('/')[-1]
            with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=downloadfile) as t:
                filename, headers = request.urlretrieve(
                    url=self.config.source,
                    filename=self.config.local_data_file,
                    reporthook=tqdmHook(t)
                )
            logger.info(f"{filename} downloaded with the following info: \n{headers}")
        else:
            logger.info(f"File already exists. Size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    def verify(self):
        modelpath = os.path.join(self.config.unzip_dir, "model.h5")
        status = {
            "path" : modelpath,
            "exists" : os.path.exists(modelpath),
            "size" : get_size(Path(modelpath))
        }
        return status