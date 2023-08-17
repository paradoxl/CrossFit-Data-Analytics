const logoImgElem = document.getElementById('plot');
const selectElem = document.getElementById('comboselector');
document.addEventListener("DOMContentLoaded", function() {
    var select = document.getElementById("comboselector");
    var logoImgElem = document.getElementById("plot");
  
    document.getElementById('button').onclick = function() {
      logoImgElem.src = 'static/images/' + select.options[select.selectedIndex].value + '.png';
    };
  });