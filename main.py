from bs4 import BeautifulSoup
import pandas as pd

file = open("DLTINS_20210118_01of01.xml", "r")
contents = file.read()

soup = BeautifulSoup(contents, "xml")

get_FinAttrbts = soup.find_all("FinInstrmGnlAttrbts")

ID_TEXT = []
fullNm = []
clssfctnTp = []
cmmdtyDerivInd = []
ntnlCcy = []
issr = []

ID_id = soup.find_all("Id")

for FinInstrmGnlAttrbts in get_FinAttrbts:

    for Id in FinInstrmGnlAttrbts:
        ID_TEXT.append(Id.text)
#
    for FullNm in FinInstrmGnlAttrbts:
        fullNm.append(FullNm.text)

    for ClssfctnTp in FinInstrmGnlAttrbts:
        clssfctnTp.append(ClssfctnTp.text)

    for CmmdtyDerivInd in FinInstrmGnlAttrbts:
        cmmdtyDerivInd.append(CmmdtyDerivInd.text)

    for NtnlCcy in FinInstrmGnlAttrbts:
        ntnlCcy.append(NtnlCcy.text)

    for Issr in FinInstrmGnlAttrbts:
        issr.append(Issr.text)


data = {
    "FinInstrmGnlAttrbts.Id": ID_TEXT,
    "FinInstrmGnlAttrbts.FullNm": fullNm,
    "FinInstrmGnlAttrbts.ClsstnTp": clssfctnTp,
    "FinInstrmGnlAttrbts.CmmdtyDerivInd": cmmdtyDerivInd,
    "FinInstrmGnlAttrbts.NtnlCcy": ntnlCcy,
    "Issr": issr,
    }

df = pd.DataFrame(data)

df.to_csv("Data.csv", index=False, mode="a")
