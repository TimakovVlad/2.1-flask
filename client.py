import requests

BASE_URL = 'http://127.0.0.1:5000/ads'


def test_create_ad():
    data = {
        'title': 'Продам ноутбук',
        'description': 'Почти новый, отличное состояние',
        'owner': 'Андрей'
    }
    response = requests.post(BASE_URL, json=data)
    print(f'POST: {response.status_code}')
    print('Ответ:', response.json())


def test_get_all_ads():
    response = requests.get(BASE_URL)
    print(f'GET: {response.status_code}')
    print('Ответ:', response.json())


def test_get_ad(ad_id):
    url = f'{BASE_URL}/{ad_id}'
    response = requests.get(url)
    print(f'GET /ads/{ad_id}: {response.status_code}')
    print('Ответ:', response.json())


def test_delete_ad(ad_id):
    url = f'{BASE_URL}/{ad_id}'
    response = requests.delete(url)
    print(f'DELETE /ads/{ad_id}: {response.status_code}')
    print('Ответ:', response.json())


if __name__ == '__main__':
    # 1. Создаем объявление
    test_create_ad()

    # 2. Получаем все объявления
    test_get_all_ads()

    # 3. Получаем конкретное объявление по ID
    test_get_ad(1)

    # 4. Удаляем конкретное объявление по ID
    test_delete_ad(1)

    # 5. Проверяем список объявлений после удаления
    test_get_all_ads()
