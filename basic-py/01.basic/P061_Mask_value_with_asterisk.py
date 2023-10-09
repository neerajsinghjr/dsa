def mask_parameter(param, last_4_key=True, first_last_key=False):
    stars = ''
    total_len = len(param)
    start = 0 if first_last_key else 0
    end =  1 if first_last_key else 4
    total_len = len(param)-end
    if first_last_key:
        for i in range(start, total_len): 
            stars  += '*'
        masked_value = "{}{}{}".format(param[start], stars, param[-end])
    else:
        for i in range(total_len):
            stars += '*'
        masked_value = stars + param[total_len:]
    return masked_value
    

if __name__ == '__main__':
    # xxx = mask_parameter("JOSPS9684Q", first_last_key=True)
    # print("xxx: ", xxx)

    # xxx:  ********9872
    xxx = mask_parameter("801704219872")
    print("xxx: ", xxx)

    # xxx:  ********7622
    xxx = mask_parameter("130401507622")
    print("xxx: ", xxx)
