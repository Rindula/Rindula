import requests
from lxml import html
from googletrans import Translator
from datetime import date
import json
# Fetch CV from Xing

translator = Translator()
resp = requests.get("https://www.xing.com/profile/Sven_Nolting3")

json_data = resp.text.split("APOLLO_STATE=")[1].split(";")[0]
resp_data = json.loads(json_data)

listelements = []

i = 0
while (True):
    try:
        listelements.append(resp_data['ROOT_QUERY']['$ROOT_QUERY.profileWorkExperience({"profileId":"Sven_Nolting3"}).collection.'.i])
    except:
        break
    i += 1

elements = []

for l in listelements:
    title = translator.translate(l["jobTitle"]).text
    elements.append(f"- {l['localizedTimeString']} - {title} ({l['companyName']})")

today = date.today()
born = date.fromisoformat("2000-07-13")
with open("../../README.md", "r") as f:
    readme = f.read()
    readme = readme.replace("cv_replace_var", '\n'.join(elements))
    readme = readme.replace("age_years", str(today.year - born.year - ((today.month, today.day) < (born.month, born.day))))

with open("../../README.md", "w") as f:
    f.write(readme)
