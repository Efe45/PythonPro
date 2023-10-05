meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "CREEPY":"Korkunc",
            "AGGRO": "Agresiflesmek"
    
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
word = word.upper()

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Kelime sozlukte bulunmadi")