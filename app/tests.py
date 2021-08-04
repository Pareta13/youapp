
from youtubesearchpython.__future__ import *
import asyncio


async def main():
    channelsSearch = ChannelsSearch('online sale kese kare', limit=10, language='en', region='US')
    channelsResult = await channelsSearch.next()
    print(channelsResult)

if __name__ == '__main__':
    asyncio.run(main())