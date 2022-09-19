import pandas as pd

def get_rec_df(film):
    """
    Recommendation for 1 film
    :param film: int or str - kinopoiskId
    :return: df (kinopoiskId, ratingImdb)
    """
    matrix = pd.read_csv("matrix_ids.csv")
    prepared_data = pd.read_csv('prepared_data.csv')
    matrix = matrix.query(f"kinopoiskId!={film}")
    matrix = matrix.join(prepared_data["ratingImdb"])
    sorted_films = matrix.sort_values([f"{film}", "ratingImdb"], ascending = False)
    rec = sorted_films[["kinopoiskId", "ratingImdb"]].head()
    return rec


def get_personal_rec(five_best):
    """
    Recommendation for five "best" user's movies
    :param five_best: list of ints or strings
    :return: df (kinopoiskId, ratingImdb)
    """
    close_films = pd.DataFrame({"kinopoiskId": [], "ratingImdb": []})
    for film in five_best:
        five_recs = get_rec_df(f"{film}")
        close_films = close_films.append(five_recs)
    rec = close_films.sort_values(["ratingImdb"], ascending = False).head()
    return rec


def get_popular():
    """
    If it's not enough films to make a recommendation by them
    :return: df (kinopoiskId, ratingImdb)
    """
    prepared_data = pd.read_csv('prepared_data.csv')
    rec = prepared_data.sort_values(["ratingImdb"], ascending=False).head()
    return rec