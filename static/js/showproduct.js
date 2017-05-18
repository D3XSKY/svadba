function addProduct(product) 
{
  
    var img = document.getElementById("mainslika");
    img.setAttribute("src", "svadba-API/" + product.fajl); //SET IMAGE 
    var naslov = document.getElementById("naslov");
    naslov.appendChild(document.createTextNode(product.naziv));
    var opis = document.getElementById("opis");
    opis.appendChild(document.createTextNode(product.opis));
};

var QueryString = function () {
  // This function is anonymous, is executed immediately and 
  // the return value is assigned to QueryString!
  var query_string = {};
  var query = window.location.search.substring(1);
  var vars = query.split("&");
  for (var i=0;i<vars.length;i++) {
    var pair = vars[i].split("=");
        // If first entry with this name
    if (typeof query_string[pair[0]] === "undefined") {
      query_string[pair[0]] = decodeURIComponent(pair[1]);
        // If second entry with this name
    } else if (typeof query_string[pair[0]] === "string") {
      var arr = [ query_string[pair[0]],decodeURIComponent(pair[1]) ];
      query_string[pair[0]] = arr;
        // If third or later entry with this name
    } else {
      query_string[pair[0]].push(decodeURIComponent(pair[1]));
    }
  } 
  return query_string;
}();

/*function loadXMLDoc() {
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
       if (xmlhttp.status == 200) {
           alert(xmlhttp.responseText);
       	   result = JSON.parse(xmlhttp.responseText);
       else if (xmlhttp.status == 400) {
          alert('There was an error 400');
       }
       else {
           alert('There was other error!');
       }
    }
};
xmlhttp.open("GET", "http://127.0.0.1:8000/proizvodi/prikaz/"+QueryString.proizvod, false);
xmlhttp.send();
}

loadXMLDoc();
*/


var products = JSON.parse(localStorage.getItem("products"));

for (var i = products.length - 1; i >= 0; i--)
  if(products[i].id == QueryString.proizvod) addProduct(products[i]);