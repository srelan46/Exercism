def is_valid(isbn):
    clean_number = isbn.replace("-", "")
    
    # 1. Check length first
    if len(clean_number) != 10:
        return False
        
    total = 0
    count = 10
    
    # 2. Loop through and check characters properly
    for index, char in enumerate(clean_number):
        # ISBN-10 allows 'X' (value 10) but ONLY as the very last character
        if char.upper() == 'X' and index == 9:
            digit_value = 10
        elif char.isdigit():
            digit_value = int(char)
        else:
            return False  # Invalid character found
            
        # 3. Use += to accumulate the sum
        total += digit_value * count
        count -= 1
        
    return total % 11 == 0
