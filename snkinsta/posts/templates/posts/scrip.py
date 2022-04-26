# from datetime import date
#
# users = [
#     {
#         'email': 'Dranza@gmail.com',
#         'first_name': 'Carlos',
#         'last_name': 'Parra',
#         'password': 'Dranza997',
#         'is_admin': True
#     },
#     {
#         'email': 'leviAk@gmail.com',
#         'first_name': 'Levi',
#         'last_name': 'Ackerman',
#         'password': 'Lev1854',
#
#
#     },
#     {
#         'email': 'Mikasa@gmail.com',
#         'first_name': 'Mikasa',
#         'last_name': 'Ackerman',
#         'password': 'mikasa854',
#
#     },
#     {
#         'email': 'tatakae@gmail.com',
#         'first_name': 'Eren',
#         'last_name': 'Jaeger',
#         'password': 'tatakae30',
#         'is_admin': True,
#
#
#     }
# ]
#
# from posts.models import User
#
# for user in users:
#     obj = User(**user)
#     obj.save()
#     print(obj.pk, ':', obj.email)