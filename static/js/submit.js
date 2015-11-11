$(document).ready(function()
{   
    $("#invite-form").on('submit', function()
    {   
        var inviteeEmail = $("#email").val();
        console.log(inviteeEmail)

        if (!inviteeEmail || !inviteeEmail.length) {
            alert('Please enter an email');
            return false;
        }

        $.ajax({
          type: "POST",
          url: "/",
          headers: {
            'X-CSRFToken': csrfToken,
            },
          data: { email: inviteeEmail},
          success: function(data) {
            handleResponse(data);
          }
        });
        return false;
    });        
});

function handleResponse(data) {
    if (data.status === 'fail') {
      $("#response-text").text(getUserFriendlyError(data.error));
    }
    $("#response-div").removeClass('hidden');
}

function getUserFriendlyError(error){
  if(error === 'already_in_team'){
    return 'Already signed up! Click on "Sign in" below to get started';
  } else if(error === 'invalid_email'){
    return 'Thats an invalid email address. Please check again';
  } else if(error === 'already_invited'){
    return 'You have been invited already. Check your inbox!';
  } else if(error === 'invalid_auth'){
    return 'There seems to be some issues with the setup. Please contact the admin of this channel';
  } else{
    return error;
  }
}