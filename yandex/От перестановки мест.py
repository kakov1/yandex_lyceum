# при сложении чисел данными операциями мы получим числа с одним и тем же id
value = 1
addition = 2
value = value + addition
print(value)
value_ = 1
addition = 2
value_ += addition
print(value_)
print(id(value) == id(value_))
# при сложении списков данными операциями мы получим одинаковые внешне списки, но с разными id
value = [1, 2]
addition = [3, 4]
value = value + addition
print(value)
value_ = [1, 2]
addition = [3, 4]
value_ += addition
print(value_)
print(id(value) == id(value_))

