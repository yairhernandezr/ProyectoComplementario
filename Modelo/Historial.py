class Historial:
    def __init__(self, id_automovil = None,id_camara = None ,fechahora = None):
    
        self.id_automovil = id_automovil
        self.id_camara=id_camara
        self.fechahora = fechahora

    def get_id_automovil(self):
        return self.id_automovil
    
    def set_id_automovil(self, id_automovil):
        self.id_automovil = id_automovil

    def get_id_camara(self):
        return self.id_camara
    
    def set_id_camara(self, id_camara):
        self.id_camara = id_camara

    def get_fechahora(self):
        return self.fechahora
    
    def set_fechahora(self, fechahora):
        self.fechahora = fechahora
