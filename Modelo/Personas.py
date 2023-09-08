
class Persona:
    def __init__(self,cedula=None, pnombre = None,snombre=None, papellido=None,sapellido=None, telefono = None, email = None, tipo = None, estado = None):
        self.cedula=cedula
        self.pnombre = pnombre
        self.snombre= snombre 
        self.papellido=papellido
        self.sapellido=sapellido
        self.telefono = telefono
        self.email = email
        self.tipo = tipo
        self.estado = estado
        
    def get_id_persona(self):
        return self.id_persona
    def get_cedula(self):
        return self.cedula
    def set_cedula(self,cedula):
        self.cedula=cedula
    def get_Pnombre(self):
        return self.pnombre
    def set_Pnombre(self, pnombre):
        self.pnombre = pnombre
    def get_snombre(self):
        return self.snombre
    def set_Snombre(self, snombre):
        self.snombre = snombre
    def get_Papellido(self):
        return self.papellido
    def set_Papellido(self, papellido):
        self.papellido = papellido
    def get_Sapellido(self):
        return self.sapellido
    def set_Sapellido(self, sapellido):
        self.sapellido = sapellido
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
        
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado
    
    
