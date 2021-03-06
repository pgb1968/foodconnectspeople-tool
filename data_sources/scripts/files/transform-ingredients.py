#!/usr/bin/python3
#
# Transform a line like:
#   almond,TRUE,TRUE,TRUE,TRUE,FALSE
#
# into:
#   24, almond, __vegetarian__vegan__,
#
# and one like:
#   butter,TRUE,FALSE,TRUE,FALSE,FALSE
#
# into:
#   28, butter, __vegetarian__, __lactose__


separator = ','

# Separator for elements in the (output) fields properties and allergenes
like_separator = '__'

if __name__ == '__main__':
    line_number = 0
    with open('ingredients.csv', encoding='utf-8') as ingredients:
        for line in ingredients:
            # Skip 1st line (headers)
            if line_number == 0:
                line_number += 1
                continue

            # A line contains 6 fields:
            #ingredient,is_vegetarian,is_vegan,is_gluten_free,is_lactose_free,is_spice
            fields = line.split(separator)
            if len(fields) != 6:
                print("Corrupted line " + str(line_number))
                print(line)
                continue

            # Result must be a line whose fields are:
            # 0. ID (the line number)
            # 1. name (from field[0])
            # 2. properties: take fields 1,2,5 and concatenate them into a string
            # 3. allergenes: take fields 3,4 and write the values "gluten" and
            #   "lactose" where FALSE appears in the corresponding position.
            res = str(line_number) + separator + fields[0] + separator
            properties = []
            if fields[1] == "TRUE":
                properties.append('vegetarian')
            if fields[2] == "TRUE":
                properties.append('vegan')
            if fields[5] == "TRUE":
                properties.append('spice')
            if len(properties) > 0:
                res += '__'
                res += ('__').join(properties)
                res += '__' + separator
            else:
                res += separator

            allergenes = []
            if fields[3] == "FALSE":
                allergenes.append('gluten')
            if fields[4] == "FALSE":
                allergenes.append('lactose')
            if len(allergenes) > 0:
                res += '__'
                res += ('__').join(allergenes)
                res += '__'

            print(res)
            line_number += 1

