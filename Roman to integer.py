#Python code to conver Roman numbers into integers 

class RomanNumeral:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def roman_to_int(self, s):
        converted_number = 0

        for i in range(len(s)):
            current_number = self.roman_map[s[i]]
            next_number = self.roman_map[s[i + 1]] if i + 1 < len(s) else 0

            if current_number < next_number:
                converted_number -= current_number
            else:
                converted_number += current_number

        return converted_number



roman = RomanNumeral()
print(roman.roman_to_int("XIV"))  
print(roman.roman_to_int("MCMXCIV")) 
