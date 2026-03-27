def identify_ip(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return "invalid IP Address"

    try:
        nums = [int(part) for part in parts]

    except ValueError:
        return "Invalid IP Address (non-numeric value inputted"

    for num in nums:
        if num < 0 or num > 225:
            return "Invalid IP (out of range)"


    first = nums[0]

    
    if first == 127:
        return "IP type: Localhost"
    if first == 10:
        return "Private Class A IP"
    if first == 172 and 16 <= nums[1] <= 31:
        return "Private Class B IP"
    if first == 192 and nums[1] == 168:
        return "Private Class C IP"
    if ip == "0.0.0.0":
        return "Invalid IP"

    if ip == "225.225.225.225":
        return "Broadcast Address"



    if 1 <=first <= 126 :
        return "Class A Ip Address"

    elif 128 <= first <= 191:
        return "Class B IP Address"
    elif 192 <= first <= 223:
        return "Class C IP Address"
    else:
        return "Reserved or Mu;ticast"

    
ip_input = input("Enter an IP Address: ")
result = identify_ip(ip_input)
print("Result: ", result)

