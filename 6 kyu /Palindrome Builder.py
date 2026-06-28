def build_palindrome(s: str) -> str:
    option_front = "" # do empty value 
    for i in range(len(s), 0, -1): # reverse line count for find most bigger part
        if s[:i] == s[:i][::-1]: # [:i] - slice a string from the beginning to the index; [:i][::-1] - also this slice but reverse
            option_front = s[i:][::-1] + s # if string upper == palindrome => s[i:] reverse and attach to end
            break
    option_back = ""
    for i in range(len(s)): # cycle go standard from zero to end
        if s[i:] == s[i:][::-1]: #[i:] - slice the string from the index i to end; check palindrome
            option_back = s + s[:i][::-1] # unfold the extra and insert it into he end
            break
    if len(option_front) <= len(option_back): # measure their length, further if else who smaller
        return option_front
    else:
        return option_back
