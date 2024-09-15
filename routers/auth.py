from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get("/get_user")
async def get_user():
    return "Hello World!"

