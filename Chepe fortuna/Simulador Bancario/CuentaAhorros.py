__author__ = "David Alejandro Davila Guaranguay"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "david.davila@campusucc.edu.co"

class CuentaAhorros :
     #------------------------------------------
    # Atributos
    # -----------------------------------------------

    __saldo = 0.0
    __interes = 0

    #-----------------------------------------------------
    # Metodos
    #--------------------------------------------------------

    __method__ = 'ConsignarValor'
    __parmeter__ = 'Monto'
    __returns__ =  'Valor'
    __description__ = " Metodo que actualiza el valor de la cuenta de ahorros "
    
    def ConsignarSaldo(self, monto): 
        # Aqui va mi codigo
        self.__saldo = self.__saldo + monto
        # en este caso el monto no lleva self porque es una llamada local, osea que dentro del adefinicion ya se contempla
        # mientras que el self.__saldo es una llamada general, que se contempla dentro de otras def 


    __method__ = 'DarSaldo'
    __parmeter__ = 'nignuno'
    __returns__ =  'Saldo de la cuenta'
    __description__ = " Metodo que retorna el saldo de la cuenta del cliente "

    def DarSaldo(self): 
        # Aqui va mi codigo
        return self.__saldo
        
        
    __method__ = 'RetirarValor'
    __parmeter__ = 'monto'
    __returns__ = 'Valor a retirar'
    __description__ = " Metodo que retorna el valor a retirar "    
        
    def RetirarSaldo(self, monto):    
        # Aqui va mi codigo
        self.__saldo = self.__saldo - monto