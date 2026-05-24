import unittest

from order_system import Order, OrderLinkedList


class TestOrderLinkedList(unittest.TestCase):
    def test_append_and_display_three_orders(self) -> None:
        order_list = OrderLinkedList()
        order_list.append(Order("ORD-001", "Maya", "Phone Case", total=15.99))
        order_list.append(Order("ORD-002", "Jordan", "Headphones", total=79.99))
        order_list.append(Order("ORD-003", "Chris", "Tablet Stand", total=22.50))

        displayed_ids = [order.order_id for order in order_list.display()]

        self.assertEqual(displayed_ids, ["ORD-001", "ORD-002", "ORD-003"])

    def test_reverse_three_orders(self) -> None:
        order_list = OrderLinkedList()
        order_list.append(Order("ORD-001", "Maya", "Phone Case"))
        order_list.append(Order("ORD-002", "Jordan", "Headphones"))
        order_list.append(Order("ORD-003", "Chris", "Tablet Stand"))

        order_list.reverse()
        displayed_ids = [order.order_id for order in order_list.display()]

        self.assertEqual(displayed_ids, ["ORD-003", "ORD-002", "ORD-001"])

    def test_reverse_five_orders(self) -> None:
        order_list = OrderLinkedList()
        for order_number in range(1, 6):
            order_list.append(
                Order(f"ORD-00{order_number}", f"Customer {order_number}", f"Item {order_number}")
            )

        order_list.reverse()
        displayed_ids = [order.order_id for order in order_list.display()]

        self.assertEqual(
            displayed_ids,
            ["ORD-005", "ORD-004", "ORD-003", "ORD-002", "ORD-001"],
        )

    def test_reverse_empty_list(self) -> None:
        order_list = OrderLinkedList()

        order_list.reverse()

        self.assertEqual(order_list.display(), [])

    def test_reverse_single_order(self) -> None:
        order_list = OrderLinkedList()
        order_list.append(Order("ORD-001", "Maya", "Phone Case"))

        order_list.reverse()
        displayed_ids = [order.order_id for order in order_list.display()]

        self.assertEqual(displayed_ids, ["ORD-001"])

    def test_reverse_two_orders(self) -> None:
        order_list = OrderLinkedList()
        order_list.append(Order("ORD-001", "Maya", "Phone Case"))
        order_list.append(Order("ORD-002", "Jordan", "Headphones"))

        order_list.reverse()
        displayed_ids = [order.order_id for order in order_list.display()]

        self.assertEqual(displayed_ids, ["ORD-002", "ORD-001"])


if __name__ == "__main__":
    unittest.main()
