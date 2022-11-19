from fastapi import APIRouter, Depends, HTTPException, status
from services.reviews import get_reviews_service
from schemas.reviews import Review, ReviewInDB
from repository.reviews import ReviewsRepository
from typing import List

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/")
async def get_reviews(
    reviews_service: ReviewsRepository = Depends(get_reviews_service),
):
    return reviews_service.get_all()

@router.get("/{review_id}")
async def get_review(review_id: int, service: ReviewsRepository = Depends(get_reviews_service)):
    review = service.get_review_by_id(review_id)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review

@router.post("/")
async def create_review(review: Review, service: ReviewsRepository = Depends(get_reviews_service)):
    # print("review", review)
    return service.create_review(review)
    # return service.create_review(**review.dict())

@router.put("/{review_id}")
async def update_review(review_id: int, review: Review, service: ReviewsRepository = Depends(get_reviews_service)):
    review = service.update_review(review_id, **review.dict())
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review

@router.delete("/{review_id}", response_model=ReviewInDB)
async def delete_review(review_id: int, service: ReviewsRepository = Depends(get_reviews_service)):
    review = service.delete_review(review_id)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review

@router.get("/charging_point/{charging_point_id}", response_model=List[ReviewInDB])
async def get_reviews_by_charging_point_id(charging_point_id: int, service: ReviewsRepository = Depends(get_reviews_service)):
    return service.get_reviews_by_charging_point_id(charging_point_id)

@router.get("/user/{user_id}", response_model=List[ReviewInDB])
async def get_reviews_by_user_id(user_id: int, service: ReviewsRepository = Depends(get_reviews_service)):
    return service.get_reviews_by_user_id(user_id)

# Path: server/routers/users.py
