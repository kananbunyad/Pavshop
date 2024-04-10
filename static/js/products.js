let productsSection= document.querySelector("#products")
let colorsSection= document.querySelector("#colors")
let categorySection=document.querySelector("#categories")
let tagSection=document.querySelector("#tags")
let brandSection=document.querySelector("#brands")
const clearBtn=document.getElementById("clear")
let paginationSection = document.getElementById("pagination")

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
// async function fetchProducts() {

//     const url = `${location.origin}/api/product`
//     await fetch(url)
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("API request failed.");
//         }
//         return response.json();
//       })
//       .then((data) => {
//         console.log(data);
//         let html=""
//         for(let i=0;i<data.length;i++){
//             html+=`
//             <div class="col-md-4">
//                 <div class="item"> 
//                   <!-- Item img -->
//                   <div class="item-img"> <img class="img-1" src="${data[i].cover_image}" alt="" >
//                     <!-- Overlay -->
//                     <div class="overlay">
//                       <div class="position-center-center">
//                         <div class="inn"><a href="${data[i].cover_image}" data-lighter><i class="icon-magnifier"></i></a> <a href="" class="basket-add" data-product="${data[i].id}" data-action="add" onclick="${updateUserOrder()}" data-id=${data[i].id}><i class="icon-basket"></i></a> 
//                         <a href="#." data-product="${data[i].id}" data-action="add" class="add-wishlist" onclick="${addToWishlist()}" data-id=${data[i].id}><i class="icon-heart"></i></a></div>
//                       </div>
//                     </div>
//                   </div>
//                   <!-- Item Name -->
//                   <div class="item-name"> <a href="/product/product/${data[i].slug}">${data[i].title}</a>
//                     <p>${data[i].description}</p>
//                   </div>
//                   <!-- Price --> 
//                   <span class="price"><small>$</small>${data[i].price}</span> </div>
//               </div>`

//         }
//         productsSection.innerHTML=html
//         function updateUserOrder(productId, action) {
//           console.log('User is authenticated, sending data...');
//           console.log('productId:', productId, 'Action:', action);
      
//           var url = `${location.origin}/api/create_order`;
      
//           fetch(url, {
//             method: 'POST',
//             headers: {
//               'Content-Type': 'application/json',
//               'X-CSRFToken': csrftoken,
//             },
//             body: JSON.stringify({ 'product_version': productId,"quantity":1})
//           })
//             .then((response) => {
//               if (!response.ok) {
//                 throw new Error('Network response was not ok');
//               }
//               return response.json();
//             })
//             .then((data) => {
//               console.log('data:', data);
//             });
//         }
//         var updateBtns = document.getElementsByClassName('basket-add');
//     for (i = 0; i < updateBtns.length; i++) {
//       updateBtns[i].addEventListener('click', function (e) {
//         e.preventDefault()
//         var productId = this.dataset.product;
//       var user=this.dataset.user
//         console.log("bbb:",productId,user);
//         var action = this.dataset.action;
  
//         console.log('USER:', user);
  
//         if (user == 'AnonymousUser') {
//           addCookieItem(productId, action);
//           console.log("aaaa");
//         } else {
//           updateUserOrder(productId, action);
//           console.log("bbbbb");
//         }
//       });
//     }
//     function addToWishlist(productId, action) {
//       console.log('User is authenticated, sending data...');
//       console.log('productId:', productId, 'Action:', action);
  
//       var url = `${location.origin}/api/wishlists/create/`;
  
//       fetch(url, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//           'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({ 'product_version': productId})
//       })
//         .then((response) => {
//           if (!response.ok) {
//             throw new Error('Network response was not ok');
//           }
//           return response.json();
//         })
//         .then((data) => {
//           console.log('data:', data);
//         });
//     }
//     var wishlistBtns = document.getElementsByClassName('add-wishlist');
// for (i = 0; i < wishlistBtns.length; i++) {
//   wishlistBtns[i].addEventListener('click', function (e) {
//     e.preventDefault()
//     var productId = this.dataset.product;
//   var user=this.dataset.user
//     console.log("bbb:",productId,user);
//     var action = this.dataset.action;

//     console.log('USER:', user);

//     if (user == 'AnonymousUser') {
//       addCookieItem(productId, action);
//       console.log("aaaa");
//     } else {
//       addToWishlist(productId, action);
//       console.log("bbbbb");
//     }
//   });
// }
//     function addCookieItem(productId, action) {
//       console.log('User is not authenticated');
  
//       if (action == 'add') {
//         if (cart[productId] == undefined) {
//           cart[productId] = { 'quantity': 1 };
  
//         } else {
//           cart[productId]['quantity'] += 1;
//         }
//       }
  
//       if (action == 'remove') {
//         cart[productId]['quantity'] -= 1;
  
//         if (cart[productId]['quantity'] <= 0) {
//           console.log('Item should be deleted');
//           delete cart[productId];
//         }
//       }
//       console.log('CART:', cart);
//       document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
    
    

//   }
//       })
//       .catch((error) => {
//         console.error("An error occurred during the API request:", error.message);
//       });
//   }

async function fetchColors(){
  const url=`${location.origin}/api/color`
  await fetch(url)
  .then((response)=>{
    return response.json()
  }).then((data)=>{
    let html=""
    for(let i=0;i<data.length;i++){
      html+=`
      <li class="color-product" data-id=${data[i].title}><span style="background:${data[i].hex_code};"></span></li>
      `
    }
    colorsSection.innerHTML=html

  })

  let color=document.getElementsByClassName("color-product")
  for(let i=0;i<color.length;i++){
    color[i].addEventListener("click",()=>{
      FilterByColor(color[i].getAttribute("data-id"))
    })
  }
}

   function FilterByColor(color) {
    var url = new URL(location.origin);
      
    const currentUrl = new URL(window.location.href);
    const searchParams = currentUrl.searchParams;

// Set or update the query parameter
searchParams.delete("page")
searchParams.set('color', color);

// Update the browser's URL without reloading the page
history.pushState(null, '', currentUrl.toString());

SearchProducts()

   
  }


  async function fetchTags(){
    const url=`${location.origin}/api/tag`
    console.log(url);
    await fetch(url)
    .then((response)=>{
      return response.json()
    }).then((data)=>{
      console.log(data);
      let html=""
      for(let i=0;i<data.length;i++){
        html+=`
        <li><a href="" class="tag-product" data-id=${data[i].title}>${data[i].title}</a></li>
        `
      }
      tagSection.innerHTML=html
  
    })
  
    let tag=document.getElementsByClassName("tag-product")
    for(let i=0;i<tag.length;i++){
      tag[i].addEventListener("click",(e)=>{
        e.preventDefault()
        FilterByTag(tag[i].getAttribute("data-id"))
      })
    }
  }
  
     function FilterByTag(tag) {
  
      var url = new URL(location.origin);
      
    const currentUrl = new URL(window.location.href);
    const searchParams = currentUrl.searchParams;

// Set or update the query parameter
searchParams.delete("page")
searchParams.set('tag', tag);

// Update the browser's URL without reloading the page
history.pushState(null, '', currentUrl.toString());

   SearchProducts()
    }
  
   
  
  async function fetchCategory(){
    const url=`${location.origin}/api/category`
    await fetch(url)
    .then((response)=>{
      return response.json()
    }).then((data)=>{
      let html=""
      for(let i=0;i<data.length;i++){
        html+=`
        <li><a href="#." class="category-product" data-title=${data[i].title}> ${data[i].title} <span>24</span></a></li>
        `
      }
      html+=`
      <li><a href="#." class="category-product" data-title="all"> all</a></li>
      `
      categorySection.innerHTML=html
  
    })
  
    let category=document.getElementsByClassName("category-product")
    for(let i=0;i<category.length;i++){
      category[i].addEventListener("click",(e)=>{
        e.preventDefault()
        FilterByCategory(category[i].getAttribute("data-title"))
      })
    }
  }
  function FilterByCategory(category) {
    if (category!=="all"){
      var url = new URL(location.origin);
      
      const currentUrl = new URL(window.location.href);
      const searchParams = currentUrl.searchParams;

// Set or update the query parameter
searchParams.delete("page")
searchParams.set('category', category);

// Update the browser's URL without reloading the page
history.pushState(null, '', currentUrl.toString());
      
        

    }
  else{
    var url = new URL(location.origin);
      
    const currentUrl = new URL(window.location.href);
    const searchParams = currentUrl.searchParams;

// Set or update the query parameter
searchParams.delete('category');

// Update the browser's URL without reloading the page
history.pushState(null, '', currentUrl.toString());
  }

    
  
   

// Access the query string parameters


    
    
    SearchProducts()
   
  }


  async function fetchBrand(){
    const url=`${location.origin}/api/brand`
    await fetch(url)
    .then((response)=>{
      return response.json()
    }).then((data)=>{
      let html=""
      for(let i=0;i<data.length;i++){
        html+=`
        <li><a href="#." class="brand-product" data-title=${data[i].title}> ${data[i].title} <span>24</span></a></li>
        `
      }
      brandSection.innerHTML=html
  
    })
  
    let brand=document.getElementsByClassName("brand-product")
    for(let i=0;i<brand.length;i++){
      brand[i].addEventListener("click",(e)=>{
        e.preventDefault()
        FilterByBrand(brand[i].getAttribute("data-title"))
      })
    }
  }
  function FilterByBrand(brand) {
    var url = new URL(location.origin);
      
    const currentUrl = new URL(window.location.href);
    const searchParams = currentUrl.searchParams;

// Set or update the query parameter
searchParams.delete("page")
searchParams.set('brand',brand);

// Update the browser's URL without reloading the page
history.pushState(null, '', currentUrl.toString());
SearchProducts()
  
  
  }

  // function changePage(direction){
  //   SearchProducts(direction)
  // }
  // let htmll=''
  
  // let pages=document.getElementsByClassName("page-number")
  // console.log(pages);
  // for(let i=0;i<pages.length;i++){
  //   pages[i].addEventListener("click",(e)=>{
      
  //     e.preventDefault()
  //     changePage(pages[i].getAttribute("value"))
  //   })
  // }
  // paginationSection.innerHTML=htmll
  async function fetchPageNumber(){
    const url=`${location.origin}/api/product`
    await fetch(url)
    .then((response)=>{
      return response.json()
    }).then((data)=>{
      console.log(data);
      let htmll=""
      for(let i=1;i<=data.total;i++){
        htmll+=`
        <li><a href="" class="page-number" data-value="${i}">${i}</a></li>
        `
      }
      paginationSection.innerHTML=htmll
    })
    let pageNumber=document.getElementsByClassName("page-number")
    for(let i=0;i<pageNumber.length;i++){
      pageNumber[i].addEventListener("click",(e)=>{
        e.preventDefault()
       
        changePage(pageNumber[i].getAttribute("data-value"))
      })
    }
  }


  function changePage(page) {
    var url = new URL(location.origin);
      
    const currentUrl = new URL(window.location.href);
    const searchParams = currentUrl.searchParams;

// Set or update the query parameter
searchParams.set('page',page);

// Update the browser's URL without reloading the page
history.pushState(null, '', currentUrl.toString());
SearchProducts()
  
  
  }
clearBtn.addEventListener("click",ClearAllFilters)
function ClearAllFilters() {
    const currentUrl = new URL(window.location.href);
    const searchParams = currentUrl.searchParams;

    searchParams.delete('category');
    searchParams.delete('brand');
    searchParams.delete('color');
    searchParams.delete('tag');

    history.pushState(null, '', currentUrl.toString());
    SearchProducts(); // Assuming this function refreshes the content based on filters
}



fetchColors()
fetchBrand()
fetchTags()
fetchCategory()
fetchPageNumber()
 

  // fetchProducts()