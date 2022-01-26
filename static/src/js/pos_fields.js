odoo.define('pos_customer_restriction.pos_fields', function(require){
"use strict";

    var models = require('point_of_sale.models');
    
    models.load_fields('res.partner', ['available_in_pos']);

    

});
