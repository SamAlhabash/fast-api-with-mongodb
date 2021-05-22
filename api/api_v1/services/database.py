from motor.motor_asyncio import AsyncIOMotorClient
from config.config import settings

db_client: AsyncIOMotorClient = None


async def get_db() -> AsyncIOMotorClient:
    """Return database client instance."""
    global db_client
    return db_client[settings.DB_NAME]


async def connect_db():
    """Create database connection."""
    global db_client
    db_client = AsyncIOMotorClient(settings.MONGO_URL)


async def close_db():
    """Close database connection."""
    global db_client
    db_client.close()
