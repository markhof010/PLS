import json


fr = open(r'C:\\Users\\mark\\Documents\\HogeSchool\\analyse\Assignments\\PLS\\Loans.json')

jippie = json.load(fr)

data = {
            "ik": "hallo",
            "jij": "hallo"
        }

jippie.append(data)

print(jippie)

fr.close()

fw = open(r'C:\\Users\\mark\\Documents\\HogeSchool\\analyse\Assignments\\PLS\\Loans.json','w')

json.dump(jippie,fw)


