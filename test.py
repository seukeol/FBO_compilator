import json
from aiohttp import ClientSession
import asyncio



CLIENT_ID = '515789'
API_TOKEN = '630fcb0a-dc1c-42a9-8c63-62f33df702f3'
HEADERS = {
    "Client-Id": CLIENT_ID,
    "Api-Key": API_TOKEN,
    "Content-Type": "application/json"
}


async def main():

    async with ClientSession() as session:

        dataaa = {
            "cluster_ids": [],
            "cluster_type": "CLUSTER_TYPE_OZON"
        }

        async with session.post('https://api-seller.ozon.ru/v1/cluster/list', data=json.dumps(dataaa),headers=HEADERS) as response:
            print("Status:", response.status)
            resp_json = await response.json()
            print(resp_json)
            names = {}
            resp_json_notrash = resp_json['clusters'][0]['logistic_clusters'][0]['warehouses']




asyncio.run(main())
