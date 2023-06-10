class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable():
    def __init__(self, size):
        self.size = size
        self.T = [None] * self.size
        self.positions = 0

    def _hash_Function(self, key):
        """Metodo privado para una funcion hash que usa el algoritmo djb2"""
        hash_value = 33
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size

    def search(self, key):
        """Busca un elemento en la tabla hash basado en su key"""
        index = self._hash_Function(key)
        bucket = self.T[index]
        while bucket is not None:
            if bucket.key == key:
                return bucket.value
        return f"Key no encontrada en la tabla hash"


    def insert(self, key, value):
        """inserta un elemento en la tabla hash si la key no esta en uso."""
        index = self._hash_Function(key)

        if self.T[index] is None:
            # No hay colision, crear un nodo y asignarlo al bucket
            self.T[index] = Node(key, value)
            self.positions += 1
        else:
            # Colision, agregar al final de la linked list
            bucket = self.T[index]
            while True:
                if bucket.key == key:
                    bucket.value = value  # Actualizar el valor si la key ya existe
                    return
                if bucket.next is None:
                    break
                bucket = bucket.next
            #No hay nodo que haga match con la key, agregarlo al final
            bucket.next = Node(key, value)
            self.positions += 1

    def remove(self, key):
       """Elimina un elemento de la tabla hash si la key no esta en la tabla da un error"""
       index = self._hash_Function(key)
       bucket = self.T[index]
       prev = None
       while bucket is not None:
           if bucket.key == key:
               if prev is None:
                   # Eliminar el primer nodo de la lista
                   self.T[index] = bucket.next
                   self.positions -= 1
               else:
                   # Eliminar un nodo que no es el primero
                   prev.next = bucket.next
                   self.positions -= 1
               return
           prev = bucket
           bucket = bucket.next
       return f"Key no encontrada en la tabla hash"

    def load_Factor(self):
        """Funcion que devuelve el factor de carga de la tabla hash"""
        load_Factor = (self.positions / self.size)
        return f"el Factor de carga es: {load_Factor}"

    def longest_List(self):
        """Funcion que devuelve la lista mas larga dentro de la tabla hash"""
        longest_length = 0
        for bucket in self.T:
            length = 0
            current = bucket
            while current is not None:
                length += 1
                current = current.next
            if length > longest_length:
                longest_length = length
        if longest_length == 0:
            return None  # la lista esta vacia

        return f"La lista mas larga tiene {longest_length} nodos"
    
    def posiciones_Ocupadas(self):
        return f"La cantidad de posiciones ocupadas es {self.positions}"

##################################                   #######################################################################
##################################    Interfaz       #######################################################################
##################################                   #######################################################################
##################################                   #######################################################################
tabla = HashTable(50000)


def menu() -> None:
    print("1. Add new item")
    print("2. Query item")
    print("3. Delete item")
    print("4. Stats")
    print("5. Exit")
    print()


if __name__ == "__main__":
    while True:
        menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            key = input("ingresar key: ")
            val = (input("ingresar value: "))

            tabla.insert(key, val)
        elif choice == 2:
            print(tabla.search(input("Ingresar valor buscado: ")))
        elif choice == 3:
            print(tabla.remove(input("Ingresar codigo del producto a eliminar: ")))
        elif choice == 4:
            print(tabla.load_Factor())
            print(tabla.longest_List())
            print(tabla.posiciones_Ocupadas())

        elif choice == 5:
            break
        else:
            print("Invalid choice")
        print()
