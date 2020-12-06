with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def check_password(string, part_one = True):

    split = string.split(':')

    password = split[1].strip()
    policy = split[0].split(' ')

    policy_letter = policy[1]

    numbers = policy[0].split('-')

    min_limit = int(numbers[0])
    max_limit = int(numbers[1])

    occurances = password.count(policy_letter)

    if part_one:

        if occurances >= min_limit and occurances <= max_limit:
            return 1
        else:
            return 0

    else:

        # Get letters at index
        to_check = password[min_limit - 1] + password[max_limit -1]

        if to_check.count(policy_letter) == 1:
            return 1
        else:
            return 0


part_one = 0
part_two = 0

for password in lines:

    part_one += check_password(password, part_one=True)
    part_two += check_password(password, part_one=False)


print(f'Part one: {part_one}')
print(f'Part two: {part_two}')

