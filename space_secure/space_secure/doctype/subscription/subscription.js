// Copyright (c) 2023, MalekQumboz and contributors
// For license information, please see license.txt

frappe.ui.form.on('Subscription', {
	// refresh: function(frm) {

	// }

	start_date:function(frm){
	frm.trigger("get_total_subscription_days");
	},
	end_date:function(frm){
	frm.trigger("get_total_subscription_days");
	},
	get_total_subscription_days:function(frm){

	frappe.call({
	method:"space_secure.space_secure.doctype.subscription.subscription.get_total_subscription_days",
	args:{
	start_date:frm.doc.start_date,
	end_date:frm.doc.end_date
	},
	callback:(r)=>{
	frm.doc.total_subscription_days=r.message;
	frm.refresh()
	}
	})},
});
