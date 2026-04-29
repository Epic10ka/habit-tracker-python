from time import sleep
import json

NOME = 'nome'
FREQUENCIA = 'frequencia'
CONCLUIDOS = 'concluidos'



def data_save(dados):
    with open('habitos.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def data_load():
    try:
        with open('habitos.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

habitos = data_load()

def menu_return():
    sleep(0.8)
    print()
    print('\033[1;97mVoltando ao menu\033[m.'.center(62))
    print()
    for c in range (0, 3, 1):
        c = '*'.center(50)
        print(c)
        sleep(0.7)

def criar():
    while True:
        print()
        print('\033[1;97mCRIAR HÁBITO\033[m'.center(62))
        print('   ║            ------------------                ║')
        print('   ╚==============================================╝')
        hab = input('                     Hábito: ').title().strip()
        freq = input('             Frequência (Semanal/Diário): ').title().strip()
        if freq not in ['Diario', 'Diário', 'Semanal']:
            print('\033[1;91mFrequência inválida\033[m'.center(62))
            continue

        habito = {
            NOME: hab,
            FREQUENCIA: freq,
            CONCLUIDOS: 0
        }
        habitos.append(habito)
        data_save(habitos)
        while True:
            print()
            again = input('             Quer registrar mais? [S/N]: ').strip().upper()[0]
            print()
            if again == 'S':
                break

            elif again == 'N':
                return


            else:
                print('\033[1;91mOpção inválida\033[m'.center(62))
                continue

def listar():
    print()
    print('\033[1;97mLISTA DE HÁBITOS\033[m'.center(62))
    print('   ║              ------------------              ║')
    for h in habitos:
        print(f'{h[NOME]} | {h[FREQUENCIA]} | {h[CONCLUIDOS]}'.center(52))
    print('   ╚==============================================╝')

def concluir():
    while True:
        print()
        print('\033[1;97mMarcar como Concluído'.center(64))
        print('   ║               -------------------            ║')
        for i, habito in enumerate(habitos):
            print(f'[{i}] — {habito[NOME]}'.center(52))
        print('   ╚==============================================╝\033[m')
        print()
        try:
            indice_hab = int(input('                 Selecione o hábito: ').strip())
            if 0 <= indice_hab < len(habitos):
                habitos[indice_hab][CONCLUIDOS] += 1
                data_save(habitos)
                print()
                print('...'.center(56))
                sleep(0.5)
                print('\033[1;92mHábito concluído\033[m \033[1;97mcom sucesso!\033[m'.center(76))
            else:
                print('\033[1;91mÍndice inválido.\033[m'.center(62))

        except ValueError:
            print('\033[1;91mOpção inválida\033[m'.center(62))
            continue
        while True:
            print()
            again = input('          Deseja concluir outro hábito? [S/N]:').strip().upper()[0]
            if not habitos:
                print()
                print('\033[1;91mNenhum hábito registrado\033[m'.center(62))
                menu_return()
                return

            if again == 'N':
                menu_return()
                break
            elif again == 'S':
                break
            else:
                print()
                print('\033[1;91mOpção inválida\033[m'.center(64))
        if again == 'N':
            break

def progresso():
    print()
    print('\033[1;97mPROGRESSO\033[m'.center(65))
    print('   ║              ------------------              ║')
    for h in habitos:
        if h[FREQUENCIA] == 'Diário' or h [FREQUENCIA] == 'Diario':
            meta = 7
        else:
            meta = 4
        feitos = h[CONCLUIDOS]
        if feitos > 0:
            porcentagem = (feitos/meta) * 100
        else:
            porcentagem = 0
        print(f'{h[NOME]} - {porcentagem:.2f}%'.center(55))
    print('   ╚==============================================╝')

def no_habit():
    if not habitos:
        print()
        print('\033[1;91mNenhum hábito registrado\033[m'.center(62))
        menu_return()
        return

def main():
    while True:
        print('║       --------------------------------------       ║')
        print('\033[1;97m║            Sistema de Gestão de Hábitos            ║'.center(62))
        print('║       ´`´`´`´`´`´`´`´`´`´`´`´`´`´`´`´`´`´`´`       ║')
        print('║——————                                        ——————║')
        print('║                [1] Criar Hábito                    ║')
        print('║                [2] Listar hábitos                  ║')
        print('║                [3] Marcar como concluído           ║')
        print('║                [4] Ver Progresso                   ║')
        print('║                [5] Sair                            ║')
        print('╚————————————————————————————————————————————————————╝\033[m')
        try:
            option = int(input('                        > '))
            if option == 1:
                criar()
    
            if option == 2:
                if not habitos:
                    no_habit()
                else:
                    listar()
    
            if option == 3:
                if not habitos:
                    no_habit()
                else:
                    print()
                    while True:
                        access = input('            Deseja acessar o menu? (S/N): ').strip().upper()[0]
                        if access == 'S':
                            concluir()
                            break
                        elif access == 'N':
                            break
    
            if option == 4:
                if not habitos:
                    no_habit()
                else:
                    progresso()
    
            elif option == 5:
                print()
                print('\033[1;97mFinalizando...\033[m'.center(64))
                for fim in range (3, 0 ,-1):
                    fim= '*'.center(52)
                    sleep(0.5)
                    print(fim)
    
                break
        except ValueError:
            print('\033[1;91mOpção inválida\033[m'.center(62))

if __name__ == "__main__":
    main()
