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
from openerp.models import Model


class View(Model):

    """View class."""

    _inherit = 'ir.ui.view'

    def render(self, cr, uid, id_or_xml_id, values=None, engine='ir.qweb', context=None):
        """
        Override of the render function to make sure the website object is available in each
        template.

        :param cr: object
        :param uid: integer
        :param id_or_xml_id: string
        :param values: dictionary
        :param engine: string
        :param context: dictionary
        :return: string
        """
        if values is None:
            values = dict()
        # if no website object is provided it will
        # be added to the values dictionary to ensure the availability
        # of the current website object in all templates
        if 'website' not in values:
            w_obj = self.pool.get('website')
            if w_obj:
                current_website = w_obj.get_current_website(
                    cr, uid, context=context)
                if current_website:
                    values['website'] = current_website
        return super(View, self).render(cr, uid, id_or_xml_id,
                                        values, engine, context)
