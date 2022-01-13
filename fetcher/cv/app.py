import requests
from lxml import html
from googletrans import Translator
from datetime import date
import json
# Fetch CV from Xing

translator = Translator()
resp = requests.get("https://www.xing.com/profile/Sven_Nolting3", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

json_data = resp.text.split("APOLLO_STATE=")[1].split(";")[0]
resp_data = json.loads(json_data)

listelements = []

i = 0
while (True):
    try:
        listelements.append(resp_data['ROOT_QUERY']['$ROOT_QUERY.profileWorkExperience({"profileId":"Sven_Nolting3"}).collection.'+str(i)])
    except:
        break
    i += 1

elements = []

print(listelements)
print("::group::Elemente")
for l in listelements:
    print(l)
    title = translator.translate(l["jobTitle"]).text
    elements.append(f"- {l['localizedTimeString']} - {title} ({l['companyName']})")
print("::endgroup::")
today = date.today()
born = date.fromisoformat("2000-07-13")
with open("../../README.md", "r") as f:
    readme = f.read()
    readme = readme.replace("cv_replace_var", '\n'.join(elements))
    readme = readme.replace("age_years", str(today.year - born.year - ((today.month, today.day) < (born.month, born.day))))

with open("../../README.md", "w") as f:
    f.write(readme)
