# Definição das ações do robô aspirador
acoes = ['direita', 'esquerda', 'aspirar', 'nada']

# Espaço de estados
estados = (('A_suja','B_suja', 'A'), ('A_suja','B_limpa', 'A'),
           ('A_limpa','B_suja', 'A'), ('A_limpa','B_limpa', 'A'),
           ('A_suja','B_suja', 'B'), ('A_limpa','B_suja', 'B'),
           ('A_suja','B_limpa', 'B'), ('A_limpa','B_limpa', 'B')
           )

# Definição do estado inicial
estado_inicial = ('A_limpa', 'B_limpa', 'A')
# estado_inicial = ('A_limpa', 'B_suja', 'A')

# Definição do estado objetivo
estado_meta = (('A_limpa', 'B_limpa', 'A'), ('A_limpa','B_limpa', 'B'))

# Definição das regras do ambiente
# acao(estado_atual) -> proximo_estado
regras = [(estados[0], 'aspirar', estados[2]),
          (estados[1], 'aspirar', estados[3]),
          (estados[2], 'direita', estados[5]),
          (estados[3], 'nada', estados[3]),
          (estados[4], 'aspirar', estados[6]),
          (estados[5], 'aspirar', estados[7]),
          (estados[6], 'esquerda', estados[1]),
          (estados[7], 'nada', estados[7])
          ]

# Implementação da busca em largura
def busca_largura(estado_inicial, estado_meta, regras):
    caminho = []
    fila = [estado_inicial]
    visitado = []
    while fila:
        estado_atual = fila.pop(0)
        # print('Estados visitados: ', visitado)

        if estado_atual not in visitado:
            visitado.append(estado_atual)
            if estado_atual in estado_meta:
                return caminho
            for (estado_regra, acao, proximo_estado) in regras:
                if estado_regra == estado_atual:
                  caminho.append(acao)
                  estado_atual = proximo_estado
                  fila.append(estado_atual)
                  break
    return None

# Chamada da função de busca em largura
solucao = busca_largura(estado_inicial, estado_meta, regras)

# Impressão da solução
if solucao:
    print('Solução encontrada: ', solucao)
else:
    print('Não foi encontrada uma solução.')