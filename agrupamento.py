import pandas as pd
from sklearn.cluster import KMeans


csv = pd.read_csv('dados.csv', sep = ',')
csv = csv.drop(columns=['id', 'tipo', 'data_publicacao', 'num_reacoes'])
dados = csv.values 
modelo = KMeans(3, random_state=0)
resultado = modelo.fit_predict(dados)


print('Digite o número de interações abaixo:')

comentarios = int(input('Comentários: '))
compartilhamentos = int(input('Compartilhamentos: '))
likes = int(input(' Likes: '))
loves = int(input('Loves: '))
wows = int(input('Wows: '))
risos = int(input('Risos: '))
raiva = int(input('Raiva: '))
triste = int(input('Triste: '))

interacoes = [comentarios, compartilhamentos, likes, loves, wows, risos, raiva, triste]
resultadoInterecoes = modelo.predict(interacoes)

print(resultadoInterecoes[0])
    
