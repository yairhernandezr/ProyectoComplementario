class Celda:
    def __init__(self, id_parqueadero = None,id_apartamento = None, numerocelda = None):
        self.id_parqueadero = id_parqueadero
        self.id_apartamento = id_apartamento
        self.numerocelda = numerocelda

    def get_id_parqueadero(self):
        return self.id_parqueadero
    
    def set_id_parqueadero(self, id_parqueadero):
        self.id_parqueadero = id_parqueadero
    
    def get_id_apartamento(self):
        return self.id_apartamento
    
    def set_id_apartamento(self, id_apartamento):
        self.id_apartamento = id_apartamento

    def get_numerocelda(self):
        return self.numerocelda

    def set_numerocelda(self, numerocelda):
        self.numerocelda = numerocelda
#Prueba
#if __name__ == '__main__':
#      celda1 = Celda()
#     celda1.set_id_celda(201)
#      celda1.set_id_parqueadero("B201")
#      print(celda1.get_id_parqueadero())
#     print(celda1.get_id_celda())
#     print(celda1.get_id_apartamento())
#     print(celda1.get_numerocelda())