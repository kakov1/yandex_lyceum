def number_in_english(number):
    one = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
           6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
           11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
           16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 0: 'zero'}
    two = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
           60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred'}
    if number in one.keys():
        return one[number]
    elif number in two.keys():
        return two[number]
    else:
        if len(str(number)) == 2:
            return f'{two[int(str(number)[0]) * 10]} {one[int(str(number)[1])]}'
        else:
            if int(str(number)[1:]) in one.keys():
                return f'{one[int(str(number)[0])]} hundred and {one[int(str(number)[1:])]}'
            elif int(str(number)[1:]) in two.keys():
                return f'{one[int(str(number)[0])]} hundred and {two[int(str(number)[1:])]}'
            else:
                return f'{one[int(str(number)[0])]} hundred and {two[int(str(number)[1]) * 10]}' \
                       f' {one[int(str(number)[2])]}'
