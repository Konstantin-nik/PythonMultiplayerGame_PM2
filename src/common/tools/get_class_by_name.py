from src.common.actions import Action, JumpAction, ShootAction, MoveAction, SpawnAction, TalkAction
from src.game.objects.game_object import GameObject
from src.game.objects.game_objects import GameObjects
from src.game.objects.player.player import Player


def get_class_by_name(name):
    match name:
        case 'GameObject':
            return GameObject
        case 'GameObjects':
            return GameObjects
        case 'Player':
            return Player
        case 'Action':
            return Action
        case 'JumpAction':
            return JumpAction
        case 'ShootAction':
            return ShootAction
        case 'MoveAction':
            return MoveAction
        case 'SpawnAction':
            return SpawnAction
        case 'TalkAction':
            return TalkAction

    return None
