import numpy as np

# writes all numbers less than 28123 that are abundant
# abundant numbers are those that are LESS than the sum of their proper divisors
def write_small_abundant():
    abundant_numbers = []
    for i in range(12, 28123):
        print(i)
        proper_divisors = []
        for divisor in range(1, i):
            if i % divisor == 0:
                proper_divisors.append(divisor)
        if sum(proper_divisors) > i:
            abundant_numbers.append(i)
    file = open("static_data/small_appundant_numbers.txt", "w")
    np.savetxt(file, np.array(abundant_numbers, int))
    file.close()

def find_nonabundant_sums():
    abundant_numbers = np.loadtxt("static_data/small_appundant_numbers.txt").astype(int)
    target = []
    for i in range(13, 28124):
        print(i)
        L, R = 0, len(abundant_numbers)-1
        while(L <= R):
            if abundant_numbers[L] + abundant_numbers[R] == i:
                break
            elif abundant_numbers[L] + abundant_numbers[R] < i:
                L += 1
            else:
                R -= 1
        if L > R:
            target.append(i)
    print(sum(target))
if __name__ == "__main__":
#     write_small_abundant()
    find_nonabundant_sums()
