'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

MAX_ITEMS_IN_ORDER = 100
MAX_ORDER_COST = 1e9
MAX_ITEM_COST = 1e6

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def is_reasonable_cost_gen(max_cost):
    """Not empty"""
    def worker(cost):
        return cost > max_cost * -1 and cost < max_cost

    return worker

is_reasonable_order_cost = is_reasonable_cost_gen(MAX_ORDER_COST)
is_reasonable_item_cost = is_reasonable_cost_gen(MAX_ITEM_COST)

def validorder(order: Order):
    """Not empty"""
    net = 0

    for item in order.items:
        if item.type == 'payment':
            if is_reasonable_order_cost(item.amount):
                net += Decimal(item.amount)
        elif item.type == 'product':
            if is_reasonable_item_cost(item.amount) and item.quantity < MAX_ITEMS_IN_ORDER:
                net -= Decimal(item.amount) * Decimal(item.quantity)
        else:
            return f"Invalid item type: {item.type}"

    if net < 0:
        return f"Order ID: {order.id} - Payment imbalance: ${net:0.2f}"

    return f"Order ID: {order.id} - Full payment received!"
