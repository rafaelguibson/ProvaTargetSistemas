def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def is_fibonacci(num, i=0):
    fib = fibonacci(i)
    if fib == num:
        return True
    elif fib > num:
        return False
    else:
        return is_fibonacci(num, i + 1)

def main():
    number = int(input("Informe um número: "))

    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci. ")
    else:
        print(f"O número {number} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
