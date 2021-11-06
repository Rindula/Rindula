import requests
from lxml import html
from googletrans import Translator
from datetime import date
# Fetch CV from Xing

translator = Translator()
resp = requests.get("https://www.xing.com/profile/Sven_Nolting3")

tree = html.fromstring(resp.content)
cvi = tree.xpath("/html/body/div[1]/div[2]/div/div[2]/section/div/main/div/div/div[2]/div/div/div[2]/div[2]/ul")

listelements = cvi[0].getchildren()

elements = []

for l in listelements:
    title = translator.translate(l.xpath(".//h4/text()")[0]).text
    ps = l.xpath(".//p/descendant-or-self::*/text()")
    employer = ps[-1]
    timespan = translator.translate(''.join(ps[0:-1])).text
    elements.append(f"- {timespan} - {title} ({employer})")

with open("../../README.md", "r") as f:
    readme = f.read()

today = date.today()
born = datetime.date(2000,7,13)

readme = readme.replace("cv_replace_var", '\n'.join(elements))
readme = readme.replace("age_years", today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

with open("../../README.md", "w") as f:
    f.write(readme)
