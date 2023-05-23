from Nodo import Nodo

# Creando los nodos
raiz = Nodo()
nodo37 = Nodo()
nodo20 = Nodo()
nodo24 = Nodo()
nodo34 = Nodo()
nodo50 = Nodo()
nodo58 = Nodo()
nodo78 = Nodo()

# Dando valores a los nodos y estableciendo conexiones
raiz.valor = 46
raiz.izquierda = nodo37
raiz.derecha = nodo50
nodo37.valor = 37
nodo37.izquierda = nodo20
nodo20.valor = 20
nodo20.derecha = nodo24
nodo24.valor = 24
nodo24.derecha = nodo34
nodo50.valor = 50
nodo50.izquierda = nodo58
nodo50.derecha = nodo78

# Nodos Hojas
nodo34.valor = 34
nodo58.valor = 58
nodo78.valor = 78


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


busquedaProfundidad(raiz)
