def intToRoman(num: int) -> str:
        value = ''
        romanNumerals = [
            (1, 'I', 'X', 'C', 'M'), 
            (2, 'II', 'XX', 'CC', 'MM'), 
            (3, 'III', 'XXX', 'CCC', 'MMM'), 
            (4, 'IV', 'XL', 'CD', ''),
            (5, 'V', 'L', 'D', ''),
            (6, 'VI', 'LX', 'DC', ''), 
            (7, 'VII', 'LXX', 'DCC', ''), 
            (8, 'VIII', 'LXXX', 'DCCC', ''),
            (9, 'IX', 'XC', 'CM', ''),  
        ]
        powerOfTen = 1
        for i in str(num)[::-1]:
            i = int(i)
            if i != 0: 
                value = romanNumerals[i-1][powerOfTen] + value
            powerOfTen += 1
        return value
    
print(intToRoman(3749))
print(intToRoman(58))
print(intToRoman(1994))