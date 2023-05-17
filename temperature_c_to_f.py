# F = C * 9 / 5 + 32
# C = (F - 32) * 5 / 9
# 讓使用者輸入攝氏(C)溫度, 然後轉換成華氏(F)溫度
temp_c = input('Please enter the Celsius tempurature: ')
temp_c = float(temp_c)
temp_f = temp_c * 9 / 5 + 32
temp_f = float(temp_f)
print('Fahrenheit is', temp_f, '.')