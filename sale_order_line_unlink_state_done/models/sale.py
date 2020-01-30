# Copyright 2020 MathBenTech <info@mathben.tech>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def unlink(self):
        # Force another state before be deleted
        self.state = "cancel"
        return super(SaleOrderLine, self).unlink()
