from __future__ import annotations
import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path: str)-> None:
        self.file_path = file_path

    def load_data(self)-> pd.DataFrame:
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        raise FileNotFoundError(f"File Not Found : {self.file_path}")