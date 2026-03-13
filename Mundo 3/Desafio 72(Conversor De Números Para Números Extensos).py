extece_number:tuple = (
        'one','two','three','four','five','six','seven','eight','nine','ten',
        'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty'
            )
while True:
    try:
        number:input = int(input("Read Number:"))
    except ValueError:
        print("ERR")
        continue
    if  number < 1 or number > 20: 
        print("ERR") 
        continue
    print("Number In Extence:",extece_number[number-1])
    while True:#Ext
        exit:input = input("Think To Exit?[Y/N]:").upper().strip()[0]
        if exit in ['Y','N']:   break
        else:   continue
    if exit == 'Y': break