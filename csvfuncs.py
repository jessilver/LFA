import pandas as pd

def get_table_map(csv_file):
    """"
    Função que lê um arquivo CSV e retorna um dicionário que mapeia os estados e entradas
    """
    table = pd.read_csv(csv_file)
    table_map = {}
    alphabet = [key for key in table.columns if key not in ('Index', 'δ')]

    for row in table.itertuples():

        state = row.δ
        is_initial = '->' in state
        is_final = '*' in state

        state = state.replace('->', '').replace('*', '').strip()

        table_map[state] = {
            'is_initial': is_initial,
            'is_final': is_final
        }

        for key in alphabet:
            table_map[state][key] = getattr(row, key)

    return table_map , alphabet