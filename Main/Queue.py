import pygame.time

import Customer as c
import Settings as st
import random

all_orders = ['Latte', 'Espresso', 'Matcha', 'Cappuccino', 'Hot Chocolate', 'Americano', 'Frappuccino', 'Mocha']
orders_queue = ['Latte', 'Espresso', 'Matcha']
customers = [
    c.Customer(st.standx + st.standwidth + (i * c.customer_space_between), st.groundy - c.radius, orders_queue[i])
    for i in range(len(orders_queue))]
MAX_QUEUE_SIZE = 5

def update_queue():
    for i, customer in enumerate(customers):
        customer.x = st.standx + st.standwidth + (i * c.customer_space_between)


def serve_customer():
    if len(customers) > 0:
        customers.pop(0)
        update_queue()

def try_spawn_customer():
    if len(customers) < MAX_QUEUE_SIZE:
        # append a NEW CUSTOMER(x, y, order) into queue
        rand_order = random.choice(all_orders)
        new_x = st.standx + st.standwidth + (len(customers) * c.customer_space_between)
        customers.append(c.Customer(new_x, st.groundy - c.radius, rand_order))
