
function submitData(event) {
event.preventDefault();
const name = document.getElementById('name').value;
const tel = document.getElementById('tel').value;
const email = document.getElementById('email').value;
const requesttype = document.getElementById('requesttype').value;
const service = document.getElementById('service').value;
const package = document.getElementById('package').value;
const complaint = document.getElementById('complaint').value;
const support = document.getElementById('support').value;
const message = document.getElementById('message').value;

frappe.call({
  method: 'space_secure.www.servicerequest.insert_data',
  args: {
    full_name: name,
    email: email,
    phone: tel,
    type: requesttype,
    srevice_name: service,
    package_name: package,
    complaint_topic: complaint,
    technical_support: support,
    description: message,

  }
  ,
  callback: function(response) {
    Swal.fire({
       position: 'top-end',
        icon: 'success',
        title: 'Thank you for your message',
        showConfirmButton: false,
        timer: 1500
      });
  }
});
}

