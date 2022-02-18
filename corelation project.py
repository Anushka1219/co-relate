import pandas as pd
import plotly.express as px
import csv
import numpy as np

coffee=[]
sleep=[]

with open("marks.csv") as csvfile:
    df=csv.DictReader(csvfile)
    fig=px.scatter(df,x="Marks",y="Days Present",title="Co-Relation")
    print(df)
    fig.show()

    for i in df:
        coffee.append(float(i["Marks"]))
        sleep.append(float(i["Days Present"]))
    datasource={"x":marks,"y":dayspresent}
c=np.corrcoef(datasource["x"],datasource["y"])
print(c)

