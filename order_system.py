from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    customer: str
    details: str
    status: str = "Pending"
    total: float = 0.0

    def __str__(self) -> str:
        return (
            f"Order ID: {self.order_id}, Customer: {self.customer}, "
            f"Details: {self.details}, Status: {self.status}, Total: ${self.total:.2f}"
        )


class Node:
    def __init__(self, order: Order) -> None:
        self.order = order
        self.next = None


class OrderLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, order: Order) -> None:
        new_node = Node(order)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self) -> list[Order]:
        orders = []
        current = self.head

        while current is not None:
            orders.append(current.order)
            current = current.next

        return orders

    def reverse(self) -> None:
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


def print_orders(title: str, orders: list[Order]) -> None:
    print(title)
    if not orders:
        print("No orders in the list.")
        return

    for order in orders:
        print(order)


def main() -> None:
    order_list = OrderLinkedList()

    order_list.append(Order("ORD-101", "Ava Johnson", "Laptop", "Processing", 899.99))
    order_list.append(Order("ORD-102", "Liam Smith", "Wireless Mouse", "Shipped", 24.99))
    order_list.append(Order("ORD-103", "Noah Davis", "Keyboard", "Delivered", 49.99))

    print_orders("Orders in original order:", order_list.display())

    order_list.reverse()
    print()
    print_orders("Orders after reversing the linked list:", order_list.display())


if __name__ == "__main__":
    main()
