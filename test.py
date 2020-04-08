import json


fr = open(r'./Loans.json')

jippie = json.load(fr)

data = {
            "ik": "hallo",
            "jij": "hallo"
        }

jippie.append(data)

print(jippie)

fr.close()

fw = open(r'./Loans.json','w',newline='\n')

json.dump(jippie,fw)


