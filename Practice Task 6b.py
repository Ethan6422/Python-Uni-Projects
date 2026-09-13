import pickle

bank_account = []

with open ("bank_accounts.txt", "r") as infile:
    for row in infile:
        if not row.startswith("#"):
            row = row.rstrip("\n")
            account_num, balance = row.split(",")
            bank_account.append([int(account_num.strip()), int(balance.strip())])

print(bank_account)

out_outfile = open('bank.dat', 'wb')
pickle.dump(bank_account, out_outfile)
out_outfile.close()


with open('bank.dat', 'rb') as f:
    return pickle.load(f)