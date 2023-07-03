class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")


class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit transaction with ID{self.transaction_id} processed_Amount: {self.amount}")


class WithdrawalTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withdrawal transaction with ID{self.transaction_id} processed_Amount: {self.amount}")


class PaymentTransaction(MpesaTransaction):
    def __init__(self, transaction_id, amount, recipient):
        super().__init__(transaction_id, amount)
        self.recipient = recipient

    def process_transaction(self):
        print(f"Payment transaction with ID{self.transaction_id} processed_Amount: {self.amount} "
              f"Recipient: {self.recipient}")


deposit = DepositTransaction(" DHTY", 2000)
deposit.process_transaction()
withdrawal = WithdrawalTransaction(" WRTY ", 5000)
withdrawal.process_transaction()
payment=PaymentTransaction(" Moneeeyyy ",20000,"Rubi")
payment.process_transaction()
