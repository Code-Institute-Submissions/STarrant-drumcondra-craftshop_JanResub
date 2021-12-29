/* Code Credit ChrisZ - Boutique Ado Project as per README */


var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');

var style = {
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

card.mount('#card-element', {style: style});
