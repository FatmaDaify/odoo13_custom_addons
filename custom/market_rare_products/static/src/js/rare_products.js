odoo.define('market_rare_products.market_rare_products', function (require) {
"use strict";
var core = require('web.core');
var screens = require('point_of_sale.screens');
var models = require('point_of_sale.models');
var _t = core._t;
models.load_fields('product.product', ['rare_list','max_allowed_order_qty']);

var RareProductsButton = screens.ActionButtonWidget.extend({
    template: 'RareProductsButton',
    button_click: function(){
        var self = this;
        this.gui.show_popup('confirm',{
            'title': _t('Please Confirm'),
            'body': _t('Do you want to add these items to rare list'),
            'confirm': function() {
                self.add_items_to_rare_list();
            },
        });
    },
    add_items_to_rare_list: function() {
        var order    = this.pos.get_order();
        var lines    = order.get_orderlines();
        for (var i = 0; i < lines.length; i++) {
            var product  =  lines[i].get_product()
            product.rare_list = true;
            console.log("after",product);
         }
    },

});

screens.define_action_button({
    'name': 'Rare List',
    'widget': RareProductsButton,
});

return {
    RareProductsButton: RareProductsButton,
}

});
