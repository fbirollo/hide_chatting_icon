# -*- coding: utf-8 -*-
{
    'name': "Hide Chatting Icon",
    'license': 'AGPL-3',
    'summary': """Hide icon chatting from header""",
    'description': """
        Hide icon Chatting from header
    """,
    'version': "18.0",
    'author': "Fernando Birollo",
    'support': 'fbirollo@gmail.com',
    'images': ['static/description/icon.png'],
    'category': 'tools',
    'depends': ['base'],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
            'hide_chatting_icon/static/src/css/hide_chatting_icon.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
