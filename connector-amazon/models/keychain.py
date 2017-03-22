# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class KeychainAccount(models.Model):
    _inherit = 'keychain.account'

    namespace = fields.Selection(selection_add=[('amazon', 'Amazon')])

    def _amazon_validate_data(self, data):
        return True
