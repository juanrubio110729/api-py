#1er endpoint, ordenar matriz
sinClasificar = [3,5,5,6,8,3,4,4,7,7,1,1,2]
archivo = []
repetido= []
clasificado= []


for i in sinClasificar:
    if i not in archivo:
        archivo.append(i)
    else:
        repetido.append(i)

archivo.sort()

clasificado = archivo + repetido


#2do Endpoint
datos = [
    {"name": "Juan", "surname": "Rodriguez", "age": 19},
    {"name": "Dylan", "surname": "Rubio", "age": 8},
    {"name": "Cristian", "surname": "Garcia", "age": 20}
]


