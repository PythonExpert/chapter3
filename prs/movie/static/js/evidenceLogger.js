function postEvidence(user_id, content_id, event) {

    var now = new Date();
    var dateString = now.getFullYear() + '-' + now.getMonth() + '-' + now.getDate() + ' ' + now.getUTCHours() + ':' + now.getMinutes(); 
    $.ajax({  
          type: 'GET',  
          url: 'http://moviegeek.com:8000/log/' + content_id 
          		+ '/' + event 
          		+ '?date=' + dateString 
          		+ '&sessionid={{sessionId}}&userid={{user_id}}' ,  
    
          error: function(req, status, ex) { 
	          console.error("exception: " + ex);
          },  
          timeout:60000  
        });  

  };