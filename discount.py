priceitem=input().strip()
prime_digits={'2','3','5','7'}
discount=sum(int(digit)for digit in priceitem if digit in prime_digits)
print(discount)
