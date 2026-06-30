import asyncio


class Bankomat:
    def __init__(
        self,
        banknotes: dict,
    ):
        self.banknotes: dict = banknotes
        self.lock = asyncio.Lock()

    def deposit_banknote(self, banknote, banknote_count):
        if banknote in self.banknotes:
            self.banknotes[banknote] += banknote_count
        else:
            self.banknotes[banknote] = banknote_count
        return "Деньги зачислены"

    def get_total_amount(self):
        total = 0
        for k, v in self.banknotes.items():
            total += k * v
        return total

    async def withdraw(self, amount):
        async with self.lock:
            result = {}
            # остаток
            remaining = amount
            for nominal in sorted(self.banknotes, reverse=True):
                take = min(remaining // nominal, self.banknotes[nominal])
                if take == 0:
                    continue
                result[nominal] = take
                remaining -= nominal * take
            if remaining != 0:
                return f"Невозможно выдать эту сумму - {amount} рублей"
            await asyncio.sleep(1)
            for nominal, count in result.items():
                self.banknotes[nominal] -= count
            return result


# b1 = Bankomat(
#     {
#         1000: 5,
#         5000: 3,
#         500: 100,
#         100: 25,
#     }
# )
# print(b1.get_total_amount())
# print(b1.withdraw(3500))
# print(b1.banknotes)
# print(b1.withdraw(500))
# print(b1.banknotes)
# print(b1.withdraw(3750))
# print(b1.get_total_amount())
if __name__ == "__main__":

    async def main():
        b = Bankomat(
            {
                1000: 3,
                5000: 4,
                # 500: 6,
                100: 7,
            }
        )
        task1 = asyncio.create_task(b.withdraw(2000))
        task2 = asyncio.create_task(b.withdraw(2000))
        result = await asyncio.gather(task1, task2)
        print(result)
        print(b.banknotes)

    asyncio.run(main())
