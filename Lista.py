from Elemento import Elemento

class Lista:
    def _init_(self):
        self.primeiro = None

    #fabrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e
    
    def imprimeLista(self):
        aux = self.primeiro
        if(aux != None):
            while(aux != None):
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Lista Vazia ---")

    def addElementoNoFinal(self, valorQualquer):
        aux = self.primeiro
        if(aux != None):
            #se nao for vazio JA TEM ELEMENTO
            while(aux.proximo != None):
                aux = aux.proximo
            #neste ponto o aux aponta para o ultimo elemento
            aux.proximo = self.criarNovoElemento(valorQualquer)     
        else:
            # NAO TEM ELEMENTO
            self.primeiro = self.criarNovoElemento(valorQualquer)
            
    
##------------------------------------------------##
## MAIN ##

#Criando uma lista VAZIA
minhaLista = Lista()
minhaLista.addElementoNoFinal(91)
minhaLista.addElementoNoFinal(92)
minhaLista.addElementoNoFinal(93)

minhaLista.imprimeLista()
