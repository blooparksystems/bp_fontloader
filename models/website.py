# -*- coding: utf-8 -*-
from openerp.models import Model
from openerp import fields


class Website(Model):
    _inherit = 'website'

    use_fontloader = fields.Boolean(
        string='Use Fontloader',
        default=True,
        help=('if activated the fonts will be loaded at the end of the page,'
              ' and default front is shown till font is loaded'))
