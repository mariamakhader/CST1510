

# Name  : Mariam Khader
# Lane  :  AI       
# Date  : 29/09/2026


label = input("Enter label: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))

if value >= limit:
    status = "OVER LIMIT"
else:
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"Label: {label}")
print(f"Value: {value}")
print(f"Limit: {limit}")
print(f"Status: {status}")

print("=" * 34)
