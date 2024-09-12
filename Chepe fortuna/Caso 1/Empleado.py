__author__ = "David Alejandro Davila"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.davila@campusucc.edu.co"

from Fecha import Fecha 

class Empleado: 
    # Aqui inicia la declaracion de mi clase
    """#---------------------------------------------------
    # Atributos
    ------------------------------#"""
    
    nombre = ""
    apellido = ""
    salario = 0 
    
    """#------------------------------------------
    # 1 = Masculino, 2 = Femenino
    ------------------------------------------------------#"""
    
    sexo = 0 
    
    """#---------------------------------------------------
    # Asociación 
    ------------------------------#"""
    
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()
    
    '''#-----------------------------------------------------
    # Metodos
    --------------------------------------------------------#'''
    
    def DarNombre(self): 
        # Aqui va mi codigo (recordar aumentar la sangria para que todos los returnados pertenezcan acá)    
        return self.nombre 
        
    # Estas son buenas practicas, no se hace en comentarios sino directamente
    __method__ = 'CambiarSalario'
    __parmeter__ = 'nuevoSalario'
    __returns__ = 'Salario'
    __description__ = " metodo que actualiza el salario del empleado " 
        
    def CambiarSalario(self, nuevoSalario): 
        # Aqui va mi codigo (el sistema asume que el salario es 0, por eso se imprementa el "nuevoSalario" para cambiarlo)
        self.DarSalario = nuevoSalario 
        # Al ir con parametros se le da una asignacion que en este caso es el propio parametro
    
    def DarSalario(self):
        # Aqui va mi codigo 
        return self.DarSalario 
    
    __method__ = 'ConsultarFechaIngreso'
    __parmeter__ = 'Ninguno'
    __returns__ = 'Fecha de ingreso'
    __description__ = " metodo que muestra la fecha de ingreso del empleado "

    def ConsultarFechaIngreso(self): 
        # Aqui va mi codigo 
        return self.fechaIngreso.DarFecha()
    
    __method__ = 'SalarioAnual'
    __parmeter__ = 'Ninguno'
    __returns__ = 'Salario anual'
    __description__ = " Muestra el salario anual del empleado "

    def CalcularSalarioAnual(self): 
        # Codigooo
        # Forma 1
        # total = self.salario*12
        # return total 
        # Forma 2
        return self.salario*12 
    
    __method__ = 'CalcularImpuestoSalarioAnual'
    __parmeter__ = 'Ninguno'
    __returns__ = 'Impuesto del salario anual'
    __description__ = " Muestra el impuesto del salario anual del empleado "

    def CalcularImpuestoSalarioAnual(self): 
        #Codigoo
        #Forma 1
        #salarioAnual = self.CalcularSalarioAnual()
        #impuestoAnual = salarioAnual * 0.19
        # return impuestoAnual 
        # Forma 2
        return self.calcularSalarioAnual()*0.19
    
    __method__ = 'CalcularImpuestoSalario'
    __parmeter__ = 'Ninguno'
    __returns__ = 'Impuesto del salario '
    __description__ = " Muestra el impuesto del salario  del empleado "

    def CalcularImpuestoMensual(self):
        return self.DarSalario()*0.19 
    
        
    
    
    
    
    
    
    
    

            