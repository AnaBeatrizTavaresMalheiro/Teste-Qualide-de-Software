import math

class Calculadora :

    def __init__ ( self ):
        self . historico = []
        self . resultado = 0

    def somar ( self , a, b):
        if not isinstance (a, (int , float )) or not isinstance (b, (int , float )):
            raise TypeError (" Argumentos devem ser numeros ")
        resultado = a + b
        self . historico . append (f"{a} + {b} = { resultado }")
        self . resultado = resultado
        return resultado

    def subtrair ( self , a, b):
        if not isinstance (a, (int , float )) or not isinstance (b, (int , float )):
            raise TypeError (" Argumentos devem ser numeros ")
        resultado = a - b
        self . historico . append (f"{a} - {b} = { resultado }")
        self . resultado = resultado
        return resultado

    def multiplicar ( self , a, b):
        if not isinstance (a, (int , float )) or not isinstance (b, (int , float )):
            raise TypeError (" Argumentos devem ser numeros ")
        resultado = a * b
        self . historico . append (f"{a} * {b} = { resultado }")
        self . resultado = resultado
        return resultado

    def dividir ( self , a, b):
        if not isinstance (a, (int , float )) or not isinstance (b, (int , float )):
            raise TypeError (" Argumentos devem ser numeros ")
        
        # Verificação de zero ou valores extremamente pequenos
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        if abs(b) < 1e-300:  
        # Ajuste: evita divisões por números muito próximos de zero
        # Evita resultados numéricos extremamente grandes que podem causar overflo
            raise ValueError("Divisão por zero não é permitida")

        resultado = a / b

        # Ajuste: se o resultado for inteiro (ex: 5.0), converte para int
        if resultado.is_integer():
            resultado_formatado = int(resultado)
        else:
            resultado_formatado = resultado

        self.historico.append(f"{a} / {b} = {resultado_formatado}")
        self.resultado = resultado
        return resultado

    def potencia ( self , base , expoente ):
        if not isinstance (base , (int , float )) or not isinstance ( expoente , (int ,
        float )):
            raise TypeError (" Argumentos devem ser numeros ")
        #|*Sugestão de melhoria : 0^0 deve se apresentada como uma indeterminação 
        if base == 0 and expoente == 0:
            raise TypeError ("Indeterminação")
        resultado = base ** expoente
        self . historico . append (f"{ base } ^ { expoente } = { resultado }")
        self . resultado = resultado
        return resultado

    def limpar_historico ( self ):
        self . historico . clear ()

    def obter_ultimo_resultado ( self ):
        return self . resultado