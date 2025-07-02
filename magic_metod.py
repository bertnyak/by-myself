class Vector:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            # Скалярное умножение
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            # Векторное произведение
            return Vector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        else:
            raise TypeError("Можно умножать только на число или другой вектор")
    
    def dot(self, other: 'Vector') -> float:
        """Скалярное произведение векторов"""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def magnitude(self) -> float:
        """Длина вектора"""
        return (self.x**2 + self.y**2 + self.z**2)**0.5


# Примеры использования
if __name__ == "__main__":
    # Создаем векторы
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    
    # Сложение векторов
    v3 = v1 + v2
    print(f"Сложение векторов v1 + v2 = {v3}")
    
    # Вычитание векторов
    v4 = v2 - v1
    print(f"Вычитание векторов v2 - v1 = {v4}")
    
    # Умножение на скаляр
    v5 = v1 * 2
    print(f"Умножение на скалярv1 * 2 = {v5}")
    
    # Векторное произведение
    v6 = v1 * v2
    print(f"Векторное произведение v1 × v2 = {v6}")
    
    # Скалярное произведение
    dot_product = v1.dot(v2)
    print(f"Скалярное произведение v1 · v2 = {dot_product}")
    
    # Длина вектора
    magnitude_v1 = v1.magnitude()
    print(f"Длина векторов |v1| = {magnitude_v1}")
    