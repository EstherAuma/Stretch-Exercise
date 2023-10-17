#Author: Esther
# tax_calculator.py

def calculate_tax(earnings):
    if earnings < 12000:
        return 0
    elif 12000 <= earnings <= 36000:
        return (earnings - 12000) * 0.20
    else:
        return (earnings - 36000) * 0.40 + 4800  # 20% tax on the first 24000, then 40% on the rest

if __name__ == '__main__':
    earnings = float(input("Enter your annual earnings: "))
    tax = calculate_tax(earnings)
    print(f"Tax owed: ${tax:.2f}")
