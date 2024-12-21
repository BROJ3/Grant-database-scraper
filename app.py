import sqlite3
import urllib, zipfile, io
import pandas as pd
import requests
import datetime

dt = datetime.datetime.now()

# Download Grants from Grants.Gov
def main():
  r = urllib.request.urlopen(f"https://prod-grants-gov-chatbot.s3.amazonaws.com/extracts/GrantsDBExtract{str(dt.year).zfill(2)}{str(dt.month).zfill(2)}{str(dt.day).zfill(2)}v2.zip")


  with zipfile.ZipFile(io.BytesIO(r.read())) as z:
    with z.open(z.namelist()[0]) as myfile:
      df = pd.read_xml(myfile.read())
      return df

conn = sqlite3.connect('grants.db')

df = main()

df.to_sql('grants', conn, if_exists='replace', index=False)
