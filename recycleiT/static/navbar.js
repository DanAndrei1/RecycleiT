 window.onscroll = function() {scrollFunction()};
    var a = 0

    function setMinHeight() {
        var header = document.getElementById('head');
        var backgroundImage = new Image();
        backgroundImage.src = getComputedStyle(header).backgroundImage.replace(/url\((['"])?(.*?)\1\)/gi, '$2').split(',')[0];

        backgroundImage.onload = function() {
            var imageHeight = this.height;
            a = imageHeight
            header.style.minHeight = imageHeight + 'px';
        };
    }

    window.addEventListener('load', setMinHeight);
    function scrollFunction() {
      var navbar = document.getElementById("navbar");
      var logo = document.getElementById("logo");

      if ((document.body.scrollTop > 80 && document.documentElement.scrollTop > 80) || (document.body.scrollMarginBottom > 150  || document.documentElement.scrollTop > 150)) {
        logo.getElementsByTagName("img")[0].style.height = "50px";

        navbar.style.backgroundColor = "rgba(0 , 0 , 0,  0.2)";
        navbar.style.padding = "10px";
      } else{
        logo.getElementsByTagName("img")[0].style.height = "50px";

        navbar.style.backgroundColor = "transparent";
        navbar.style.padding = "0px";
      }
    }