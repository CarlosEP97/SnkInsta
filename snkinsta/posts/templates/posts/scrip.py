from datetime import date

users = [
    {
        'email': 'Dranza@gmail.com',
        'first_name': 'Carlos',
        'last_name': 'Parra',
        'password': 'Dranza997',
        'is_admin': True
    },
    {
        'email': 'leviAk@gmail.com',
        'first_name': 'Levi',
        'last_name': 'Ackerman',
        'password': 'Lev1854',
        'birthdate': date(829, 12,25)

    },
    {
        'email': 'Mikasa@gmail.com',
        'first_name': 'Mikasa',
        'last_name': 'Ackerman',
        'password': 'mikasa854',
        'birthdate': date(845, 2,10)
    },
    {
        'email': 'tatakae@gmail.com',
        'first_name': 'Eren',
        'last_name': 'Jaeger',
        'password': 'tatakae30',
        'is_admin': True,
        'birthdate': date(845, 3, 30),
        'bio': "me llamo eren jaeger,uso el poder del titan fundador para hablar con el pueblo de ymir."

    }
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)