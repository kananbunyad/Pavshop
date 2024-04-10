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
let cartt=document.getElementById("cartttt")
let btn=document.getElementById("carttt")
const csrftoken = getCookie('csrftoken');


async function getCart() {
   
    const url = `${location.origin}/api/create_order`
    await fetch(url)
    .then((response) => {
    if (!response.ok) {
        throw new Error("API request failed.");
    }
    return response.json();
    })
    .then((data) => {

    console.log("carttt",data);
    let html=""
    for(let i=0;i<data.length;i++){
        console.log(data[i]["product_version"]);
        console.log(data[i]["cart"]["user"])
        if(data[i]["cart"]["user"] == parseInt(cartt.getAttribute("data-id"))){
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
                            <li class="col-sm-1">
                                <div class="position-center-center">
                                <div class="quinty"> 
                                    <!-- QTY -->
                                    <input type="number" class="qtyyyy" min="0" value="${data[i]["quantity"]}"/>
                                </div>
                                </div>
                            </li>
                            
                            <!-- TOTAL PRICE -->
                            <li class="col-sm-2">
                                <div class="position-center-center"> <span class="price" ><small>$</small> <span class="total" value=""></span></span> </div>
                            </li>
                            
                            <!-- REMOVE -->
                            <li class="col-sm-1">
                                <div class="position-center-center"> <span class="closee"><i class="icon-close"></i></span></div>
                            </li>
                            </ul>`;
  
                            
    }}
    
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
        await fetch(`${location.origin}/api/delete_order/${itemId}`, {
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
    
 
    let total=document.getElementsByClassName("total")
    let quantittyy=document.getElementsByClassName("qtyyyy")
    
    for(let i=0;i<quantittyy.length;i++){
        console.log(quantittyy[i]);
    }
    console.log(quantittyy[0].getAttribute("value"));
    let price=document.getElementsByClassName("pricee")
    for(let i=0;i<total.length;i++){
      
        total[i].innerHTML=parseFloat(price[i].getAttribute("value"))*parseFloat(quantittyy[i].value)
        console.log(total[i]);
    }
  
    for(let i=0;i<quantittyy.length;i++){
        quantittyy[i].addEventListener("change",()=>{
            console.log(price[i].value,quantittyy[i].value);
            total[i].innerHTML=parseFloat(price[i].getAttribute("value"))*parseFloat(quantittyy[i].value)
        })
    }
   
    
        })

      
      
        
}


// const addCart = {
//     async addProductCart(ProductID, Quantity=1) {
//         const response = await fetch(`${location.origin}/api/create_order`, {
            
//             method: 'POST',
//             headers: {
//                 'Content-type': 'application/json',
//                 'X-CSRFToken': csrftoken,
//             },
//             body: JSON.stringify({
//                 'product_version': ProductID,
//                 'quantity': Quantity
//             })
//         }).then(response=>response.json()).then(data=>{
//             let html=""
//             for(let i=0;i<data.length;i++){
//                 html += ` <ul class="row cart-details">
//                 <li class="col-sm-6">
//                     <div class="media"> 
//                     <!-- Media Image -->
//                     <div class="media-left media-middle"> <a href="#." class="item-img"> <img class="media-object" src="${data[i]["product_version"]["cover_image"]}" alt=""> </a> </div>
                    
//                     <!-- Item Name -->
//                     <div class="media-body">
//                         <div class="position-center-center">
//                         <h5>${data[i]["product_version"]["title"]}</h5>
//                         <p>${data[i]["product_version"]["description"]}</p>
//                         </div>
//                     </div>
//                     </div>
//                 </li>
                
//                 <!-- PRICE -->
//                 <li class="col-sm-2">
//                     <div class="position-center-center"> <span class="price"><small>$</small>${data[i]["product_version"]["price"]}</span> </div>
//                 </li>
                
//                 <!-- QTY -->
//                 <li class="col-sm-1">
//                     <div class="position-center-center">
//                     <div class="quinty"> 
//                         <!-- QTY -->
//                         <input type="number" min="0" value="${data[i]["quantity"]}"/>
//                     </div>
//                     </div>
//                 </li>
                
//                 <!-- TOTAL PRICE -->
//                 <li class="col-sm-2">
//                     <div class="position-center-center"> <span class="price"><small>$</small>${data[i]["product_version"]["price"]*data[i]["quantity"]}</span> </div>
//                 </li>
                
//                 <!-- REMOVE -->
//                 <li class="col-sm-1">
//                     <div class="position-center-center"> <a href="#."><i class="icon-close"></i></a> </div>
//                 </li>
//                 </ul>`
//             }
//             cartsss.innerHTML=html
          
//         });

      

//     }
// }      
        

// function functionAddToBasket(ProductID) {
//     const quantity = 1;
//     addCart.addProductCart(ProductID, quantity);
// } 



getCart()
