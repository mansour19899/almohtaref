$(window).scroll(function() {

    //After scrolling 100px from the top...
    if ( $(window).scrollTop() >= 500 ) {
      $('#mainheader').css('background-color','rgba(255, 255, 255,1)');  
      $('#Btntop').css('display','block');   

    //Otherwise remove inline styles and thereby revert to original stying
    } 
    else if( $(window).scrollTop() >= 150){
      $('.hii').css('background-size', '2.8rem');
      $('.hii').css('background-position-y', '0.1rem');
      $('.hii').css('height', '5rem');
    }
    else {
        $('.hii').css('background-size', '5rem'); 
        $('.hii').css('background-position-y', '1rem');
        $('.hii').css('height', '10rem');
        $('#mainheader').css('background-color','rgba(255, 255, 255,0.5)'); 
        $('#Btntop').css('display','none');   
    }
});

// ------------------------modalgallry---------------------------
function openModal() {
    document.getElementById("myModal").style.display = "block";
  }
  
  function closeModal() {
    document.getElementById("myModal").style.display = "none";
  }
  
  var slideIndex = 1;
  showSlides(slideIndex);
  
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  
  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    captionText.innerHTML = dots[slideIndex-1].alt;
  }
// -----------------------------end---------------------

// -----------------------scrooltop----------------------------

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// ------------------------------menu mobile----------------------------

function myFunction() {
  var x = document.getElementById("myLinks");
  var xx=document.getElementById("menumobile");
  if (x.style.display === "block") {
    x.style.display = "none";
    xx.innerText="menu";
  } else {
    x.style.display = "block";
    xx.innerText="close";   

  }
}