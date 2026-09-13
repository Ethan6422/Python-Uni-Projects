bank_account = []

with open ("bank_accounts.txt", "r") as infile:
    for row in infile:
        if not row.startswith("#"):
            row = row.rstrip("\n")
            account_num, balance = row.split(",")
            bank_account.append([int(account_num.strip()), int(balance.strip())])

print(bank_account)

found = False
while not found:
    number = int(input("Enter an account number: "))

    for account in bank_account:
        if account[0] == number:
            print(F"Account {number} found")
            found = True

    if found:
        break
    else:
        print("Account not found")
