import pickle
#Clase que serializa los objetos
class Serializador:
    
    @staticmethod
    def serializar(objetos, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(objetos, file)