
async function getCart() {
    let cart=document.getElementById("home-cart")
   
    const url = `${location.origin}/api/create_order`
    await fetch(url)
    .then((response) => {
    if (!response.ok) {
        throw new Error("API request failed.");
    }
    return response.json();
    })
    .then((data) => {

    console.log(data);
    let html=""
    for(let i=0;i<data.length;i++){
      if(data[i]["cart"]["user"] == parseInt(cart.getAttribute("data-id"))){
        html+=`
        <li>
        <div class="media-left">
          <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${data[i]["product_version"]["cover_image"]}" alt="..."> </a> </div>
        </div>
        <div class="media-body">
          <h6 class="media-heading">${data[i]["product_version"]["title"]}</h6>
          <span class="price">${data[i]["product_version"]["price"]} USD</span> <span class="qty">QTY: ${data[i]["quantity"]}</span> </div>
      </li>`

    }
  else{
    html=""
  }}
    cart.innerHTML=html
})}

    getCart()


async function getWishlist() {
  let cart=document.getElementById("home-wishlist")
 
  const url = `${location.origin}/api/wishlists`
  await fetch(url)
  .then((response) => {
  if (!response.ok) {
      throw new Error("API request failed.");
  }
  return response.json();
  })
  .then((data) => {

  console.log(data);
  let html=""
  for(let i=0;i<data.length;i++){
    if(data[i]["user"] == parseInt(cart.getAttribute("data-id"))){
      html+=`
      <li>
      <div class="media-left">
        <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${data[i]["product_version"]["cover_image"]}" alt="..."> </a> </div>
      </div>
      <div class="media-body">
        <h6 class="media-heading">${data[i]["product_version"]["title"]}</h6>
        <span class="price">${data[i]["product_version"]["price"]} USD</span>  </div>
    </li>`

  }}
  cart.innerHTML=html
})}

  getCart()
  getWishlist()