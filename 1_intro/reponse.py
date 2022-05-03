"""
    Premier exemple de programme qui permet d'apprendre en cas d'absence de reponse
"""

print("Bonjour")

reponse = {"ca va ?" : "Bien et toi ?"}

question = input()

while question != "Au revoir":
    if question in reponse:
        print(reponse[question])
    else:
        print("Je ne sais pas comment réagir, quelle serait une bonne reponse ?")
        reponse[question] = input()
        print("Merci, je m'en souviendrai et maintenant ?")
    question = input()

print("Au revoir")