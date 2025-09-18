#4.1 Teste de Operações Sequenciais
#Objetivo: Verificar se múltiplas operações funcionam em conjunto.
def test_operacoes_sequenciais ( self ) :
    calc = Calculadora ()

    # * Ajuste para não ter interferencia de outros testes
    calc.limpar_historico()
    #

    # Sequencia : 2 + 3 = 5 , depois 5 * 4 = 20 , depois 20 / 2 = 10
    calc . somar (2 , 3)
    resultado1 = calc . obter_ultimo_resultado ()
    calc . multiplicar ( resultado1 , 4)
    resultado2 = calc . obter_ultimo_resultado ()
    calc . dividir ( resultado2 , 2)
    resultado_final = calc . obter_ultimo_resultado ()

    self . assertEqual ( resultado_final , 10)
    self . assertEqual ( len ( calc . historico ) , 3)

    # * Ajuste para não ter interferencia de outros testes
    calc.limpar_historico()
    #

    # * Sugestão de melhoria: Verificar se múltiplas operações funcionam em conjunto com outras operações
    # Sequencia : 10 - 6 = 4 , depois 2 ** 3 = 64 , depois 8 * -1 = -64 , depois -8 / -2 = 32
    calc.subtrair(10, 6)           # 10 - 6 = 4
    resultado1 = calc.obter_ultimo_resultado()

    calc.potencia(resultado1, 3)   # 4 ** 3 = 64
    resultado2 = calc.obter_ultimo_resultado()

    calc.multiplicar(resultado2, -1)  # 64 * -1 = -64
    resultado3 = calc.obter_ultimo_resultado()

    calc.dividir(resultado3, -2)    # -64 / -2 = 32
    resultado_final = calc.obter_ultimo_resultado()


#4.2 Teste de Interface entre Métodos
#Objetivo: Verificar se diferentes métodos se comunicam corretamente.
def test_integracao_historico_resultado ( self ) :
    calc = Calculadora ()
    # * Ajuste para não ter interferencia de outros testes
    calc.limpar_historico()
    #

    calc . potencia (2 , 3) # 2^3 = 8
    calc . somar ( calc . obter_ultimo_resultado () , 2) # 8 + 2 = 10
    
    self . assertEqual ( calc . obter_ultimo_resultado () , 10)
    self . assertEqual ( len ( calc . historico ) , 2)
    self . assertIn ("2 ^ 3 = 8", calc . historico )
    self . assertIn ("8 + 2 = 10", calc . historico )

    # * Ajuste para não ter interferencia de outros testes
    calc.limpar_historico()
    #

    # * Sugestão de melhoria: Verificar se diferentes métodos se comunicam corretamente.
    
    calc.multiplicar(5, 3)         # 5 * 3 = 15
    calc.subtrair(calc.obter_ultimo_resultado(), 4)  # 15 - 4 = 11

    self.assertEqual(calc.obter_ultimo_resultado(), 11)
    self.assertEqual(len(calc.historico), 2)
    self.assertIn("5 * 3 = 15", calc.historico)
    self.assertIn("15 - 4 = 11", calc.historico)

