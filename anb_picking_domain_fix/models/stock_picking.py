# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api

import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.onchange('picking_type_code')
    def onchange_picking_type_code(self):
        if self.picking_type_code in ['incoming', 'outgoing']:
            return {
                'domain': {
                    'partner_id': [
                        '|', ('parent_id', '=', False),
                        ('type', '=', 'delivery'),
                    ],
                }
            }
        else:
            return {
                'domain': {
                    'partner_id': [
                        '|',  ('id', '=', self.company_id.id),
                        '&', ('parent_id', '=', self.company_id.id),
                        ('type', '=', 'delivery'),
                    ],
                }
            }
