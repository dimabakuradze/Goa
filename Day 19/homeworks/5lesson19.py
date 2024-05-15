"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""


def abbrev_name(name):
    name = name.upper()
    splited_name = name.split(" ")



    firstname = splited_name[0]
    lastname  = splited_name[1]


    result = firstname[0] + "." + lastname[0]


    return result



print(abbrev_name("dima bakuradze"))


