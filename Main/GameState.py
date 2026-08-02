# GameState.py — owns all live game data

coins = 0
upgrades_spent_today = 0
drinks_served_today = 0
coins_earned_today = 0
orders_today = {}

def earn_coins(amount: int) -> None:
    global coins, drinks_served_today, coins_earned_today
    coins += amount
    coins_earned_today += amount
    drinks_served_today += 1

def track_order(order: str) -> None:
    orders_today[order] = orders_today.get(order, 0) + 1

def reset_daily_stats() -> None:
    global coins_earned_today, drinks_served_today, upgrades_spent_today
    coins_earned_today = 0
    drinks_served_today = 0
    upgrades_spent_today = 0
    orders_today.clear()

def spend_coins(amount: int) -> bool:
    global coins, upgrades_spent_today
    if coins >= amount:
        coins -= amount
        upgrades_spent_today += amount
        return True
    return False  # can't afford it!