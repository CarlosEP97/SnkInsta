
"""Posts views."""
# Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime


posts = [
    {
        'title': 'declaration of war',
        'user': {
            'name': 'Eren Jaeger',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://animenewsandfacts.com/wp-content/uploads/2020/12/Attack-On-Titan-Season-4-Episode-5-Countdown.jpg',
    },
    {
        'title': 'sea ',
        'user': {
            'name': 'Mikasa Akerman',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://www.tonica.la/__export/1620830185141/sites/debate/img/2021/05/12/mikasa-ackerman-se-quedx-con-jean.jpg_1902800913.jpg',
    },
    {
        'title': 'beaten the beast ',
        'user': {
            'name': 'Levi Akerman',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EceJXtZWsAAHRsm.jpg',
    }
]


def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})