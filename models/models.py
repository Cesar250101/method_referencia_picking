# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Pedidos(models.Model):
    _inherit = 'sale.order'
    
    @api.multi
    def action_confirm(self):
        pedidoinvoice_vals = super(Pedidos, self).action_confirm()
        picking_id=self.env['stock.picking'].search([('sale_id','=',self.id)]).id
        referencias=self.referencia_ids
        for r in referencias:
            vals={
                    "origen": r.folio,
                    "sii_referencia_TpoDocRef": r.sii_referencia_TpoDocRef.id,
                    "motivo": r.motivo,
                    "fecha_documento": r.fecha_documento,
                    "stock_picking_id":picking_id,
                }      
        self.env['stock.picking.referencias'].create(vals)    
                        

