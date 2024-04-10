let searchInput=document.querySelector("#search-input")
let searchButton=document.querySelector("#search-button")
let currentUrl=window.location.href
let productsSection1= document.querySelector("#products")

async function SearchProducts(){
    
    let params = new URLSearchParams(document.location.search);
    let searchedData = params.get("search") ? params.get("search") : ""
    let categoryData=params.get("category") ? params.get("category") : ""
    let  color=params.get("color") ? params.get("color") : ""
    let  tag=params.get("tag") ? params.get("tag") : ""
    let  brand=params.get("brand") ? params.get("brand") : ""
    let page=params.get("page") ? params.get("page") : "1"
   
  

    

   
   
    let url=`${location.origin}/api/product/?page=${page}&search=${searchedData}&product__category__title=${categoryData}&color__title=${color}&tags__title=${tag}&product__brand__title=${brand}`
    await fetch(url)
    .then(response=>response.json())
    .then(data=>{
        console.log(data.results[0]);
        let html=""
        for(let i=0;i<data.results.length;i++){
            html+=`
            <div class="col-md-4">
            <div class="item"> 
              <!-- Item img -->
              <div class="item-img"> <img class="img-1" src="${data.results[i].cover_image}" alt="" >
                <!-- Overlay -->
                <div class="overlay">
                  <div class="position-center-center">
                    <div class="inn"><a href="${data.results[i].cover_image}" data-lighter><i class="icon-magnifier"></i></a> <a href="" class="basket-add" data-product="${data.results[i].id}" data-action="add" onclick="${updateUserOrder()}" data-id=${data.results[i].id}><i class="icon-basket"></i></a> 
                    <a href="#." data-product="${data.results[i].id}" data-action="add" class="add-wishlist" onclick="${addToWishlist()}" data-id=${data.results[i].id}><i class="icon-heart"></i></a></div>
                  </div>
                </div>
              </div>
              <!-- Item Name -->
              <div class="item-name"> <a href="/product/product/${data.results[i].slug}">${data.results[i].title}</a>
                <p>${data.results[i].description}</p>
              </div>
              <!-- Price --> 
              <span class="price"><small>$</small>${data.results[i].price}</span> </div>
          </div>`

        }
        productsSection1.innerHTML=html
        
        // <li><a href="#"><i class="fa fa-angle-left"></i></a></li>
        // <li class="active"><a href="#">1</a></li>
        // <li><a href="#">2</a></li>
        // <li><a href="#">3</a></li>
        // <li><a href="#"><i class="fa fa-angle-right"></i></a></li>
      
        function updateUserOrder(productId, action) {
          console.log('User is authenticated, sending data...');
          console.log('productId:', productId, 'Action:', action);
      
          var url = `${location.origin}/api/create_order`;
      
          fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'product_version': productId,"quantity":1})
          })
            .then((response) => {
              if (!response.ok) {
                throw new Error('Network response was not ok');
              }
              return response.json();
            })
            .then((data) => {
              console.log('data:', data);
              getCart()
            });
            
        }
        var updateBtns = document.getElementsByClassName('basket-add');
    for (i = 0; i < updateBtns.length; i++) {
      updateBtns[i].addEventListener('click', function (e) {
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
          updateUserOrder(productId, action);
          console.log("bbbbb");
        }
      });
    }
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
    var wishlistBtns = document.getElementsByClassName('add-wishlist');
for (i = 0; i < wishlistBtns.length; i++) {
  wishlistBtns[i].addEventListener('click', function (e) {
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
}
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
      })
      
}
searchButton.addEventListener("click",(e)=>{
    e.preventDefault()
    let searchInput=document.querySelector("#search-input")
    window.location.replace(
        `${location.origin}/product/product/?search=${searchInput.value}`,
      );
    
    SearchProducts()
 
})
SearchProducts()
