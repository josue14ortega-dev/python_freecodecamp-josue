"""
Name: Josue Ortega
Date: 21-Abril-2026
Lab #9
Player Interface


"""
import abc
import random

class Player(abc.ABC):
    def __init__(self):
        # Inicialización de atributos base
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        # 10. Selección aleatoria
        selected_move = random.choice(self.moves)
        
        # 11. Actualización de la posición (x + dx, y + dy)
        new_x = self.position[0] + selected_move[0]
        new_y = self.position[1] + selected_move[1]
        self.position = (new_x, new_y)
        
        # 12. Registro en el historial
        self.path.append(self.position)
        
        # 13. Retorno de la posición actualizada
        return self.position

    @abc.abstractmethod
    def level_up(self):
        """Método abstracto para ser implementado en subclases."""
        pass

class Pawn(Player):
    def __init__(self):
        # 22. Llamada obligatoria al constructor del padre
        super().__init__()
        
        # 23. Movimientos iniciales: arriba, abajo, izquierda, derecha
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # 25. Adición de movimientos diagonales
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)