import csv
import time
from plyer import notification


filename="file.csv" 
columns=[]
rows=[]

with open(filename,'r') as csvfile:
    reader=csv.reader(csvfile)
    print("headers",next(reader))

if __name__ == __name__:
    notification.notify(
        title="  my header",
        message="  my descreaption",
        app_icon="warning",
        timeout=5,

    )   
    time.sleep(7) 
