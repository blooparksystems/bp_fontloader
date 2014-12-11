# -*- coding: utf-8 -*-
{
    'name': "bp_8_0_fontloader",

    'summary': """
    Provide Fontloader for the Themes""",

    'description': """
    Provide Fontloader for the Themes""",

    'author': "BLOOPARK SYSTEMS GMBH. & CO. KG",
    'website': "http://www.bloopark.de",

    'category': 'theme',
    'version': '0.1',


    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'website'
    ],

    # always loaded
    'data': [
        'views/res_config.xml',
        'views/themes.xml'
    ],
}