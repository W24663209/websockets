for text in open('1.json').read().split("\n"):
    try:
        print(f"payOut('ed33cc088d6226ef', '{text.split(',')[0]}', '{text.split(',')[1]}')")
    except:
        pass
