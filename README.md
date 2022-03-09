# country_currencies
Data sources for currencies in json and delimited formats

Contains:
- the unicode symbol (if appropriate) for the currency, 
- standard number of decimal digits to display, 
- name of the currency and its subunit (for example, Dollar and Cent), and 
- matching plurals (Dollars and Cents) as well as 
- the unit conversion (e.g. 100 to 1) as that may not be reflected in the number of decimal digits, and
- position of the symbol (before or after the value)


Each country may have more than one currency, there are three files: curreny, countries, and country_currencies to reflect that data model.

Includes "countries" which may not be recognized by ISO or other standards orgs.  Those will have negative numeric country codes (e.g. -999) and 3-character alpha codes starting with an numeric value.

Includes "currencies" which may not be recognized by ISO or other standards (e.g. Antarctic Penguin).

Example:
`"JEP":{
              "currency_code":"JEP",         
              "currency_number":"-996",
              "standard_code":"F",
              "currency":"Jersey pound",
              "unit_singular":"Sterling",
              "unit_plural":"Sterlings",
              "subunit_singular":"Penny",
              "subunit_plural":"Pennies",
              "subunits_per_unit":"100",
              "digits_after_decimal":"2",
              "currency_symbol":"J£",
              "symbol_before_value":"F"
              },
`
