from datetime import datetime


def predict_tag(tags):
    # TODO: lamnguyen
    ids = [1, 2, 3, 4]
    return [f'test {datetime.now()}', f'test {datetime.now()}', f'test {datetime.now()}']


def user_history(user_id):
    # TODO: lamnguyen

    return [
        {
            'id': 1,
            'name': 'Lam Nguyen',
            'url': 'google.com',
            'tags': ['ab', 'cd'],
            'des': 'Nguyen Vu Son Lam'
        },
        {
            'id': 2,
            'name': 'Nam Nguyen',
            'url': 'facebook.com',
            'tags': ['xxx', 'xyyy'],
            'des': 'Nguyen Dnah Nam'
        },]
