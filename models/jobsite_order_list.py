from odoo import models, fields, api


class jobsite_order_list(models.Model):
    _inherit = 'jobsite'

    sale_orders = fields.One2many('sale.order', 'jobsite_id', 'Job Orders',domain=['|', ('active', '=', True), ('active', '=', False),('job_order','!=',False)],
        context={'active_test': False} ,readonly=True)

    active_orders = fields.Integer(string='Active Orders',compute='_count_active_orders')
    closed_orders= fields.Integer(string='Closed Orders',compute='_count_closed_orders')

    def _count_active_orders(self):
        self.active_orders = sum(1 for sale_order in self.sale_orders if sale_order.active)

    def _count_closed_orders(self):
        self.closed_orders = sum(1 for sale_order in self.sale_orders if not sale_order.active)

    def calculate_marker_color(jobsite):
        if jobsite.active_orders==0:
            if jobsite.closed_orders==0:
                return 'black'
            elif jobsite.closed_orders>0:
                return 'blue'
        elif jobsite.active_orders>=1 and jobsite.active_orders<=2:
            return 'red'
        elif jobsite.active_orders>=3 and jobsite.active_orders<=5:
            return 'orange'
        elif jobsite.active_orders>=6 and jobsite.active_orders<=15:
            return 'yellow'
        else:
            return 'green'




        #
        # if jobsite.active_orders == 0:
        #     if jobsite.closed_orders == 0:
        #         return 'black'
        #     elif jobsite.closed_orders > 0:
        #         return 'blue'
        # elif 1 <= jobsite.active_orders <= 2:
        #     return 'red'
        # elif 3 <= jobsite.active_orders <= 5:
        #     return 'orange'
        # elif 6 <= jobsite.active_orders <= 15:
        #     return 'yellow'
        # else:
        #     return 'green'





