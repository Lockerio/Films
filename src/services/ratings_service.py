from src.serializers.ratings_serializer import RatingSerializer


class RatingService:
    def __init__(self, serializer: RatingSerializer):
        self.serializer = serializer

    def get_one(self, film_id, user_id):
        return self.serializer.get_one(film_id, user_id)

    def get_all(self):
        return self.serializer.get_all()

    def update(self, data):
        return self.serializer.update(data)

    def create(self, data):
        return self.serializer.create(data)

    def delete(self, film_id, user_id):
        self.serializer.delete(film_id, user_id)
