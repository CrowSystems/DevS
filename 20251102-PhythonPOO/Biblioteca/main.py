class Libro:
    def __int__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"{self.titulo} por {self.autor} disponible: {self.disponoble}"

    def cambiar_disponibilidad(self):
        if self.disponible:
            self.disponible = False


mi_libro = Libro("100 años de soledad","Gabriel García Marquez")
otro_libro = Libro("El principito","Saint-Exupéry")

print(f"mi_libro: {mi_libro.titulo} {mi_libro.autor}")        
print(f"mi_libro: {otro_libro.titulo} {otro_libro.autor}")        