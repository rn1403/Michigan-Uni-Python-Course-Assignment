hrs = int(input("Enter Hours:"))
rate = float(input("Enter rate per hour:"))
def computepay(hrs,rate):
    if hrs <= 40:
        grossPay = hrs*rate
    else:
        normalPay = 40*rate
        overtimePay = (hrs-40)*1.5*rate
        grossPay = normalPay+overtimePay
    return grossPay

print("Pay",computepay(hrs,rate))