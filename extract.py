import pandas as pd

class Extract:
    def extract_info(self,path):
        print("path is formed" + path)
        data = pd.read_csv(path)
        return data