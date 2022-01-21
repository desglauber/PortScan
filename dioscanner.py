import nmap

scanner = nmap.PortScanner()

print('Bem vindo ao Dio Scanner')
print('<---------------------->')

ip = input('Digite o IP para ser verificado: ')
print('Você digitou o IP: ', ip)
type(ip)

menu = input(""""\n Escolha o tipo de varredura
        1 -> SYN
        2 -> UDP
        3 -> Intensa
        Digite a opção: """)
print('A opção escolhida foi: ', menu)

if menu == '1':
    print('Versão do Nmap: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('Status do IP: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('Portas abertas: ', scanner[ip]['tcp'].keys())

elif menu == '2':
    print('Versão do Nmap: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('Status do IP: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('Portas Abertas: ', scanner[ip]['udp'].keys())

elif menu == '3':
    print('Versão do Nmap: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print('Status do IP: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('Portas Abertas: ', scanner[ip]['tcp'].keys())

else:
    print('Escolha uma opção correta')