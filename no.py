
import numpy as np


class No():
    def __init__(self, estado, meta, nivel, pai = None ):
        self.__estado = estado
        self.__meta = meta
        self.__nivel = nivel
        self.__heuristica = nivel
        self.__pai = pai
        self.calcula_heuristica()
    
    #Sobrescrita dos metodos internos para comparação de heuristica dos nós sem dar erro
    
    def __eq__(self, outro_no):
        return self.__heuristica == outro_no.__heuristica
    
    def __hash__(self):
        return hash(str(self.__estado))
        
    def __lt__(self, outro_no):
        return self.__heuristica < outro_no.__heuristica
    
    
    def __gt__(self, outro_no):
        return self.__heuristica > outro_no.__heuristica
    
    def get_estado(self):
        return self.__estado
    
    def get_pontos(self):
        return self.__heuristica
    
    def get_nivel(self):
        return self.__nivel
    
    def get_pai(self):
        return self.__pai
    
    def calcula_heuristica(self):
            for quadro_atual in self.__estado:
                indice_atual = self.__estado.index(quadro_atual)
                indice_meta = self.__meta.index(quadro_atual)
                linha_atual, col_atual = indice_atual // int(np.sqrt(len(self.__estado))), indice_atual % int(np.sqrt(len(self.__estado)))
                linha_meta, col_meta = indice_meta // int(np.sqrt(len(self.__estado))), indice_meta % int(np.sqrt(len(self.__estado)))
                self.__heuristica += self.manhattan(linha_atual, col_atual, linha_meta, col_meta)

            
    def manhattan(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)