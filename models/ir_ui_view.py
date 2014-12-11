# -*- coding: utf-8 -*-
from openerp.models import Model


class View(Model):
    _inherit = 'ir.ui.view'

    def render(self, cr, uid, id_or_xml_id,
               values=None, engine='ir.qweb',
               context=None):
        """
        Override of the render function to make sure
        the website object is available in each template.

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
        if not 'website' in values:
            w_obj = self.pool.get('website')
            if w_obj:
                current_website = w_obj.get_current_website(
                    cr, uid, context=context)
                if current_website:
                    values['website'] = current_website
        return super(View, self).render(cr, uid, id_or_xml_id,
                                        values, engine, context)
