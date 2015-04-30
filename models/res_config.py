# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.models import TransientModel
from openerp import fields


class WebsiteConfigSettings(TransientModel):

    """Adds the fields for Fontloader."""

    _inherit = 'website.config.settings'

    use_fontloader = fields.Boolean(
        string='Use Fontloader',
        related='website_id.use_fontloader',
        help=('if activated the fonts will be loaded at the end of the page,'
              ' and default front is shown till font is loaded'))
