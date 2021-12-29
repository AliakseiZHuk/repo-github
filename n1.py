my_list = [ 4, {2, 3.3}, True, False, bytearray(b"some text"), type(None)]

for i, item in enumerate(my_list, 1):
         print(f"{i}) {item} - {type(item)}")
