class Apartamento:
    """Clase Apartamento
    los atributos de la clase son:
    id_apartamento la llave primaria que identifica al apartamento
    bloque : identifica al bloque, A, B, C
    numero: identifica el apartamento A-201
    """
    def __init__(self, id_apartamento =None ,Bloque = None, numero = None, id_persona = None):
        self.id_apartamento=id_apartamento
        self.bloque = Bloque
        self.numero = numero
        self.id_persona = id_persona
    
    def get_id_apartamento(self):
        return self.id_apartamento
    

    
    def get_Bloque(self):
        return self.Bloque
    
    def set_Bloque(self, Bloque):
        self.Bloque = Bloque
    
    def get_Numero(self):
        return self.numero
    
    def set_Numero(self, numero):
        self.numero = numero
    
    def get_id_persona(self):
        return self.id_persona
    
    def set_id_persona(self, id_persona):
        self.id_persona = id_persona
