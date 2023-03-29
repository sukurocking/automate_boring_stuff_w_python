def picnic_print(items_dict, left_width, right_width):
    print("PICNIC ITEMS".center(left_width + right_width, "-"))
    for k, v in items_dict.items():
        print(k.ljust(left_width,".") + str(v).rjust(right_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
picnic_print(picnic_items, 12, 5)
picnic_print(picnic_items, 20, 6)