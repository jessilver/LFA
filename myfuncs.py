import csvfuncs as cf
import glob

csv_file = glob.glob('tabela_de_transicao/*.csv')[0]
table_map, alphabet = cf.get_table_map(csv_file)

def is_letter_in_alphabet(letter):
    """
    Função que verifica se a letra está no alfabeto.
    """
    if letter in alphabet:
        return True
    else:
        raise ValueError(f"\033[93mLetra {letter} não encontrada no alfabeto: {alphabet}\033[0m")

def is_state_in_table(state):
    """
    Função que verifica se o estado está na tabela de transição.
    """
    if state in table_map:
        return True
    else:
        raise ValueError(f"\033[93mEstado {state} não encontrado na tabela de transição.\033[0m")

def is_state_final(state):
    """
    Função que verifica se o estado é final.
    """
    if is_state_in_table(state):
        return table_map[state]['is_final']

def get_initial_state():
    """
    Função que retorna o estado inicial.
    """
    for state, info in table_map.items():
        if info['is_initial']:
            return state
    raise ValueError("\033[91mEstado inicial não encontrado na tabela de transição.\033[0m")

def get_state_info(state):
    """
    Função que retorna informações sobre o estado atual.
    """
    if is_state_in_table(state):
        return table_map[state]

def funcao_de_transicao(q,a):
    """
    Função de transição que retorna o próximo estado com base no estado atual e na entrada.
    """
    if is_state_in_table(q) and is_letter_in_alphabet(a):
        state = table_map[q][a]
        return state
    else:
        raise ValueError(f"\033[93mTransição não definida para estado {q} e entrada {a}\033[0m")
    
def funcao_de_transicao_estendida(q,w):
    """
    Função de transição estendida que retorna o resultado com base na sequência de entradas.
    """
    if len(w) == 0:
        return q
    
    a = w[-1]
    x = w[:-1]

    return funcao_de_transicao(funcao_de_transicao_estendida(q, x), a)