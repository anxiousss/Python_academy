def solution(elf_number, dwarf_number, people_number):
    elf_first_digit = elf_number // 10
    elf_second_digit = elf_number % 10

    dwarf_first_digit = dwarf_number // 10
    dwarf_second_digit = dwarf_number % 10

    people_first_digit = people_number // 10
    people_second_digit = people_number % 10

    if elf_first_digit == dwarf_first_digit == people_first_digit:
        print(elf_first_digit)

    if elf_second_digit == dwarf_second_digit == people_second_digit:
        print(elf_second_digit)


def main():
    elf_number = int(input())
    dwarf_number = int(input())
    people_number = int(input())
    solution(elf_number, dwarf_number, people_number)


if __name__ == '__main__':
    main()
