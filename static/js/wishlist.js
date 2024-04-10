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

let cartsss=document.getElementById("cart-inner")
let btn=document.getElementById("carttt")
const csrftoken = getCookie('csrftoken');


async function getCart() {
   
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
        console.log(data[i]["product_version"]);
        html += ` <ul class="row cart-details">
                            <li class="col-sm-6">
                                <div class="media"> 
                                <!-- Media Image -->
                                <div class="media-left media-middle"> <a href="#." class="item-img"> <img class="media-object" src="${data[i]["product_version"]["cover_image"]}" alt=""> </a> </div>
                                
                                <!-- Item Name -->
                                <div class="media-body">
                                    <div class="position-center-center">
                                    <h5>${data[i]["product_version"]["title"]}</h5>
                                    <p>${data[i]["product_version"]["description"]}</p>
                                    </div>
                                </div>
                                </div>
                            </li>
                            
                            <!-- PRICE -->
                            <li class="col-sm-2">
                                <div class="position-center-center"> <span class="pricee" value="${data[i]["product_version"]["price"]}"><small>$</small>${data[i]["product_version"]["price"]}</span> </div>
                            </li>
                            
                            <!-- QTY -->
                          
                            
                         
                            
                            <!-- REMOVE -->
                            <li class="col-sm-1">
                                <div class="position-center-center"> <span class="closee"><i class="icon-close"></i></span></div>
                            </li>
                            </ul>`;
  
                            
    }
    
    cartsss.innerHTML=html
    let close = document.getElementsByClassName("closee")
    console.log(close);

    for(let i=0;i<close.length;i++){
        close[i].addEventListener("click",()=>{
            console.log("bbb");
            remove(data[i]["id"])
        })
    }
    async function remove(itemId) {
      
        // Send a request to the server to remove the item from the cart
        await fetch(`${location.origin}/api/delete_wishlist/${itemId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken // Replace with your actual CSRF token
            }
        })
        .then(() => {
            getCart()
          
            console.log("yes");
        });
    }
    
 
    
      
      
        
}

)}


getCart()
