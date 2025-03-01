import math
import matplotlib.pyplot as fig
import numpy as np

print("-" * 20, end=' ')
print('\033[1;36m Calculadora de Cálculo Numérico\033[m', end=' ')
print("-" * 20)

init_cal = input('Deseja iniciar a calculadora? [S/N] ').strip().upper()
if init_cal == 'N':
    print('\033[1;31mPrograma encerrado!\033[m')
    exit()

while True:
    print('Calculadora iniciada!')
    print('Selecione a operação desejada:')
    print('''[1] Erro Absoluto
[2] Erro Relativo
[3] Sistema de Equações Lineares
[4] Arredondamento
[5] Truncamento
[6] Operações com Pontos Flutuantes
[7] Método da Bisseção
[8] Sair''')
    
    op = input('Qual opção escolhida: ').strip()
    
    if op == '1':
       print('\033[1;33mErro Absoluto\033[m')
       x_exato = float(input('Digite o valor exato: '))
       x_aprox = float(input('Digite o valor aproximado: '))
       erro_abs = abs(x_exato - x_aprox)
       print(f'O erro absoluto é \033[31m{erro_abs}\033[m\n')
       x_vals = [x_exato, x_aprox]
       y_vals = [0, erro_abs]

       # Gráfico
       fig.plot(x_vals, y_vals, marker='o', linestyle='-', color='red', label='Erro Absoluto')
       fig.xlabel('Valores')
       fig.ylabel('Erro Absoluto')
       fig.title('Erro Absoluto entre Valor Exato e Aproximado')
       fig.legend()
       fig.grid()
       fig.show()

    elif op == '2':
        print('\033[1;33mErro Relativo\033[m')
        xexato = float(input('Digite o valor exato: '))
        xaprox = float(input('Digite o valor aproximado: '))
        if xexato == 0:
            print("Erro: O valor exato não pode ser zero para calcular o erro relativo.")
        else:
            erroabs = abs(xexato - xaprox)
            errorel = erroabs / abs(xexato)  
            print(f'O erro absoluto é \033[31m{erroabs}\033[m')
            print(f'O erro relativo é \033[34m{errorel:.6f}\033[m')
            x_vals = [xexato, xaprox]
            y_vals = [0, errorel]

            # Gráfico

            fig.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue', label='Erro Relativo')
            fig.xlabel('Valores')
            fig.ylabel('Erro Relativo')
            fig.title('Erro Relativo entre Valor Exato e Aproximado')
            fig.legend()
            fig.grid()
            fig.show()
    
    elif op == '3':
      print('\033[1;33mSistema de Equações Lineares\033[m')
      a1 = float(input('Digite o valor de a1: '))
      b1 = float(input('Digite o valor de b1: '))
      c1 = float(input('Digite o valor de c1: '))
      a2 = float(input('Digite o valor de a2: '))
      b2 = float(input('Digite o valor de b2: '))
      c2 = float(input('Digite o valor de c2: '))
      det = a1 * b2 - a2 * b1

      if det == 0:
        print('O sistema não tem solução única.\n')
      else:
        detx = c1 * b2 - c2 * b1
        dety = a1 * c2 - a2 * c1
        x_sol = detx / det
        y_sol = dety / det
        print(f'O valor de x é \033[31m{x_sol}\033[m e o valor de y é \033[34m{y_sol}\033[m\n')

        x_vals = np.linspace(x_sol - 5, x_sol + 5, 100)  
        y1_vals = (c1 - a1 * x_vals) / b1 if b1 != 0 else np.full_like(x_vals, c1 / a1)
        y2_vals = (c2 - a2 * x_vals) / b2 if b2 != 0 else np.full_like(x_vals, c2 / a2)

        # Grfico
        fig.plot(x_vals, y1_vals, label=f'{a1}x + {b1}y = {c1}', linestyle='-', color='blue')
        fig.plot(x_vals, y2_vals, label=f'{a2}x + {b2}y = {c2}', linestyle='-', color='green')
        fig.scatter(x_sol, y_sol, color='red', zorder=3, label=f'Solução ({x_sol:.2f}, {y_sol:.2f})')
        fig.xlabel('x')
        fig.ylabel('y')
        fig.title('Solução do Sistema de Equações Lineares')
        fig.axhline(0, color='black', linewidth=1)
        fig.axvline(0, color='black', linewidth=1)
        fig.legend()
        fig.grid()
        fig.show()

    elif op == '4':
        print('\033[1;33mArredondamento\033[m')
        num = float(input('Digite o número: '))
        casas = int(input('Digite o número de casas decimais: '))
        print(f'O número arredondado é \033[31m{round(num, casas)}\033[m\n')
    
    elif op == '5':
        print('\033[1;33mTruncamento\033[m')
        num = float(input('Digite o número: '))
        casas = int(input('Digite o número de casas decimais: '))
        trunc = math.trunc(num * 10 ** casas) / (10 ** casas)
        print(f'O número truncado é \033[31m{trunc}\033[m\n')
    
    elif op == '6':
        print('\033[1;33mOperações com Pontos Flutuantes\033[m')
        m = float(input('Digite o valor de m: '))
        b = float(input('Digite o valor de b: '))
        e = float(input('Digite o valor de e: '))
        print(f'O valor de x é \033[31m{m * math.pow(b, e)}\033[m\n')

        # Gráfico

        x_vals = np.linspace(-10, 10, 100)
        y_vals = m * b ** x_vals
        fig.plot(x_vals, y_vals, label=f'{m} * {b}^x', linestyle='-', color='purple')
        fig.xlabel('x')
        fig.ylabel('y')
        fig.title('Operações com Pontos Flutuantes')
        fig.legend()
        fig.grid()
        fig.show()

    elif op == '7':
        print('\033[1;33mMétodo da Bisseção\033[m')
        a = float(input('Digite o valor de a: '))
        b = float(input('Digite o valor de b: '))
        tol = float(input('Digite a tolerância: '))
        n = int(input('Digite o número de iterações: '))
        fa = a ** 2 - 4
        fb = b ** 2 - 4
        if fa * fb > 0:
            print('Não há raiz no intervalo\n')
        else:
            for _ in range(n):
                p = (a + b) / 2
                fp = p ** 2 - 4
                if abs(fp) < tol:
                    break
                if fa * fp > 0:
                    a = p
                else:
                    b = p
            print(f'A raiz é \033[31m{p}\033[m\n')
    
    elif op == '8':
        print('Saindo...')
        break
    
    else:
        print('\033[1;31mOpção inválida! Tente novamente.\033[m\n')
    
    continuar = input('Deseja realizar outra operação? [S/N] ').strip().upper()
    if continuar != 'S':
        print('\033[1;32mPrograma encerrado!\033[m')
        break