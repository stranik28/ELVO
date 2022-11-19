from models.reviews import Reviews
from repository.base import BaseRepository

class ReviewsRepository(BaseRepository):
    def get_reviews_by_charging_point_id(self, charging_point_id):
        return self.session.query(Reviews).filter_by(charging_point_id=charging_point_id).all()

    def get_reviews_by_user_id(self, user_id):
        return self.session.query(Reviews).filter_by(user_id=user_id).all()

    def get_review_by_id(self, review_id):
        return self.session.query(Reviews).filter_by(id=review_id).first()

    def create_review(self, review):
        review = Reviews(**review.dict())
        print("review", review)
        self.session.add(review)
        self.session.commit()
        return "Ok"

    def update_review(self, review_id, body, stars):
        review = self.get_review_by_id(review_id)
        review.body = body
        review.stars = stars
        self.session.commit()
        return review

    def delete_review(self, review_id):
        review = self.get_review_by_id(review_id)
        self.session.delete(review)
        self.session.commit()
        return review

    def get_all(self):
        return self.session.query(Reviews).all()