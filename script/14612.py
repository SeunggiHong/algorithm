class Restaurant:
    def __init__(self):
        self.orders = []

    def order(self, n, t):
        self.orders.append((t, n))

    def sort(self):
        self.orders.sort(key=lambda x: (x[0], x[1]))

    def complete(self, n):
        for i in range(len(self.orders)):
            if self.orders[i][1] == n:
                self.orders.pop(i)
                return

    def show_orders(self):
        return [order[1] for order in self.orders]

def main():
    N, M = map(int, input().strip().split())
    restaurant = Restaurant()
    
    for _ in range(N):
        command = input().strip().split()
        cmd = command[0]

        if cmd == "order":
            tableNum = int(command[1])
            orderTime = int(command[2])
            restaurant.order(tableNum, orderTime)

        elif cmd == "complete":
            tableNum = int(command[1])
            restaurant.complete(tableNum)

        else:
            restaurant.sort()

        current_orders = restaurant.show_orders()
        if not current_orders:
            print("sleep")
        else:
            print(" ".join(map(str, current_orders)))

if __name__ == "__main__":
    main()
