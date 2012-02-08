$(document).ready(function() { 
  $('#city').focus(function(){
    if ($(this)._cleared) return;
    $(this).val('');
    $(this)._cleared = true;
  });  
  
  
  var locations = [
  ];

  
  $( "#city" ).autocomplete({
    source: locations,
    minLength: 2,
    select: function( event, ui ) {
      window.location.href += ui.item.circ + ".html"; 
    },
    open: function() {
      $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
    },
    close: function() {
      $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
    }
  });
	
});
