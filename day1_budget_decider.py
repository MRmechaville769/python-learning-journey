# Day 1: Budget Decision Program
budget = 2500
product_price = 800

print("=== Financial Decision Helper ===")
print(f"Budget: {budget} EGP")
print(f"Product Price: {product_price} EGP")

if product_price <= budget:
    print("✅ You can buy this")
    print(f"Remaining: {budget - product_price} EGP")
else:
    print("❌ Price exceeds budget")
    print(f"You need: {product_price - budget} EGP more")
    "day 1: budget decision program"
