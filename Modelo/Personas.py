
class Persona:
    def __init__(self,id_persona=None, nombre = None, telefono = None, email = None, estado = None, tipo = None):
        self.id_persona=id_persona
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.estado = estado
        self.tipo = tipo
    def get_id_persona(self):
        return self.id_persona
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
    
    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo
