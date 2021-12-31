/* Code Credit ChrisZ - Boutique Ado Project as per README */


let stripePublicKey = $('#id_stripe_public_key').text().slice(1,-1);
let clientSecret = $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: "#000",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#32325d"
        }
        },
        invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#dc3545", /* Bootstrap Danger Class */
        iconColor: "#dc3545" /* Bootstrap Danger Class */
        }
    };
let card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle Stripe card errors.
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let errorText = event.error.message;
        let html = `
            <span class="icon" role="alert">
                <i class="bi bi-x-circle-fill dc-stripe-error">
            </i></span>
            <span class="dc-stripe-error"> ${errorText}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
})

// Stripe payment elements

const options = {
    clientSecret: clientSecret,
    // Fully customizable with appearance API.
    appearance: {/*...*/},
  };
  
  // Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in step 2
  const elements = stripe.elements(options);
  
  // Create and mount the Payment Element
  const paymentElement = elements.create('payment');
  paymentElement.mount('#payment-element');

// Handle form submission

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});