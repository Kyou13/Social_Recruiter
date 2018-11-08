# cat lang.json | jq '.ML'
import numpy as np
from db import psql_save
import csv
import re
import json
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def print_cmx(y_true, y_pred):
    labels = sorted(list(set(y_true)))
    cmx_data = confusion_matrix(y_true, y_pred, labels=labels)

    df_cmx = pd.DataFrame(cmx_data, index=labels, columns=labels)

    plt.figure(figsize = (10,7))
    sn.heatmap(df_cmx, annot=True)
    plt.show()

def cos_sim(v1, v2):
    res = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    if np.isnan(res):
      return 0
    else:
      return res

# DBから取得
db = psql_save()
rows = db.select_description_all()

with open("lang.json","rb") as f:
  lang_list = json.load(f)

# 正規表現の文字列作成
langnames = ["id"]
lang_regexes = []
for lang in lang_list:
  lang_regex = '|'.join(lang_list[lang])
  lang_regexes.append(lang_regex)
  langnames.append(lang) 

data = []
for row in rows:
  tmp = [row[0]]
  # tmp = []
  for lang in lang_regexes:
    count = len(re.findall(lang, row[1], re.IGNORECASE))
    # Numpy.whereで一括処理したほうが早い？
    if count > 0:
      tmp.append(1)
    else:
      tmp.append(0)
  data.append(tmp)

data = np.array(data)
# csvで保存
df = pd.DataFrame(data,columns=langnames).set_index("id")
df.to_csv("skills.csv")

sim = []
# numpy使った積計算
for (c,i) in enumerate(data[:,1:][:100]):
  tmp = []
  tmp.extend(np.zeros(c))
  for j in data[:,1:][c:100]:
    tmp.append(cos_sim(i,j))
  sim.append(tmp)
sim = np.array(sim)
sim = np.hstack((data[:,0][:100][:,None],sim))
df = pd.DataFrame(sim,columns=np.append(["id"],data[:,0][:100])).set_index("id")
df.to_csv("sim.csv")
