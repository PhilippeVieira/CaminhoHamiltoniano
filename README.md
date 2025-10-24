# Caminho Hamiltoniano

Este repositório contém uma implementação em Python do algoritmo de backtracking para encontrar um **Caminho Hamiltoniano** em um grafo orientado ou não orientado.



## 1. Descrição do Projeto

O objetivo deste projeto é determinar se existe um **Caminho Hamiltoniano** em um dado grafo (direcionado ou não).

Um Caminho Hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez.  
O problema de encontrar tal caminho é um problema clássico na teoria dos grafos e é conhecido por ser **NP-Completo**.  
A implementação fornecida utiliza uma abordagem de força bruta recursiva, conhecida como *backtracking*, para explorar todas as possibilidades de caminhos.



## 2. Lógica da Implementação (`main.py`)

O script `main.py` é estruturado da seguinte forma:

#### `class Grafo`

Esta classe representa o grafo.

- `__init__(self, vertices)`:  
  O construtor inicializa o grafo com um número de vértices (`int`) e cria uma lista de adjacência (`self.grafo`) usando um `defaultdict(list)`.  
  Também armazena o número de vértices em `self.V`.

- `adicionar_aresta(self, u, v)`:  
  Adiciona uma aresta bidirecional entre os vértices `u` e `v`, atualizando a lista de adjacência para ambos.

---

#### `_encontrar_caminho_util(self, u, caminho)`

Esta é a função recursiva (auxiliar) que implementa a lógica de *backtracking*.

**Lógica linha a linha:**

1. A função recebe o vértice atual `u` e a lista `caminho` contendo os vértices já visitados.
2. O vértice `u` é adicionado ao caminho.
3. **Caso Base (Sucesso):** Se o comprimento do `caminho` for igual ao número total de vértices (`self.V`), significa que visitamos todos os vértices.  
   Um Caminho Hamiltoniano foi encontrado, então a função imprime o caminho e retorna `True`.
4. **Passo Recursivo (Exploração):**  
   - O código itera sobre todos os `v` vizinhos de `u` (`self.grafo[u]`):
   - Para cada vizinho `v`, ele verifica se `v` ainda não está no `caminho`.
   - Se `v` não foi visitado, o algoritmo tenta explorar esse novo caminho chamando a si, recursivamente:  
      `_encontrar_caminho_util(v, caminho)`
   - Se a chamada recursiva retornar `True`(o que significa que um caminho foi encontrado a partir de `v`), a função propaga esse `True` para cima, encerrando a busca.
5. **Backtrack (Falha):** Se o loop sobre os vizinhos terminar sem encontrar um caminho (ou seja, todos os vizinhos já foram visitados ou os caminhos recursivos falharam), significa que o vértice `u` não leva a uma solução a partir deste estado. O algoritmo então "retrocede" (backtracks), removendo `u` do `caminho` (`caminho.pop()`) e retorna `False`.

---

#### `encontrar_caminho_hamiltoniano(self)`

Esta é a função principal que inicia a busca.

1. O algoritmo deve funcionar independentemente do vértice inicial. Por isso, esta função itera por todos os vértices do grafo (de `0` a `self.V - 1`).
2. Para cada vértice `i`, ela inicia uma nova busca de backtracking chamando `_encontrar_caminho_util(i, [])` com um caminho vazio.
3. Se algum retorno for `True`, a função principal imprime uma mensagem de sucesso e encerra.
4. Se o loop terminar e nenhum caminho for encontrado a partir de nenhum vértice inicial, a função imprime uma mensagem de falha e retorna `False`.

---

### Funções de Execução (`if __name__ == "__main__":`)

O bloco principal decide qual modo de execução utilizar com base nos argumentos de linha de comando (`sys.argv`):

#### **Modo de Teste (`testes_predefinidos`)**
- Ativado se o script for executado **sem argumentos**(`python main.py`).
- Esta função instancia e testa três grafos de exemplo com diferentes estruturas, imprimindo os resultados de cada um.

#### **Modo de Argumento (`grafo_personalizado`):**
* Ativado se o script for executado com um argumento (`python main.py "..."`).
* O argumento (`grafo_str`) é lido como uma string.
* A função usa `ast.literal_eval` para converter com segurança a string em uma lista Python (ex: `"[[0,1]]"` se torna `[[0, 1]]`).
* Ela valida se a estrutura é uma lista de pares de inteiros.
* Determina o número de vértices (`num_vertices`) encontrando o maior ID de vértice na lista de arestas e somando 1.
* Cria o grafo e chama `encontrar_caminho_hamiltoniano()`.
* Possui tratamento de erros para caso a string não seja um grafo válido.

## 3 - Como Executar o Projeto
Você precisará do Python 3 instalado para rodar este script.

### Pré-requisitos
* [Python 3.x](https://www.python.org/downloads)

### Execução Local
1.  Clone este repositório:
    ```bash
    git clone [https://github.com/PhilippeVieira/CaminhoHamiltoniano.git](https://github.com/PhilippeVieira/CaminhoHamiltoniano.git)
    cd CaminhoHamiltoniano
    ```
2.  Existem duas formas de executar o script:

    **A) Executando os Casos de Teste Internos:** Para rodar os exemplos pré-definidos no código, execute:
    ```bash
    python main.py
    ```
    *Saída esperada:*
    ```
    --- Executando testes pré-definidos ---
    --- Exemplo 1 ---
    Caminho Hamiltoniano encontrado:
    [0, 1, 2, 3, 4]
    ... (etc.)
    ```

    **B) Fornecendo um Grafo Personalizado via Argumento:** Você pode passar um grafo como uma string na linha de comando. O grafo deve ser uma lista de arestas (listas ou tuplas de dois inteiros).
    
    **Importante:** Use aspas (`" "`) ao redor da string do grafo.
    </br></br>
    *B.1 Exemplo (Grafo Triângulo/K3):*
    ```bash
    python main.py "[[0,1], [1,2], [2,0]]"
    ```
    *Saída esperada:*
    ```
    --- Processando Grafo da Entrada: [[0,1], [1,2], [2,0]] ---
    Grafo criado com 3 vértices (0 a 2) e 3 arestas.
    Caminho Hamiltoniano encontrado:
    [0, 1, 2]
    ```

    *B.2 Exemplo (Grafo Linha):*
    ```bash
    python main.py "[[0,1], [1,2], [2,3]]"
    ```
    *Saída esperada:*
    ```
    --- Processando Grafo da Entrada: [[0,1], [1,2], [2,3]] ---
    Grafo criado com 4 vértices (0 a 3) e 3 arestas.
    Caminho Hamiltoniano encontrado:
    [0, 1, 2, 3]
    ```

    *B.3 Exemplo (Entrada Inválida):*
    ```bash
    python main.py "[0,1], [1,2]]"
    ```
    *Saída esperada:*
    ```
    --- Processando Grafo da Entrada: [0,1], [1,2]] ---
    
    Erro: O texto enviado não era um grafo válido.
    Detalhe: unmatched ']' (<unknown>, line 1)
    ```

## 4 - Relatório Técnico: Análise da Complexidade Computacional
### 4.1 - Classes P, NP, NP-Completo e NP-Difícil
O Problema do Caminho Hamiltoniano (HPP) se enquadra nas seguintes classes:

* **Classe NP (Nondeterministic Polynomial time):** O HPP está na classe NP. Um problema está em NP se uma solução candidata puder ser verificada em tempo polinomial.
    * **Justificativa:** Se recebermos um "caminho candidato" (uma sequência de vértices), podemos facilmente verificar se ele é um Caminho Hamiltoniano em tempo polinomial. A verificação consiste em:
        1.  Checar se o caminho contém `V` vértices (onde `V` é o total de vértices). `O(V)`
        2.  Checar se todos os vértices são únicos. `O(V)` (usando um set/hash).
        3.  Checar se existe uma aresta entre cada vértice consecutivo no caminho (`caminho[i]` e `caminho[i+1]`). `O(V)` (assumindo consulta `O(1)` na lista de adjacência, ou `O(V * logV)` no total se as listas de adjacência forem longas).
            Como a verificação é polinomial (`O(V)` ou `O(V^2)`), o problema está em NP.


* **Classe NP-Difícil (NP-Hard):** Um problema é NP-Difícil se ele for "pelo menos tão difícil quanto" qualquer problema em NP. Formalmente, qualquer problema em NP pode ser reduzido a ele em tempo polinomial.
    * **Justificativa:** O HPP é NP-Difícil. Isso é provado mostrando que um problema sabidamente NP-Completo, como o **Problema do Circuito Hamiltoniano (HCP)** ou o **Problema 3-SAT**, pode ser reduzido ao HPP. O Problema do Caminho Hamiltoniano é uma generalização do Problema do Caixeiro Viajante (TSP) na sua forma de decisão.


* **Classe NP-Completo (NP-Complete):** Um problema é NP-Completo se ele está em NP e também é NP-Difícil.
    * **Justificativa:** Como o Problema do Caminho Hamiltoniano satisfaz ambas as condições (está em NP e é NP-Difícil), ele é classificado como NP-Completo.


* **Classe P (Polynomial time):** Esta classe contém problemas que podem ser resolvidos (não apenas verificados) em tempo polinomial.
    * **Justificativa:** Ninguém jamais encontrou um algoritmo de tempo polinomial para o HPP. A menos que se prove que P = NP (o que é a maior questão em aberto na ciência da computação), assume-se que o HPP não está na classe P.


* **Relação com o Caixeiro Viajante (TSP):** O Problema do Caminho Hamiltoniano é redutível ao TSP. Se tivéssemos um "oráculo" que resolve o TSP, poderíamos usá-lo para resolver o HPP. Basta criar um grafo completo a partir do grafo original, atribuir peso 1 às arestas que existem no original e peso 2 (ou infinito) às que não existem. Se o TSP encontrar um caminho de peso total `V-1`, então existe um Caminho Hamiltoniano.

### 4.2 - Análise da Complexidade Assintótica de Tempo
* **Complexidade Temporal: `O(V * V!)`**
* **Método de Determinação (Análise da Árvore de Recursão):** O algoritmo implementado é um backtracking que, no pior caso, explora todas as permutações possíveis dos vértices para verificar se formam um caminho.
    1. A função `encontrar_caminho_hamiltoniano` chama `_encontrar_caminho_util` no máximo `V` vezes (uma para cada vértice inicial).
    2.  A função recursiva `_encontrar_caminho_util` gera uma árvore de busca.
    3.  O primeiro nó (raiz) tem `V` escolhas.
    4.  O próximo nível de recursão tem `V-1` escolhas (todos os vizinhos, exceto o vértice atual).
    5.  O próximo tem `V-2` escolhas, e assim por diante.
    6.  O número total de caminhos potenciais (nós na árvore) é da ordem de `V * (V-1) * (V-2) * ... * 1`, o que é `V!` (V Fatorial).
    7.  Em cada chamada recursiva (`_encontrar_caminho_util`), o algoritmo realiza duas operações custosas:
        * Itera sobre os vizinhos: `O(V)` (ou `O(d)` onde `d` é o grau do vértice).
        * Verifica se o vizinho está no `caminho`: `if u not in caminho`. Em Python, a verificação `in` para listas é `O(k)`, onde `k` é o tamanho do caminho (que vai de 1 a `V`).
         <br></br>
        
    Portanto, a complexidade é o número de nós na árvore de recursão (`O(V!)`) multiplicado pelo custo de processamento em cada nó (`O(V)` para o loop + `O(V)` para a verificação `in`), resultando em `O(V^2 * V!)`.
    Frequentemente, esta complexidade é simplificada para `O(V * V!)`, assumindo que a verificação `in` e a busca de vizinhos são otimizadas ou analisadas de forma amortizada. De qualquer forma, a complexidade é fatorial, o que é computacionalmente inviável para grafos grandes.

### 4.3 - Aplicação do Teorema Mestre
* **O Teorema Mestre é aplicável? Não.**
* **Justificativa:** O Teorema Mestre é uma ferramenta para analisar a complexidade de algoritmos de "dividir para conquistar" que seguem uma relação de recorrência específica: `T(n) = aT(n/b) + f(n)` Onde:
    * `n` é o tamanho do problema.
    * `a` é o número de subproblemas.
    * `n/b` é o tamanho de cada subproblema (o problema é dividido em partes menores).
    * `f(n)` é o custo de dividir o problema e combinar os resultados.
      <br></br>
  
  A recorrência do nosso algoritmo de backtracking não se encaixa nesse modelo. A recorrência se parece mais com `T(V) = (V-1) * T(V-1) + O(V^2)`, pois um problema de tamanho `V` gera até `V-1` subproblemas de tamanho `V-1` (não `V/b`). O Teorema Mestre não pode ser aplicado a recorrências onde o tamanho do subproblema é reduzido por subtração (como `T(n-1)`) em vez de divisão (`T(n/b)`).

### 4.4 - Análise dos Casos de Complexidade
* **Pior Caso (`O(V * V!)`):** O pior caso ocorre quando o algoritmo precisa explorar a árvore de busca quase inteira. Isso acontece tipicamente em duas situações:
    1.  **Grafos Completos (K_v):** Em um grafo onde todos os vértices estão conectados, o algoritmo tentará `V-k` caminhos em cada nível `k`. Existem `V!` caminhos possíveis, e o algoritmo explorará muitos deles.
    2.  **Grafos sem Caminho Hamiltoniano:** O algoritmo só concluirá que não há caminho após explorar todas as permutações possíveis e falhar em todas.
* **Melhor Caso (`O(V)`):** O melhor caso ocorre quando o primeiro caminho tentado pelo algoritmo é um Caminho Hamiltoniano válido.
    * **Exemplo:** Um grafo que é uma linha simples (`0-1-2-3...V-1`) e a busca começa no vértice `0` (ou `V-1`).
    * **Análise:** A função `encontrar_caminho_hamiltoniano` inicia em `i=0`. A função `_encontrar_caminho_util(0, [])` é chamada. Ela encontra o vizinho `1`, chama `_encontrar_caminho_util(1, [0])`. Esta encontra o vizinho `2`, e assim por diante. Haverá apenas `V` chamadas recursivas, e cada chamada encontra o próximo vértice correto imediatamente. O custo total é linear em relação ao número de vértices.
* **Caso Médio:**
    * A análise do caso médio é extremamente complexa. O desempenho depende da densidade (número de arestas) e da estrutura do grafo.
    * **Grafos Esparsos (poucas arestas):** O desempenho é geralmente melhor que o pior caso, pois a árvore de busca é "podada" (pruned) muito mais cedo. Em cada etapa, há menos vizinhos para explorar, e os caminhos tendem a atingir "becos sem saída" mais rapidamente, forçando o backtrack.
    * **Impacto no Desempenho:** A poda da árvore de busca é o fator crucial. Em um grafo do "mundo real", o algoritmo raramente atingirá o `O(V!)`, mas ainda assim será exponencial/fatorial, tornando-o lento para grafos com mais de 20-25 vértices.


# Licença

Este projeto está licenciado sob a Licença MIT.