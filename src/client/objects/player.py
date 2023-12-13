import yaml


class Player:
    def __init__(self, name, coords, colors):
        self.name = name
        self.coords = coords
        self.colors = colors

    def __eq__(self, other):
        return (self.name == other.name) and (self.coords == other.coords) and (self.colors == other.colors)


player_1 = Player(name='Petya', coords=(10, 9), colors=(1, 0, 3))

yaml_string = yaml.dump(player_1.__dict__)
print(yaml_string)

yaml_data = yaml.full_load(yaml_string)
player_2 = Player(**yaml_data)
print(player_1 == player_2)
