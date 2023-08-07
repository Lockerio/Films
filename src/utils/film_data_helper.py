import math


class FilmDataHelper:
    @staticmethod
    def format_films(films):
        formatted_films = []
        for film in films:
            current_id = film.id
            current_title = film.title
            current_genre = film.genre

            ratings = film.ratings
            ratings_amount = len(ratings)

            if ratings_amount == 0:
                current_rating = 0
            else:
                ratings_sum = 0
                for rating in ratings:
                    ratings_sum += rating.rating

                current_rating = math.ceil(ratings_sum / ratings_amount)

            formatted_films.append({
                "id": current_id,
                "title": current_title,
                "genre": current_genre,
                "rating": current_rating
            })

        return formatted_films
