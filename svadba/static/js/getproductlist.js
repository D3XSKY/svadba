function addProductsToStore(product) {
	
 	var ul = document.getElementById("proizvodi");
		var root_div = document.createElement("div");
		//root_div.appendChild(document.createTextNode('<img src="productimgs/sirloin.png"/>'));
		root_div.setAttribute("class", "span6 element category0"+product.kategorija); // added root_divne
		root_div.setAttribute("data-category", "category0"+product.kategorija); // added root_divne
		//DIV1
		var div1 = document.createElement("div");
		div1.setAttribute("class", "hover_img");
		var img = document.createElement("img");
		img.setAttribute("src", "svadba-API/" + product.fajl); //SET IMAGE 
		img.setAttribute("alt", "");
		//alert(img)
		var span1 = document.createElement("span");
		span1.setAttribute("class", "portfolio_zoom");
		var a1 = document.createElement("a");
		a1.setAttribute("href", "svadba-API/" + product.fajl); //SET IMAGE
		a1.setAttribute("rel", "prettyPhoto[portfolio"+product.id+"]");
		span1.appendChild(a1);
		var span2 = document.createElement("span");
		span2.setAttribute("class", "portfolio_link");
		var a2 = document.createElement("a");
		a2.setAttribute("href", "single_portfolio.html?proizvod="+product.id);
		a2.appendChild(document.createTextNode("Pregled proizvoda"));
		span2.appendChild(a2);
		div1.appendChild(img);
		div1.appendChild(span1);
		div1.appendChild(span2);
		//DIV2
		var div2 = document.createElement("div");
		div2.setAttribute("class", "item_description");
		var title = document.createElement("h6");
		var a3 = document.createElement("a");
		a3.setAttribute("href", "single_portfolio.html?proizvod="+product.id);
		a3.appendChild(document.createTextNode(product.naziv)); //SET TITLE
		title.appendChild(a3);

		var describe = document.createElement("div");
		describe.setAttribute("class", "descr");
		describe.appendChild(document.createTextNode(product.opis));//SET DESCRIPTION
		
		div2.appendChild(title);
		div2.appendChild(describe);

		root_div.appendChild(div1);
		root_div.appendChild(div2);
		ul.appendChild(root_div);
	};

function loadXMLDoc() {
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
       if (xmlhttp.status == 200) {
       	   result = JSON.parse(xmlhttp.responseText);
       	   localStorage.setItem("products", xmlhttp.responseText);
		for (var i = 0; i < result.length; i++) 
           addProductsToStore(result[i]);
       }
       else if (xmlhttp.status == 400) {
          alert('There was an error 400');
       }
       else {
           alert('There was other error!');
       }
    }
};
xmlhttp.open("GET", "http://127.0.0.1:8000/proizvodi/prikaz/", false);
xmlhttp.send();
}

loadXMLDoc();
