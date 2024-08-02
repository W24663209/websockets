for text in open('1.json').read().split("\n"):
    try:
        print(f"payOut('a711e39f4df14684', '{text.split(',')[0]}', '{text.split(',')[1]}')")
    except:
        pass
