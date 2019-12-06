document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });

$(document).ready(function() {
    $(".dropdown-trigger").dropdown();
    $('input#input_text').characterCounter();
    $('select').formSelect();
    $('.datepicker').datepicker();
    //$('.sidenav').sidenav();
  });
