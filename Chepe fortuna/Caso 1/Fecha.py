__author__ = "David Alejandro Davila"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.davila@campusucc.edu.co"

class Fecha : 
    # Aqui inicia la declaracion de mi clase
    """#---------------------------------------------------
    # Atributos
    ------------------------------#"""
    
    dia = 0
    mes = 0
    anio = 0 
    
    '''#-----------------------------------------------------
    # Metodos
    --------------------------------------------------------#'''
    
    __method__ = 'DarDia'
    __parameter__ = 'nignuno'
    __returns__ = 'Dia'
    __Description__ = 'Metodo que regresa el dia'
    
    def DarDia(self):
        return self.dia 
    
    
    __method__ = 'DarMes'
    __parameter__ = 'nignuno'
    __returns__ = 'Mes'
    __Description__ = 'Metodo que regresa el mes'
    
    def DarMes(self):
        return self.mes 
        
        
    __method__ = 'DarAnio'
    __parameter__ = 'nignuno'
    __returns__ = 'Anio'
    __Description__ = 'Metodo que regresa el anio'
    
    def DarAnio(self):
        return self.anio


    __method__ = 'Dar fecha'
    __parameter__ = 'Nignuno'
    __returns__ = 'la fecha de la clase'
    __Description__ = 'Metodo que regresa la fecha digitada por el usuario'
    
    def DarFecha(self): 
        return self.dia + '/' + self.mes + '/' + self.anio
