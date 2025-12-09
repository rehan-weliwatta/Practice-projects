print("Sri Lanka Income Tax calculator 2025")
print("------------------------------------")

monthly_income = int(input("Enter monthly income :"))
annual_income = monthly_income * 12

print(f"Annual income :{annual_income}")

if annual_income <= 500000:
    annual_tax = annual_income / 100 *6
    print(f"Monthly tax : {annual_tax / 12}")
    print(f"Annual tax :{annual_tax}")

elif annual_income >= 500001 or annual_income <= 1000000:
    annual_tax = ((annual_income - 500000)/100 * 12) + (500000 / 100 * 6)
    print(f"Monthly tax : {annual_tax / 12}")
    print(f"Annual tax :{annual_tax}")

elif annual_income >= 1000001 or annual_income <= 1500000:
    annual_tax = ((annual_income - 1000000)/100 * 18) + (500000 / 100 * 12) + (500000 / 100 * 6)
    print(f"Monthly tax : {annual_tax / 12}")
    print(f"Annual tax :{annual_tax}")

elif annual_income >= 1500001 or annual_income <= 2000000:
    annual_tax = ((annual_income - 1500000)/100 * 24) + (500000 / 100 * 18) + (500000 / 100 * 12) + (500000 / 100 * 6)
    print(f"Monthly tax : {annual_tax / 12}")
    print(f"Annual tax :{annual_tax}")

elif annual_income >= 2000001 or annual_income <= 2500000:
    annual_tax = ((annual_income - 2000000)/100 * 30) + (500000 / 100 * 24) + (500000 / 100 * 18) + (500000 / 100 * 12) + (500000 / 100 * 6)
    print(f"Monthly tax : {annual_tax / 12}")
    print(f"Annual tax :{annual_tax}")

elif annual_income >= 2500001:
    annual_tax = ((annual_income - 2500000)/100 * 36) + (500000 / 100 * 30)  + (500000 / 100 * 24) + (500000 / 100 * 18) + (500000 / 100 * 12) + (500000 / 100 * 6)
    print(f"Monthly tax : {annual_tax / 12}")
    print(f"Annual tax :{annual_tax}")

print("------------------------------------")