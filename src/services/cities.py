from typing import Dict, List

from src.models import get_cities_data


async def get_cities() -> List[Dict]:
    return await get_cities_data()
