import numpy as np
from queue import PriorityQueue
from no import No


class Solucao():
    def __init__(self, estado_inicial, meta):
        self.__estado_inicial = estado_inicial
        self.__meta = meta
        self.__caminho = []
        self.__resumo = ""
        self.__heuristica_nos = []
        
        
    def get_caminho(self):
        return self.__caminho
    
    def get_resumo(self):
        return self.__resumo
        
    def resolve(self):
        eixo_x = [1, 0, -1,  0]
        eixo_y = [0, 1,  0, -1]
        
        nivel = 0
        visitados = set()
        
        
        nos = PriorityQueue()
        no_inicial = No(self.__estado_inicial.flatten().tolist(), self.__meta.flatten().tolist(),nivel,  pai = None)
        nos.put(no_inicial)
        
        tot_nos = 0
        while nos.qsize():    
            tot_nos += 1
            
            no_atual = nos.get()
            estado_atual = no_atual.get_estado()
            
            self.__heuristica_nos.append(no_atual.get_pontos())
            
            if str(estado_atual) in visitados:
                continue
            visitados.add(str(estado_atual))
            
            if estado_atual == self.__meta.flatten().tolist():
                
                self.__resumo = str("A* deu " + str(no_atual.get_nivel()) + " passos (profundidade) para chegar ao meta, e visitou " + str(tot_nos) + " nós")
                
                while no_atual.get_pai():
                    self.__caminho.append(no_atual)
                    no_atual = no_atual.get_pai()
                    
                break
            
            quadrado_vazio = estado_atual.index(0)
            linha = quadrado_vazio // self.__meta.shape[0]
            col = quadrado_vazio % self.__meta.shape[0]
            
            estado_atual = np.array(estado_atual).reshape(self.__meta.shape[0], self.__meta.shape[0])
            for x, y in zip(eixo_x, eixo_y):
                novo_estado = np.array(estado_atual)
                
                if linha + x >= 0 and linha + x < self.__meta.shape[0] and col + y >= 0 and col + y < self.__meta.shape[0]:
                    
                    novo_estado[linha, col], novo_estado[linha+x, col+y] = novo_estado[linha+x, col+y], novo_estado[linha, col]
                    
                    estado = No(novo_estado.flatten().tolist(), self.__meta.flatten().tolist(), no_atual.get_nivel() + 1, no_atual)
                    if str(estado.get_estado()) not in visitados:
                        nos.put(estado)
        
        return self.__caminho, self.__heuristica_nos


def A_star(estado_inicial, meta):
    solucao = Solucao(estado_inicial, meta)
    caminho, heuristica = solucao.resolve()
    
    print(heuristica)
    h1 =  2 + 1 + 1 + 1 + 1 + 1 + 1 + 2
    h2 =  2 + 1 + 1 + 1 + 2 + 1 + 1 + 2
    if len(caminho) == 0:
        print("Nenhum movimento feito, já estamos no meta.")
        exit(1)
    
    linha_inicialdx = estado_inicial.flatten().tolist().index(0)
    linha_inicial= linha_inicialdx // meta.shape[0]
    col_inicial = linha_inicialdx % meta.shape[0]
    

    print('\nEstado Inicial')
    for i in range(meta.shape[0]):
        print(estado_inicial[i, :]) 
    print()
    
    for no in reversed(caminho):
        
        index_atual = no.get_estado().index(0)
        linha_atual= index_atual // meta.shape[0]
        col_atual = index_atual % meta.shape[0]
        
        nova_linha = linha_atual - linha_inicial
        nova_col = col_atual - col_inicial
        
        if nova_col == 0 and nova_linha == -1:
            print('Movendo para CIMA  de ' + str((linha_inicial + 1, col_inicial + 1)) + ' --> ' + str((linha_atual + 1, col_atual + 1)))
            print("Novo Estado após movimento:\n")
            
        elif nova_col == 0 and nova_linha == 1:
            print('Movendo para BAIXO  de ' + str((linha_inicial + 1, col_inicial + 1)) + ' --> ' + str((linha_atual + 1, col_atual + 1)))
            print("Novo Estado após movimento:\n")
            
        elif nova_linha == 0 and nova_col == 1:
            print('Movendo para DIREITA de ' + str((linha_inicial + 1, col_inicial + 1)) + ' --> ' + str((linha_atual + 1, col_atual + 1)))
            print("Novo Estado após movimento:\n")
            
        else:
            print('Movendo para ESQUERDA  de ' + str((linha_inicial + 1, col_inicial + 1)) + ' --> ' + str((linha_atual + 1, col_atual + 1)))
            print("Novo Estado após movimento:\n")
    
        linha_inicial = linha_atual
        col_inicial = col_atual
        
        for i in range(meta.shape[0]):
            
            print(np.array(no.get_estado()).reshape(meta.shape[0], meta.shape[0])[i, :]) 
        print()
        
    print(solucao.get_resumo())
    print()



meta = [1,2,3,4,5,6,7,8,0] 


#estado_inicial = [1,2,3,4,5,6,7, 0,8] 
estado_inicial = [2, 8, 1, 7, 6, 3, 4, 5, 0]


#estado_inicial = [4,15,12,11,8,13,14,10,6,5,2,1,7,9,3,0]
#meta = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0] 

n= 3
 
estado_inicial = np.array(estado_inicial).reshape(n, n) #n = 3, numpy matriz
meta = np.array(meta).reshape(n, n)
#print(estado_inicial)

A_star(estado_inicial, meta)