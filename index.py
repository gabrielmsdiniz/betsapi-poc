import requests
import json
import csv
import pandas as pd

if __name__ == "__main__":
  ids = []

  for r in results:
    ids.append(r.id)


  print('Reading file...')
  r = requests.get("https://pt.betsapi.com/docs/samples/event_odds.json")
  rJson = r.json()
  print('File read')

  results = rJson['results']
  df = pd.DataFrame.from_dict(results)
  df.to_csv('data/example.csv')
  print('Results Saved')

  df_odds = df['odds']
  df_odds.to_csv('data/odds.csv')
  print('Odds saved')