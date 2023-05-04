def number_to_time(num):
    quotient = num // 60
    remainder = num % 60
    if quotient < 2:
        quotient =  str(quotient) + " hour, " 
    else:
        quotient = str(quotient) + " hours, "
    if remainder < 2:
        remainder = str(remainder) + " minute"
    else:
        remainder = str(remainder) + " minutes"
    return quotient + remainder
