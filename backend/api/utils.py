import aiohttp


# Сервис сокращения ссылок
endpoint = "https://clck.ru/--"


# Сокращение новой ссылки
async def make_short(new_url):
    async with aiohttp.ClientSession() as session:
        url = (new_url, "?utm_source=sender")
        async with session.get(endpoint, params={"url": url}) as response:
            data = await response.text()
            return data
