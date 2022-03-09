import io
filename = r'z:\currencies.txt'
f = io.open(filename,encoding='utf-16')

try:
    while (True):
        line = f.readline()
        contentR = line.split('\n')[0].split('\t')
        coded = contentR[0:1]+contentR[0:]
        content = tuple(coded)
        print(u'''"%s":{
              "currency_code":"%s",
              "currency_number":"%s",
              "standard_code":"%s",
              "unit_singular":"%s",
              "currency":"%s",
              "unit_plural":"%s",
              "subunit_singular":"%s",
              "subunit_plural":"%s",
              "subunits_per_unit":"%s",
              "digits_after_decimal":"%s",
              "currency_symbol":"%s",
              "symbol_before_value":"%s"
              },'''
            %(content))
finally:

    f.close()

filename = r'z:\country_currencies.txt'
f = io.open(filename,encoding='utf-16')

try:
    while (True):
        line = f.readline()
        contentR = line.split('\n')[0].split('\t')
        coded = contentR[1:2]+contentR[0:]
        content = tuple(coded)
        print(u'''"%s":{
              "country_name":"%s",
              "country_code":"%s",
              "numeric_code":"%s",
              "currency_code":"%s"
              },'''
            %(content))
finally:

    f.close()

filename = r'z:\countries.txt'
f = io.open(filename,encoding='utf-16')

try:
    while (True):
        line = f.readline()
        contentR = line.split('\n')[0].split('\t')
        coded = contentR[3:4]+contentR[0:5]
        content = tuple(coded)
        print(u'''"%s":{
              "english_short_name":"%s",
              "french_short_name":"%s",
              "alpha_2_code":"%s",
              "alpha_3_code":"%s"
              "numeric_code":"%s"
              },'''
            %(content))
finally:

    f.close()

