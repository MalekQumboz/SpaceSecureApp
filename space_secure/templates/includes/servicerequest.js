
function submitData(event) {
event.preventDefault();
const name = document.getElementById('name').value;
const tel = document.getElementById('tel').value;
const email = document.getElementById('email').value;
const subject = document.getElementById('subject').value;
const message = document.getElementById('message').value;
frappe.call({
  method: 'space_secure.www.index.insert_data',
  args: {
    full_name: name,
    email: email,
    phone: tel,
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

