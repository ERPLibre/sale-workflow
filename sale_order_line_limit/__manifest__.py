# Copyright 2020 MathBenTech <info@mathben.tech>
# License AGPLv3.0 or later (https://www.gnu.org/licenses/agpl-3.0.en.html).

{
    "name": "Sale Order Line Limit",
    "summary": "Add limit to sale.order.line on pages sale.order.line",
    "category": "Sale",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "MathBenTech",
    "website": "https://www.mathben.tech",
    'description': """
Sale Order Line Limit
=====================
Specify the limit on one2many in model sale.order of field order_line.
This will show the pages when more line is added of limit.

""",
    "depends": [
        "sale",
    ],
    "data": [
        "views/sale_order_view.xml"
    ],
    "demo": [],
    "qweb": [],
    "application": False,
}
