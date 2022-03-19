viagem = float(input('Qual é a distancia da viagem? '))
valor =  viagem * .5 if viagem <= 200 else viagem * .45
print(f'Custo da passagem. {valor:.2f}')

'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

Aula do Curso de Python criado pelo professor Gustavo Guanabara para o portal CursoemVideo.com.'''
