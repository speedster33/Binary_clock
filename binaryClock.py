import time

def main():
    while True:
        binary_time()
        time.sleep(1)
        print("\033[H\033[J")


def binary_time():
    time_tupple = time.localtime()
    time_list = [
        time_tupple[3] // 10,     #10 hour digit, index 0
        int(time_tupple[3] % 10), #1  hour digit, index 1
        time_tupple[4] // 10,     #10 minute digit, index 2
        int(time_tupple[4] % 10), #1  minute digit, index 3
        time_tupple[5] // 10,     #10 second digit, index 4
        int(time_tupple[5] % 10)  #1  second digit, index 5
    ]
    for x in range(len(time_list)):
        time_list[x] = decimal_to_binary(time_list[x])

    format_binary_time(time_list)


def decimal_to_binary(decimal):
    binary_list = []
    n = 8 
    while n >= 1:
        one_or_zero = 0
        if decimal - n >= 0:
            decimal -= n
            one_or_zero = 1

        n /= 2 
        binary_list.append(one_or_zero) 
    return binary_list


def format_binary_time(time_list):
    index = 0
    for binary_digits in range(len(time_list[index])):
        for digits in range(len(time_list)):
            print(str(time_list[digits][binary_digits]), end = " ")
        print()


if __name__ == '__main__':
    main()