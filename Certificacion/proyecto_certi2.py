class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
                                                                         
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        if not self.withdraw(amount, f"Transfer to {category.name}"):
            return False
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def __str__(self):
        lines = [self.name.center(30, "*")]

        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f'{item["amount"]:>7.2f}'
            lines.append(description + amount)

        lines.append(f"Total: {self.get_balance()}")
        return "\n".join(lines)



def create_spend_chart(categories):
    title = "Percentage spent by category"

    spent = []
    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += -item["amount"]
        spent.append(category_spent)

    total_spent = sum(spent)
    if total_spent == 0:
        percentages = [0 for _ in spent]
    else:
        percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    lines = [title]

    for y in range(100, -1, -10):
        line = f"{y:>3}| "
        for p in percentages:
            line += "o  " if p >= y else "   "
        # No recortar espacios: los tests esperan longitud consistente.
        lines.append(line)

    lines.append("    " + "-" * (len(categories) * 3 + 1))

    names = [c.name for c in categories]
    max_len = max(len(n) for n in names) if names else 0
    for i in range(max_len):
        line = "     "
        for name in names:
            line += (name[i] if i < len(name) else " ") + "  "
        lines.append(line)

    return "\n".join(lines)