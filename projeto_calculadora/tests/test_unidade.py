from src.calculadora import Calculadora

#3. Teste de Unidade

#3.1 Testes de Entrada e Saída
#Objetivo: Validar se os parâmetros são interpretados corretamente e os valores retornados estão corretos.

#Operação 1 : Soma
def test_entrada_saida_soma ( self ):
  calc = Calculadora ()
  resultado = calc . somar (5, 3)
  self . assertEqual ( resultado , 8)
  self . assertEqual ( calc . obter_ultimo_resultado () , 8)

#Operação 2 : Subtração
def test_entrada_saida_subtracao ( self ):
  calc = Calculadora ()
  resultado = calc . subtrair (10, 3)
  self . assertEqual ( resultado , 7)
  self . assertEqual ( calc . obter_ultimo_resultado () , 5)

#Operação 3 : Multiplicação
def test_entrada_saida_multiplicacao ( self ):
  calc = Calculadora ()
  resultado = calc . multiplicar (2, 10)
  self . assertEqual ( resultado , 20)
  self . assertEqual ( calc . obter_ultimo_resultado () , 20)

#Operação 4 : Divisão
def test_entrada_saida_divisao ( self ):
  calc = Calculadora ()
  resultado = calc . dividir (5, 2)
  self . assertEqual ( resultado , 2.5)
  self . assertEqual ( calc . obter_ultimo_resultado () , 2.5)

#Operação 5 : Potência
def test_entrada_saida_potencia ( self ):
  calc = Calculadora ()
  resultado = calc . potencia (5, 2)
  self . assertEqual ( resultado , 2.5)
  self . assertEqual ( calc . obter_ultimo_resultado () , 2.5)

###################################################################################
###################################################################################
###################################################################################

# 3.2 Testes de Tipagem
def test_tipagem_invalida ( self ):
    calc = Calculadora()

    # SOMAR: Testa se a função rejeita tipos inválidos
    with self.assertRaises(TypeError):  # String como primeiro argumento
        calc.somar("5", 3)

    # * Sugestão de melhoria: Inclusão de outros testes
    with self.assertRaises(TypeError):  # String como segundo argumento
        calc.somar(5, "3")
    with self.assertRaises(TypeError):  # Ambos argumentos como strings
        calc.somar("5", "3")

    # SUBTRAIR: Testa tipos inválidos nos argumentos
    with self.assertRaises(TypeError):
        calc.subtrair("10", 2)

    # * Sugestão de melhoria: Inclusão de outros testes
    with self.assertRaises(TypeError):
        calc.subtrair(10, "2")
    with self.assertRaises(TypeError):
        calc.subtrair("10", "2")

    # MULTIPLICAR: Verifica se entradas não numéricas são rejeitadas
    with self.assertRaises(TypeError):
        calc.multiplicar("10", 2)

    # * Sugestão de melhoria: Inclusão de outros testes
    with self.assertRaises(TypeError):
        calc.multiplicar(10, "2")
    with self.assertRaises(TypeError):
        calc.multiplicar("10", "2")

    # DIVIDIR: Além da divisão por zero, testa tipagem incorreta
    with self.assertRaises(TypeError):
        calc.dividir("10", 2)

    # * Sugestão de melhoria: Inclusão de outros testes
    with self.assertRaises(TypeError):
        calc.dividir(10, "2")
    with self.assertRaises(TypeError):
        calc.dividir("10", "2")

    # POTÊNCIA: Testa se apenas tipos numéricos são aceitos
    with self.assertRaises(TypeError):
        calc.potencia("3", 3)
    
    # * Sugestão de melhoria: Inclusão de outros testes
    with self.assertRaises(TypeError):
        calc.potencia(3, "3")
    with self.assertRaises(TypeError):
        calc.potencia("3", "3")

###################################################################################
###################################################################################
###################################################################################

# 3.3 Testes de Consistência
# Objetivo: Verificar se os dados permanecem consistentes apos operações.

def test_consistencia_historico ( self ):
    calc = Calculadora ()
    calc.somar (2, 3)
    calc.multiplicar (4, 5)
    # * Sugestão de melhoria: Verificar se os dados permanecem consistentes apos operações.
    calc.subtrair(10,9)
    calc.dividir(10,2)
    calc.potencia(2,2)

    #self . assertEqual (len ( calc . historico ), 2)
    self . assertEqual (len ( calc . historico ), 5)
    self . assertIn ("2 + 3 = 5", calc.historico )
    self . assertIn ("4 * 5 = 20", calc.historico )
    self . assertIn ("10 - 9 = 1", calc.historico )
    self . assertIn ("10 / 2 = 5", calc.historico )
    self . assertIn ("2 ** 2 = 4", calc.historico )

###################################################################################
###################################################################################
###################################################################################

# 3.4 Testes de Inicialização
# Objetivo: Garantir que a estrutura é inicializada corretamente.
def test_inicializacao ( self ):
    calc = Calculadora ()
    # * Sugestão de melhoria: Garantir que a estrutura é inicializada corretamente.
    try :
        self . assertEqual ( calc . resultado , 0)
        self . assertEqual (len ( calc . historico ), 0)
    except ValueError as e:
        self . assertEqual (str (e), "Erro na inicialização da calculadora")  
         # * Ajuste para não ter interferencia de outros testes
            calc.limpar_historico()
    


###################################################################################
###################################################################################
###################################################################################

#3.5 Testes de Modificação de Dados
#Objetivo: Verificar se modificações são aplicadas corretamente.
def test_modificacao_historico ( self ):
    calc = Calculadora ()
    calc . somar (1, 1)
    self . assertEqual (len ( calc . historico ), 1)
    calc . limpar_historico ()
    self . assertEqual (len ( calc . historico ), 0)

    # * Sugestão de melhoria: Verificar se modificações são aplicadas corretamente.
    calc.subtrair(7, 3)  # Realiza a operação soma
    calc.potencia(2, 2)  # Realiza outra operação
    calc.dividir(2, 2)  # Realiza outra operação
    self.assertEqual(len(calc.historico), 3)  # Verifica se o histórico tem 3 operações

    calc.limpar_historico()  # Limpa o histórico
    self.assertEqual(len(calc.historico), 0)  # Verifica se o histórico está limpo

    

###################################################################################
###################################################################################
###################################################################################

#3.6 Testes de Limite Inferior
#Objetivo: Testar comportamento com valores mínimos.
def test_limite_inferior ( self ):
    calc = Calculadora ()
    # Teste com zero
    resultado = calc . somar (0, 5)
    self . assertEqual ( resultado , 5)
    # Teste com numeros negativos muito pequenos
    resultado = calc . multiplicar (-1e-10 , 2)
    self . assertEqual ( resultado , -2e-10)

 # * Sugestão de melhoria: Verificar se modificações são aplicadas corretamente.

    resultado = calc.dividir(-1e-100, -1e-100)  # Espera-se que a divisão seja 1
    self.assertEqual(resultado, 1.0)
    
    resultado = calc.potencia(-1e-100, 2)  # Espera-se que o resultado seja 1e-200
    self.assertEqual(resultado, 1e-200)


###################################################################################
###################################################################################
###################################################################################

#3.7 Testes de Limite Superior
#Objetivo: Testar comportamento com valores máximos.
def test_limite_superior ( self ):
    calc = Calculadora ()
    # Teste com numeros grandes
    resultado = calc . somar (1e10 , 1e10)
    self . assertEqual ( resultado , 2e10)

    # * Sugestão de melhoria: Verificar se modificações são aplicadas corretamente.
    # Teste com valores próximos ao limite máximo de float do Python
    max_float = sys.float_info.max

    # Operações que devem funcionar normalmente
    resultado = calc.somar(max_float, 0)
    self.assertEqual(resultado, max_float)

    resultado = calc.subtrair(max_float, 0)
    self.assertEqual(resultado, max_float)

    resultado = calc.multiplicar(max_float, 1)
    self.assertEqual(resultado, max_float)

    resultado = calc.dividir(max_float, 1)
    self.assertEqual(resultado, max_float)

###################################################################################
###################################################################################
###################################################################################

#3.8 Testes de Valores Fora do Intervalo
#Objetivo: Verificar comportamento com valores inválidos.
def test_divisao_por_zero ( self ):
    calc = Calculadora ()
    with self . assertRaises ( ValueError ):
        calc . dividir (10 , 0)

    # * Sugestão de melhoria: Verificar se modificações são aplicadas corretamente.
    with self.assertRaises(ValueError):  # Aqui esperamos um erro ao tentar dividir por número muito pequeno
        calc.dividir(10, 1e-100)  # Tentando dividir por número extremamente pequeno
    

###################################################################################
###################################################################################
###################################################################################

#3.9 Testes de Fluxos de Controle
#Objetivo: Testar diferentes caminhos do código.
def test_fluxos_divisao ( self ):
    calc = Calculadora ()
    # Caminho normal
    resultado = calc . dividir (10 , 2)
    self . assertEqual ( resultado , 5)

    # * Sugestão de melhoria: Verificar se modificações são aplicadas corretamente.
    # Caminho normal com números negativos
    resultado = calc.dividir(-10, -2)
    self.assertEqual(resultado, 5)  # Resultado esperado é 5

    # Caminho normal com um número negativo
    resultado = calc.dividir(10, -2)
    self.assertEqual(resultado, -5)  # Resultado esperado é -5

    # Caminho de erro
    with self . assertRaises ( ValueError ):
        calc . dividir (10 , 0)
    
###################################################################################
###################################################################################
###################################################################################

#3.10 Testes de Mensagens de Erro
#Objetivo: Verificar se mensagens de erro são claras.
def test_mensagens_erro ( self ):
    calc = Calculadora ()
    try :
        calc . dividir (5, 0)
    except ValueError as e:
        self . assertEqual (str (e), " Divisao por zero não é permitida ")    
    
    # * Sugestão de melhoria: Verificar se modificações são aplicadas corretamente.
    try:
        calc.dividir(10, 1e-100)  # Divisão por número muito pequeno
    except ValueError as e:
        self.assertEqual(str(e), "Divisao por numero próximos a 0 não é permitida")