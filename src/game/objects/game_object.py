

class GameObject:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __le__(self, other):
        return self.z <= other.z

    def __lt__(self, other):
        return self.z < other.z

    def __ge__(self, other):
        return self.z >= other.z

    def __gt__(self, other):
        return self.z > other.z
