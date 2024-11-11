from abc import ABC, abstractmethod

# Clase base abstracta para productos
class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo protegido
        self._precio = precio

    @abstractmethod
    def descripcion(self):
        pass

    def get_precio(self):
        return self._precio

# Clases específicas que heredan de Producto
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def descripcion(self):
        return f"Camisa: {self._nombre}, Precio: {self._precio}, Talla: {self.talla}"

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def descripcion(self):
        return f"Pantalón: {self._nombre}, Precio: {self._precio}, Talla: {self.talla}"

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def descripcion(self):
        return f"Zapato: {self._nombre}, Precio: {self._precio}, Talla: {self.talla}"

# Clase Tienda que gestiona productos y el carrito de compras
class Tienda:
    def __init__(self):
        self.productos = []
        self.carrito = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for i, producto in enumerate(self.productos):
            print(f"{i + 1}. {producto.descripcion()}")

    def agregar_al_carrito(self, indice):
        if 0 <= indice < len(self.productos):
            producto = self.productos[indice]
            self.carrito.append(producto)
            print(f"{producto._nombre} añadido al carrito.")
        else:
            print("Índice de producto no válido.")

    def mostrar_carrito(self):
        if not self.carrito:
            print("El carrito está vacío.")
            return
        
        print("\nCarrito de compras:")
        total = sum(p.get_precio() for p in self.carrito)
        for producto in self.carrito:
            print(producto.descripcion())
        print(f"Total a pagar: {total}")

# Función principal para el menú interactivo
def menu():
    tienda = Tienda()
    
    # Agrega algunos productos a la tienda
    tienda.agregar_producto(Camisa("Camisa Blanca", 250, "M"))
    tienda.agregar_producto(Pantalon("Pantalón Negro", 400, "L"))
    tienda.agregar_producto(Zapato("Zapatos de Cuero", 600, 42))

    while True:
        print("\n--- Menú ---")
        print("1. Ver productos")
        print("2. Añadir producto al carrito")
        print("3. Ver carrito")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tienda.mostrar_productos()
        elif opcion == "2":
            try:
                indice = int(input("Indica el número del producto a añadir: ")) - 1
                tienda.agregar_al_carrito(indice)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "3":
            tienda.mostrar_carrito()
        elif opcion == "4":
            print("Gracias por tu compra.")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()