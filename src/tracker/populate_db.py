import os
import pandas as pd
from sqlalchemy import create_engine


pg_db = os.environ.get('POSTGRES_NAME')
pg_user = os.environ.get('POSTGRES_USER')
pg_pwd = os.environ.get('POSTGRES_PASSWORD')

engine = create_engine(f'postgresql://{pg_user}:{pg_pwd}@db:5432/{pg_db}')

df = pd.read_csv('../../data_analysis/prepared_data.csv',
                 converters={'genres': pd.eval})


column_labels = {'kinopoiskId': 'kinopoisk_id',
                 'ratingImdb': 'rating_imdb',
                 'filmLength': 'film_length'}

df.rename(columns=column_labels, inplace=True)

columns = ['kinopoisk_id', 'name', 'slogan', 'description', 'genres',
           'rating_imdb', 'year', 'film_length']

df = df[columns]

df.to_sql('tracker_film', engine, if_exists='replace')
