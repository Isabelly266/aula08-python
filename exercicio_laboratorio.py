matrícula = input("Voce está matriculado?")
if matrícula == "sim":
    autorização = input("Possui autorização?")
    if autorização == "sim":
        print ("Acesso permitido")
    else:
        print ("Autorização necessária")
else:
    print ("Matrícula necessária")