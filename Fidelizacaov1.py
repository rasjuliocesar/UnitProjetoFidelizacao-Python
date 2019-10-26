import getpass
from datetime import date
print('-=' * 30)
app = 'A P P   F I D E L I Z A Ç Ã O'
mens = 'S e j a   B e m - V i n d o !' 
print(f'{app:^60}')
print('-=' * 30)
print(f'{mens:^60}')
print('-' * 60)
login = 'root'
password = 'admin'
cont = 0
clientes = ['João', 'Maria', 'José', 'Paulo', 'Clemente']
telefone = ['81912345678', '81998765432', '81936985214', '81987651234', '81956781234']
email = ['joao@gmail.unit', 'maria@gmail.unit', 'jose@gmail.unit', 'paulo@gmail.unit', 'clemente@gmail.unit']
redesocial = ['João258', 'Maria147', 'José789', 'Paulo456', 'Clemente123']
fidelizacao = [1, 1, 2, 1, 4]
fidelcompleto = [0, 0, 0, 0, 0]
while True:
    print('\nPARA DAR INÍCIO, PRECISAMOS DO SEU LOGIN E SENHA.\n')
    login = str(input('INFORME O SEU LOGIN OU DIGITE 9 PARA SAIR: '))
    if login == '9':
        break
    password = getpass.getpass('INFORME A SUA SENHA: ')
    if login == 'root' and password == 'admin':
        print('')
        print('L O G I N   R E A L I Z A D O   C O M   S U C E S S O !\n')
        print('-'*60)
        print(f'S E J A   B E M - V I N D O, {login}! {date.today()}')
        print('-'*60)
        while True:
            print('\nNESTA TELA VOCÊ PODERÁ CADASTRAR UM NOVO CLIENTE'
                  ' OU APLICAR A FIDELIZAÇÃO AO CLIENTE.\n')
            print('1 - CADASTRAR CLIENTE.')
            print('2 - FIDELIZAR CLIENTE.')
            print('3 - LISTAR CLIENTES.')
            print('0 - SAIR.\n')
            x = int(input('INFORME A OPÇÃO DESEJADA: '))
            if x <= 0 or x > 3:
                print('-='*30)
                print('')
                print('S I S T E M A   E N C E R R A D O   C O M   S U C E S S O')
                break
            elif x == 1:
                print('-'*60)
                print('C A D A S T R A R   N O V O   C L I E N T E ')
                print('-'*60)
                clientes.append(str(input('NOME CLIENTE: ')))
                telefone.append(str(input('TELEFONE CLIENTE: ')))
                email.append(str(input('E-MAIL CLIENTE: ')))
                redesocial.append(str(input('REDE SOCIAL CLIENTE: ')))
                print(f'\nC L I E N T E   C A D A S T R A D O   C O M   S U C E S S O!!')
                fidelizacao.append(0)
                fidelcompleto.append(0)
            elif x == 2:
                print('-'*60)
                print('F I D E L I Z A R   C L I E N T E ')
                print('-'*60)
                fone = str(input('TELEFONE CLIENTE: '))
                if fone not in telefone:
                    print('\nTELEFONE NÃO CADASTRADO!\n')
                    break
                qtd = int(input('QUANTIDADE FIDELIZAÇÃO: '))
                for pos, phone in enumerate(telefone):
                    if phone == fone:
                        print(f'\nFoi Creditado {qtd} Ponto(s) para {clientes[pos]}')
                        fidelizacao[pos] = fidelizacao[pos] + qtd
                        if fidelizacao[pos] == 10:
                            print('\nP A R A B É N S !!')
                            print('\n VOCÊ TERÁ DIREITO A 1 COMPRA GRÁTIS!')
                            fidelizacao[pos] = 0
                            fidelcompleto[pos] += 1
                        elif fidelizacao[pos] > 10:
                            fidelcompleto[pos] += 1
                            fidelizacao[pos] -= 10
                            print('\nP A R A B É N S !!')
                            print('\n VOCÊ TERÁ DIREITO A 1 COMPRA GRÁTIS!')
                print(f'\nFIDELIZAÇÃO REALIZADA COM SUCESSO!')
            elif x == 3:
                print('-'*60)
                print('C L I E N T E S   C A D A S T R A D O S ')
                print('-'*60)
                n = 'NOME'
                t = 'TELEFONE'
                m = 'E-MAIL'
                rs = 'REDE SOCIAL'
                f = 'FIDELIZAÇÃO'
                fc = 'GRÁTIS'
                print(f'{n:<10}{t:<12}{m:<20}{rs:<12}{f:<13}{fc:<7}')
                for pos in range(0, len(clientes)):
                    print(f'{clientes[pos]:<10}{telefone[pos]:<12}{email[pos]:<20}{redesocial[pos]:<12}{fidelizacao[pos]:<13}{fidelcompleto[pos]:<7}')
    else:
        print('')
        print('\nL O G I N   E   /   O U   S E N H A   I N C O R R E T O S!\n')
        cont += 1
        if cont > 2:
            print('\nA P P   B L O Q U E A D O !!!\n')
            print('Favor enviar um e-mail para o Administrador - admin@unit')
            break
print('')
fim = 'F I M'
print('-=' * 30)
print(f'{fim:^60}')
