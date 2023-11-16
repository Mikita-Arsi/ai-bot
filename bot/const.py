from bot.models import Channel, Admin
from config import is_deploy


if is_deploy:
    channels: list[Channel] = [Channel(**{
        'id': -1001985843105,
        'prefix': 'pro_ai_novosti',
        'name': 'Мир нейросетей'
    })]
    pre_study_channel: Channel = Channel(**{
        'id': -1001822889279,
        'prefix': '',
        'name': 'Предобучение (ChatGPT, школа PROдвижение)'
    })
    pre_study_forum_id = -1001826068841
else:
    channels: list[Channel] = [Channel(**{
        'id': -1001927817429,
        'prefix': 't4iu3gi3',
        'name': 'Мир нейросетей'
    })]
    pre_study_channel: Channel = Channel(**{
        'id': -1001883793721,
        'prefix': '',
        'name': 'Предобучение (ChatGPT, школа PROдвижение)'
    })
    pre_study_forum_id = -1001867770278

admins: list[Admin] = [
    Admin(**{
        'id': 6051606294,
        'prefix': '',
        'first_name': 'Mikita',
        'last_name': None
    }),
    Admin(**{
        'id': 524316284,
        'prefix': 'glebqq',
        'first_name': 'Gleb',
        'last_name': 'Korobeinikov'
    }),
    Admin(**{
        'id': 5115501469,
        'prefix': '',
        'first_name': 'M',
        'last_name': None
    }),
    Admin(**{
        'id': 1308143259,
        'prefix': '',
        'first_name': 'K',
        'last_name': None
    })
    ]
