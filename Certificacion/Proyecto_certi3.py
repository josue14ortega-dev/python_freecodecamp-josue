""""
PROTECTO DE CERTIFICACION FREECODECAMP
Proyecto de computación científica desarrollado en Python. Implementación de clases Rectangle y Square utilizando conceptos de herencia y POO.
NOMBRE: JOSUE
FECHA: 23-ABRIL-2026"""

class Rectangle:
    """Clase que representa un rectángulo y permite calcular propiedades geométricas."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        """Devuelve una representación en texto del rectángulo."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """Actualiza el ancho del rectángulo."""
        self.width = width

    def set_height(self, height):
        """Actualiza la altura del rectángulo."""
        self.height = height

    def get_area(self):
        """Calcula y devuelve el área: base * altura."""
        return self.width * self.height

    def get_perimeter(self):
        """Calcula y devuelve el perímetro: 2 * (base + altura)."""
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """Calcula la diagonal usando el Teorema de Pitágoras."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Genera una representación visual del rectángulo con asteriscos."""
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        """Calcula cuántas veces cabe otra figura (shape) dentro de esta."""
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    """Subclase de Rectangle que representa un cuadrado."""
    
    def __init__(self, side):
        # Inicializa ambos lados con la misma medida
        super().__init__(side, side)

    def __str__(self):
        """Devuelve una representación en texto del cuadrado."""
        return f"Square(side={self.width})"

    def set_side(self, side):
        """Establece el ancho y la altura con el mismo valor."""
        self.width = side
        self.height = side

    def set_width(self, side):
        """Sobrescribe set_width para mantener la propiedad de cuadrado."""
        self.set_side(side)

    def set_height(self, side):
        """Sobrescribe set_height para mantener la propiedad de cuadrado."""
        self.set_side(side)
        


rect = Rectangle(10, 5)
print(rect.get_area()) 

sq = Square(5)
print(sq.get_perimeter()) 