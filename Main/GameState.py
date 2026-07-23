# GameState.py — owns all live game data
coins = 0
days_played = 1

def earn_coins(amount: int) -> None:
    global coins
    coins += amount

def spend_coins(amount: int) -> bool:
    global coins
    if coins >= amount:
        coins -= amount
        return True
    return False  # can't afford it!