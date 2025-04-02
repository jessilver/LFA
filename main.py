import myfuncs as mf

while True:
    try:
        entrada = input('Digite a entrada: ')

        if entrada == 'exit':
            print("Saindo do programa.")
            break

        result = mf.funcao_de_transicao_estendida(mf.get_initial_state(), entrada)

        if mf.is_state_final(result):
            print(f"\033[92mEntrada aceita. Estado final: {result}\033[0m")
        else:
            print(f"\033[91mEntrada não aceita. Estado atual: {result}\033[0m")

    except ValueError as e:
        print(e)