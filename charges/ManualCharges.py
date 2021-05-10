import decimal


class ChargeSystem:
    basic_charge = 25
    fee_per_min = 0.15
    fee = 0

    def __init__(self, phone_time, missed_payments):
        self.phone_time = phone_time
        self.missed_payments = missed_payments

    def condition(self):
        if self.phone_time < 0:
            print("通话分钟数不能小于0")
            return False
        if self.missed_payments < 0:
            print("未按时缴费次数不能小于0")
            return False
        if self.phone_time > 44640:
            print("通话分钟数超过最大时间限制")
            return False
        if self.missed_payments > 11:
            print("未按时缴费次数不能大于最大次数")
            return False
        return True

    def calculatedFee(self):
        if 0 <= self.phone_time <= 60 and self.missed_payments <= 1:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.01)
        elif 60 < self.phone_time <= 120 and self.missed_payments <= 2:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.015)
        elif 120 < self.phone_time <= 180 and self.missed_payments <= 3:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.02)
        elif 180 < self.phone_time <= 300 and self.missed_payments <= 3:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.025)
        elif 300 < self.phone_time and self.missed_payments <= 6:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.03)
        else:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time

        print("本月费用：" + str(round(self.fee, 7)))


def compute():
    record = input("请输入通话时长和未按时缴费次数（用\",\"分隔）:")
    phone_time = int(record.split(",")[0])
    missed_payments = int(record.split(",")[1])

    chargeSystem = ChargeSystem(phone_time, missed_payments)  # 实例化收费系统

    if chargeSystem.condition():
        chargeSystem.calculatedFee()


if __name__ == '__main__':
    compute()
