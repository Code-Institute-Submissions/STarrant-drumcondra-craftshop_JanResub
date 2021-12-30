/* Code Credit ChrisZ - Boutique Ado Project as per README */


let stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
let client_secret = $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripe_public_key);
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

