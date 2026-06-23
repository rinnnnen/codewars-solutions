def greet(language):
    languages_db = { #словарь (dict)
    "english": "Welcome",
    "danish": "Velkomst",
    "dutch": "Welkom",
    "estonian": "Tere tulemast",
    "finnish": "Tervetuloa",
    "flemish": "Welgekomen",
    "german": "Willkommen",
    "irish": "Failte",
    "italian": "Benvenuto",
    "latvian": "Gaidits",
    "czech": "Vitejte",
    "spanish": "Bienvenido",
    "french": "Bienvenue",
    "polish": "Witamy",
    "lithuanian": "Laukiamas",
    "swedish": "Valkommen",
    "welsh": "Croeso"
}
    return languages_db.get(language, "Welcome") # .get uses when The query does not match any variant of their dict.
