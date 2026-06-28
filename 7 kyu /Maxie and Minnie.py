def swap(number):
    s = list(str(number)) #do list and string in s
    n = len(s) # character count in s
    maxie = minnie = number
    for i in range(n): # selection of index pairs
        for j in range(i + 1, n): #cycle after i for nothing repetitions
            digits = s.copy() #copy list 
            digits[i], digits[j] = digits[j], digits[i] # change two digits
            if digits[0] != '0': #ignoring 0 in [0]
                current_num = int("".join(digits)) #join digits in one string
                if current_num > maxie: 
                    maxie = current_num #rewrites the number to the maximum from the previous one
                if current_num < minnie:
                    minnie = current_num #also with maxie but vice versa 
    return (maxie, minnie)
