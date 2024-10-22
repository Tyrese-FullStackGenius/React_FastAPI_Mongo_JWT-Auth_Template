from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import user_routes


app = FastAPI()

# Add CORS middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the route from user_routes with a prefix
app.include_router(user_routes.router, prefix="/api")


@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Start the application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
