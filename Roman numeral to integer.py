def roman_to_int(roman_numeral):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    previous_value = 0
    
    for numeral in roman_numeral[::-1]:
        current_value = roman_values[numeral]
        
        # If the previous value is smaller than the current value, subtract the previous value from the result.
        if previous_value > current_value:
            result -= current_value
        # Otherwise, add the current value to the result.
        else:
            result += current_value
        
        # Update the previous value for the next iteration.
        previous_value = current_value
    
    return result


print(roman_to_int('III')) 
print(roman_to_int('IX'))  
print(roman_to_int('LVIII'))  
print(roman_to_int('XXX'))
print(roman_to_int('MMMM'))
