from flask import Flask, request, jsonify
from flask.views import MethodView
from datetime import datetime

app = Flask(__name__)

# Список объявлений в качестве временного хранилища
ads = []


def find_ad(ad_id):
    for ad in ads:
        if ad['id'] == ad_id:
            return ad
    return None


class Ads_App(MethodView):

    def get(self, ad_id=None):
        if ad_id is None:
            return jsonify(ads)
        ad = find_ad(ad_id)
        if ad:
            return jsonify(ad)
        return jsonify({'message': 'Объявление не найдено'}), 404

    def post(self):
        data = request.get_json()
        ad = {
            'id': len(ads) + 1,
            'title': data.get('title'),
            'description': data.get('description'),
            'created_at': datetime.now().isoformat(),
            'owner': data.get('owner')
        }
        ads.append(ad)
        return jsonify(ad), 201

    def delete(self, ad_id):
        ad = find_ad(ad_id)
        if ad:
            ads.remove(ad)
            return jsonify({'message': 'Объявление удалено'}), 200
        return jsonify({'message': 'Объявление не найдено'}), 404


# Регистрация маршрутов
ads_view = Ads_App.as_view('ads_app')
app.add_url_rule('/ads', defaults={'ad_id': None}, view_func=ads_view, methods=['GET'])
app.add_url_rule('/ads', view_func=ads_view, methods=['POST'])
app.add_url_rule('/ads/<int:ad_id>', view_func=ads_view, methods=['GET', 'DELETE'])

if __name__ == '__main__':
    app.run()
