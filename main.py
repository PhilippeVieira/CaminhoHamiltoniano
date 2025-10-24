import sys
import ast # Para avaliar literais de string com segurança (ex: "[[0,1]]")

class Grafo: 
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[] for _ in range(vertices)]
        self.caminho = []

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def _pode_adicionar(self, v, pos, visitado):
        if v not in self.grafo[self.caminho[pos - 1]]:
            return False

        if visitado[v]:
            return False
            
        return True

    def _encontrar_caminho_util(self, pos, visitado):
        if pos == self.V:
            return True

        for v in range(self.V):
            if self._pode_adicionar(v, pos, visitado):
                self.caminho[pos] = v
                visitado[v] = True

                if self._encontrar_caminho_util(pos + 1, visitado):
                    return True

                visitado[v] = False
                self.caminho[pos] = -1 

        return False

    def encontrar_caminho_hamiltoniano(self):
        for inicio in range(self.V):
            self.caminho = [-1] * self.V
            visitado = [False] * self.V

            self.caminho[0] = inicio
            visitado[inicio] = True

            if self._encontrar_caminho_util(1, visitado):
                print("Caminho Hamiltoniano encontrado:")
                print(self.caminho)
                return True

        print("Nenhum Caminho Hamiltoniano encontrado.")
        return False

def testes_predefinidos():

    print("--- Executando testes pré-definidos ---")

    print("--- Exemplo 1 ---")
    g1 = Grafo(5)
    g1.adicionar_aresta(0, 1)
    g1.adicionar_aresta(1, 2)
    g1.adicionar_aresta(2, 3)
    g1.adicionar_aresta(3, 4)
    g1.adicionar_aresta(1, 3) 
    g1.adicionar_aresta(1, 4)

    g1.encontrar_caminho_hamiltoniano()
    
    print("\n" + "="*20 + "\n")

    print("--- Exemplo 2 (Grafo Desconexo) ---")
    g2 = Grafo(4)
    g2.adicionar_aresta(0, 1)
    g2.adicionar_aresta(1, 2)
    g2.adicionar_aresta(0, 2)
    
    g2.encontrar_caminho_hamiltoniano()

    print("\n" + "="*20 + "\n")

    print("--- Exemplo 3 (Grafo Casa) ---")
    g3 = Grafo(5)
    g3.adicionar_aresta(0, 1) 
    g3.adicionar_aresta(1, 2) 
    g3.adicionar_aresta(0, 3) 
    g3.adicionar_aresta(1, 3) 
    g3.adicionar_aresta(1, 4) 
    g3.adicionar_aresta(2, 4) 
    g3.adicionar_aresta(3, 4) 
    
    g3.encontrar_caminho_hamiltoniano()

def grafo_personalizado(grafo_str):
    
    print(f"--- Processando Grafo da Entrada: {grafo_str} ---")
    
    try:
        arestas = ast.literal_eval(grafo_str)
        
        if not isinstance(arestas, list):
            raise TypeError("A estrutura principal não é uma lista.")
        
        if not all(isinstance(par, (list, tuple)) for par in arestas):
             raise TypeError("A estrutura interna contém itens que não são listas/tuplas.")

        if not all(len(par) == 2 for par in arestas):
            raise ValueError("Todas as arestas devem conter exatamente 2 vértices.")

        if not all(isinstance(v, int) for par in arestas for v in par):
            raise ValueError("Todos os vértices devem ser números inteiros.")

        if not arestas:
            print("Grafo vazio fornecido.")
            num_vertices = 0
        else:
            max_vertice = 0
            for u, v in arestas:
                if u < 0 or v < 0:
                    raise ValueError("IDs de vértice não podem ser negativos.")
                max_vertice = max(max_vertice, u, v)
            
            num_vertices = max_vertice + 1
            
        if num_vertices == 0:
             print("Nenhum Caminho Hamiltoniano encontrado (Grafo vazio).")
             return

        g_usuario = Grafo(num_vertices)
        for u, v in arestas:
            g_usuario.adicionar_aresta(u, v)
            
        print(f"Grafo criado com {num_vertices} vértices (0 a {num_vertices-1}) e {len(arestas)} arestas.")
        g_usuario.encontrar_caminho_hamiltoniano()

    except (ValueError, SyntaxError, TypeError) as e:
        print(f"\nErro: O texto enviado não era um grafo válido.")
        print(f"Detalhe: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":

    if len(sys.argv) > 1:
        grafo_input_string = sys.argv[1]
        grafo_personalizado(grafo_input_string)
    else:
        testes_predefinidos()