# -*- coding: utf-8 -*-

#
#    odoo extensions
#
#    © 2017-now Josef Kaser (<http://www.pragmasoft.de>).
#
#   See the LICENSE file in the toplevel directory for copyright
#   and license details.
#


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _name = _inherit

    @api.model
    def create(self, vals):
        # partner_type = self._context.get('res_partner_search_mode')

        if not vals.get('parent_id', False):
            partner_reference = self.env['ir.sequence'].next_by_code('partner.reference')
            vals['ref'] = partner_reference

            account_receivable_number = '1' + partner_reference
            account_payable_number = '9' + partner_reference

            account_receivable = self.env['account.account'].create(
                {
                    'code': account_receivable_number,
                    'name': vals['name'],
                    'user_type_id': self.env['account.account.type'].search([('type', '=', 'receivable')]).id,
                    'reconcile': True,
                }
            )

            vals['property_account_receivable_id'] = account_receivable.id

            account_payable = self.env['account.account'].create(
                {
                    'code': account_payable_number,
                    'name': vals['name'],
                    'user_type_id': self.env['account.account.type'].search([('type', '=', 'payable')]).id,
                    'reconcile': True,
                }
            )

            vals['property_account_payable_id'] = account_payable.id

        return super(ResPartner, self).create(vals)
