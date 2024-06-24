hrs = int(input("Enter Hours:"))
rate = float(input("Enter rate per hour:"))
if hrs <= 40:
    grossPay = hrs*rate
else:
    normalPay = 40*rate
    overtimePay = (hrs-40)*1.5*rate
    grossPay = normalPay+overtimePay
print("Pay:",grossPay)
