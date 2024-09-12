import pickle
import os
class Deserializador:
    
    @staticmethod
    def deserializar(file_name):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as file:
                return pickle.load(file)
        return None
