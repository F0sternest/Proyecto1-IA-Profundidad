from binarytree import Node

class Nodo:
    def __init__(self, valor, left=None, right=None):
        self.valor = valor  
        self.izquierda = left  
        self.derecha = right 

# Creando los nodos
raiz = Nodo(46)
nodo37 = Nodo(37)
nodo20 = Nodo(20)
nodo24 = Nodo(24)
nodo34 = Nodo(34)
nodo50 = Nodo(50)
nodo58 = Nodo(58)
nodo78 = Nodo(78)

# Estableciendo conexiones
raiz.izquierda = nodo37
raiz.derecha = nodo50
nodo37.izquierda = nodo20
nodo20.derecha = nodo24
nodo24.derecha = nodo34
nodo50.izquierda = nodo58
nodo50.derecha = nodo78


# Algoritmo para la busqueda por Profundidad
def busquedaProfundidad(nodo):
    if nodo is not None:
        if nodo.valor == 58:
            print(nodo.valor)
            return True
        else:
            print(nodo.valor, end=", ")
            if busquedaProfundidad(nodo.izquierda):
                return True
            if busquedaProfundidad(nodo.derecha):
                return True
    else:
        return False

# Imprimiendo resultado
print("Busqueda y Arbol:")
busquedaProfundidad(raiz)

# Creando el arbol grafico
root = Node(46)
root.left = Node(37)
root.left.left = Node(20)
root.left.left.right = Node(24)
root.left.left.right.right = Node(34)
root.right = Node(50)
root.right.left = Node(58)
root.right.right = Node(78)

print(root)
