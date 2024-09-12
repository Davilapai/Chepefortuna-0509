__author__ = "David Alejandro Davila Guaranguay"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.davila@campusucc.edu.co"

#------------------------------------
# Importaciones (porfis, tienes q separarlos aca bien astetik)
# ----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT 

class SimuladorBancario: 
    
    #-----------------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------

    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #-----------------------------------------------------
    # Asociaciones
    #--------------------------------------------------------
    
    __cuentaAhorros=CuentaAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()

    #-----------------------------------------------------
    # Metodos
    #--------------------------------------------------------
    
    __method__ = "DepositarCuentaCorriete"
    __parameter__ = "monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"

    def DepositarCuentaCorriente(self, monto):
        self.__cuentaCorriente.ConsignarSaldo(monto)

    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Nignuno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcuar el saldo total en todas las cuentas"

    def CalcularSaldoTotal(self): 
        #Metodo 1
        # total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        # return total 
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = 'Ninguno'
    __returns__ = 'ninguno'
    __Description__ = 'Metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente'

    # Se usa el parametro cuando se maneja informacion que no está estipulada en ningun lado 
    def PasarAhorroACorriente(self): 
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros) 

    __method__ = "Ahorrar"
    __parameter__ = 'Niguno'
    __returns__ = 'Niguno'
    __Description__ = 'Metodo que permite pasar saldo de la cuenta corriente a la cuenta de ahorros'

    def Ahorrar(self): 
        saldoCorriente = self.__cuentaCorriente.DarSaldo()
        self.__cuentaCorriente.RetirarSaldo(saldoCorriente)
        self.__cuentaAhorros.ConsignarSaldo(saldoCorriente)

    __method__ = 'RetirarAhorros'
    __parameter__ = 'Monto'
    __returns__ = 'Ninguno'
    __Description__ = 'Metodo que permite retirar un monto de la cuenta de ahorros'

    def RetirarAhorros(self, monto): 
        self.__cuentaAhorros.RetirarSaldo(monto)
        
    __method__ = 'DarSaldoCorriente'
    __parameter__ = 'Ninguno'
    __returns__ = 'Saldo cuenta corriente'
    __Description__ = 'Metodo que retorna el saldo en cuenta corriente'

    def DarSaldoCorriente(self):
        return self.__cuentaCorriente.DarSaldo()

    __method__ = 'RetirarTodo'
    __parameter__= 'Ninguno'
    __returns__ = 'Ninguno'
    __Description__ = 'Metodo que permite retirar todo el diero de la cuenta'

    def RetirarTodo(self):
        self.__cuentaAhorros.RetirarSaldo(self.__cuentaAhorros.DarSaldo)
        self.__cuentaCorriente.RetirarSaldo(self.__cuentaCorriente.DarSaldo)

    __method__= 'DuplicarAhorro'
    __parameter__ = 'Ninguno'
    __returns__ = 'Ninguno'
    __Description__ = 'Metodo que permite duplicar el saldo de la cuenta de ahorros'

    def DuplicarAhorro(self):
        self.__cuentaAhorros.ConsignarSaldo(self.__cuentaAhorros.DarSaldo)
        


