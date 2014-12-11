# -*- coding: utf-8 -*-
from openerp.models import TransientModel
from openerp import fields


class WebsiteConfigSettings(TransientModel):
    _inherit = 'website.config.settings'

    use_fontloader = fields.Boolean(
        string='Use Fontloader',
        related='website_id.use_fontloader',
        help=('if activated the fonts will be loaded at the end of the page,'
              ' and default front is shown till font is loaded'))
