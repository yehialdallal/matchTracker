


$( document ).ready(function() {
    var arr = ['bg_1.jpg','bg_2.jpg','bg_3.jpg'];
    
    var i = 0;
    setInterval(function(){
        if(i == arr.length - 1){
            i = 0;
        }else{
            i++;
        }
        var img = 'url(../assets/images/'+arr[i]+')';
        $(".full-bg").css('background-image',img); 
     
    }, 4000)

});


///////////////////////////////////////////////////////
// Validate Email

/*

const button = document.getElementById('signin');
const content = document.getElementById('menu');

// define the function to change the HTML content
function changeContent() {   
var nav = document.createElement('nav');
nav.setAttribute('class','navbar navbar-default');

var outerdiv = document.createElement('div');
outerdiv.setAttribute('class','container-fluid');

var innerdiv = document.createElement('div');
innerdiv.setAttribute('class','navbar-header');

var ul = document.createElement('ul');
ul.setAttribute('class','nav navbar-nav');

for (var i=0; i<5; i++){
    var li=document.createElement('li');
    li.innerHTML='fess';
    //li.setAttribute('class','list-group-item');
    ul.appendChild(li);
}

//outerdiv.appendChild(innerdiv)
outerdiv.appendChild(ul);
nav.appendChild(outerdiv);
content.innerHTML = '';
content.appendChild(nav);
}

*/


///////////////
/*<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">WebSiteName</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">Page 1</a></li>
      <li><a href="#">Page 2</a></li>
      <li><a href="#">Page 3</a></li>
    </ul>
  </div>
</nav>
*/
///////////////

// add event listener to the button
button.addEventListener('click', changeContent);






