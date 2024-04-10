function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  
  const csrftoken = getCookie('csrftoken');
function updateUserOrder(productId, quantity,action) {
    console.log('User is authenticated, sending data...');
    console.log('productId:', productId, 'Action:', action);

    var url = `${location.origin}/api/create_order`;

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({ 'product_version': productId,"quantity":quantity})
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log('data:', data);
      });
  }
  var updateBtn = document.querySelector("#btn-add");

updateBtn.addEventListener('click', function (e) {
  e.preventDefault()
  var productId = this.dataset.product;
var user=this.dataset.user
var quantity=document.getElementById("qty1").value
  console.log("bbb:",productId,user);
  var action = this.dataset.action;

  console.log('USER:', user);

  if (user == 'AnonymousUser') {
    addCookieItem(productId, action);
    console.log("aaaa");
  } else {
    updateUserOrder(productId,quantity, action);
    console.log("bbbbb");
  }
});

function addToWishlist(productId, action) {
    console.log('User is authenticated, sending data...');
    console.log('productId:', productId, 'Action:', action);

    var url = `${location.origin}/api/wishlists/create/`;

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({ 'product_version': productId})
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log('data:', data);
      });
  }
  var wishlistBtns = document.querySelector('.add-wishlist');
wishlistBtns.addEventListener('click', function (e) {
  e.preventDefault()
  var productId = this.dataset.product;
var user=this.dataset.user
  console.log("bbb:",productId,user);
  var action = this.dataset.action;

  console.log('USER:', user);

  if (user == 'AnonymousUser') {
    addCookieItem(productId, action);
    console.log("aaaa");
  } else {
    addToWishlist(productId, action);
    console.log("bbbbb");
  }
});

function addCookieItem(productId, action) {
    console.log('User is not authenticated');

    if (action == 'add') {
      if (cart[productId] == undefined) {
        cart[productId] = { 'quantity': 1 };

      } else {
        cart[productId]['quantity'] += 1;
      }
    }

    if (action == 'remove') {
      cart[productId]['quantity'] -= 1;

      if (cart[productId]['quantity'] <= 0) {
        console.log('Item should be deleted');
        delete cart[productId];
      }
    }
    console.log('CART:', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
  
  

}