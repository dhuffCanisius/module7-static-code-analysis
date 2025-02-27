"""
This module checks if a number is prime
"""
def check_if_prime():
    i, temp = 0, 0
    n = int(str(int(input("please give a number : "))))
    for i in range(2, n // 2):
        if n % i == 0:
            temp=1
            break
    if temp == 1:
        return "given number is not prime"
    return "given number is prime"

if __name__ == "__main__":
    print(check_if_prime)