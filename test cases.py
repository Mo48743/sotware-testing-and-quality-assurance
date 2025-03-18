class RomanNumeral:
 #implementing test cases
    
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def roman_to_int(self, s):
        if not s:  # when the is  Null 
            return 0
        
        converted_number = 0
        prev_number = 0

        for char in s:
            if char not in self.roman_map:  
                return "Error: Invalid Roman numeral"
            
            current_number = self.roman_map[char]

            if prev_number and prev_number < current_number:  
               
                converted_number += current_number - 2 * prev_number
            else:
                converted_number += current_number

            prev_number = current_number
        
        invalid_cases = ["VV", "LL", "DD", "IIII", "XXXX", "CCCC", "MMMM"]
        for case in invalid_cases:
            if case in s:
                return "Error: Invalid Roman numeral repetition"

        return converted_number


# Test cases
test_cases = ["I", "V", "X", "L", "C", "D", "M", "XI", "IV", "XIV", "II", "I", "Z", "XIZ", "VV", ""]
roman = RomanNumeral()

for test in test_cases:
    print(f"Input: {test} -> Output: {roman.roman_to_int(test)}")
