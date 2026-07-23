import pygame.time

import Customer as c
import Settings as st
import GameState as gs
import random

all_orders: list[str] = list(st.DRINK_PRICES.keys())
orders_queue = []

customers = [
    c.Customer(st.standx + st.standwidth + (i * c.customer_space_between), st.groundy - c.radius, orders_queue[i])
    for i in range(len(orders_queue))]

MAX_QUEUE_SIZE = 5

last_spawn_time = 0
spawn_delay = random.randint(2000, 6000)

def update_queue():
    for i, customer in enumerate(customers):
        customer.x = st.standx + st.standwidth + (i * c.customer_space_between)


def serve_customer():
    if len(customers) > 0:
        # take the customer order index then earn_coins FOR that index only
        order = customers[0].order
        gs.earn_coins(st.DRINK_PRICES[order])
        customers.pop(0)
        update_queue()

def try_spawn_customer():
    global last_spawn_time, spawn_delay
    current_time = pygame.time.get_ticks()
    if len(customers) < MAX_QUEUE_SIZE and current_time - last_spawn_time >= spawn_delay:
        # append a NEW CUSTOMER(x, y, order) into queue
        rand_order = random.choice(all_orders)
        new_x = st.standx + st.standwidth + (len(customers) * c.customer_space_between)
        customers.append(c.Customer(new_x, st.groundy - c.radius, rand_order))
        last_spawn_time = current_time
        spawn_delay = random.randint(2000, 6000)