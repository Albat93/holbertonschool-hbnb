from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        try:
            data = request.json
            review_obj = facade.create_review(data)
            return {
                "id": review_obj.id,
                "text": review_obj.text,
                "rating": review_obj.rating,
                "user_id": review_obj.user.id,
                "place_id": review_obj.place.id
            }, 201
        except Exception as e:
            return {'message': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.user.id,
                "place_id": r.place.id
            }
            for r in reviews
        ], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review_obj = facade.get_review(review_id)
        if review_obj:
            return {
                "id": review_obj.id,
                "text": review_obj.text,
                "rating": review_obj.rating,
                "user_id": review_obj.user.id,
                "place_id": review_obj.place.id
            }, 200
        return {'message': 'Review not found'}, 404

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        try:
            data = request.json
            review_obj = facade.update_review(review_id, data)
            if review_obj:
                return {
                    "id": review_obj.id,
                    "text": review_obj.text,
                    "rating": review_obj.rating,
                    "user_id": review_obj.user.id,
                    "place_id": review_obj.place.id
                }, 200
            else:
                return {'message': 'Review not found'}, 404
        except Exception as e:
            return {'message': str(e)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        review_obj = facade.delete_review(review_id)
        if review_obj:
            return {'message': 'Review deleted successfully'}, 200
        return {'message': 'Review not found'}, 404


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""

        reviews = facade.get_reviews_by_place(place_id)

        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.user.id,
                "place_id": r.place.id
            }
            for r in reviews
        ], 200
