import os
import pandas as pd
from sqlalchemy import create_engine


pg_db = os.environ.get('POSTGRES_NAME', default='postgres')
pg_user = os.environ.get('POSTGRES_USER', default='postgres')
pg_pwd = os.environ.get('POSTGRES_PASSWORD', default='postgres')

engine = create_engine(f'postgresql://{pg_user}:{pg_pwd}@db:5432/{pg_db}')

df = pd.read_csv('/code/data_analysis/prepared_data.csv',
                 converters={'genres': pd.eval})


column_labels = {'kinopoiskId': 'kinopoisk_id',
                 'ratingImdb': 'rating_imdb',
                 'filmLength': 'film_length'}

df.rename(columns=column_labels, inplace=True)

columns = ['kinopoisk_id', 'name', 'slogan', 'description', 'genres',
           'rating_imdb', 'year', 'film_length']

df = df[columns]

df_close = pd.read_csv('/code/data_analysis/close_films.csv',
                       converters={'close': pd.eval})

df['close'] = df_close['close']
df.to_sql('tracker_film', engine, if_exists='append', index=False)

print('Таблица tracker_film успешно заполнена!')
