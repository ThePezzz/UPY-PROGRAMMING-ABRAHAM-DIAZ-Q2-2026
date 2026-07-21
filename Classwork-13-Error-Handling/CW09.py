pronouns = ['Yo', 'Tú', 'Él', 'Nosotros', 'Vosotros', 'Ellos']

endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verb = input("Write a spanish verb (ar/er/ir): ")

if verb != verb.strip():
    print("El verbo no debe tener espacios extra")
elif verb != verb.lower():
    print("El verbo debe escribirse en minusculas")
else:
    stem = verb[:-2]
    ending = verb[-2:]

    try:
        conjugations = endings[ending]
    except KeyError:
        print("El verbo debe terminar en ar, er o ir")
    else:
        for index, pronoun in enumerate(pronouns):
            print(f"{pronoun} {stem}{conjugations[index]}")
