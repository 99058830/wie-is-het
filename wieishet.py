print("De persoon kan een zwarte of blonde haarkleur hebben en een baard")

blackHair = input("Heeft de persoon een zwarte haarkleur? ")
if blackHair == "ja":
    hairLenght = input("Is het kapsel kort of lang? ")
    if hairLenght == "kort":
        print("Hij heeft een zwarte haarkleur en heeft een kort kapsel!")
    elif hairLenght == "lang":
        print("Hij heeft lang zwart haar")
    else: 
        print("Ik denk dat hij kaal is..")
if blackHair == "nee":
    blondeHair = input("Heeft hij blonde haarkleur? ")
    if blondeHair == "ja":
        hairLenght = input("Is het kapsel kort of lang? ")
        if hairLenght == "kort":
            print("Hij heeft een blonde haarkleur en heeft een kort kapsel!")
        elif hairLenght == "lang":
            print("Hij heeft lang blond haar")
        else:
            print("Ik denk dat hij kaal is..")
    else:
        print("Geen correcte gegevens ingevuld!")