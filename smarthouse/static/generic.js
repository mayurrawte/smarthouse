$(document).ready(function ()
{
    $('#loginbtn').on('click',function (event)
    {
        event.preventDefault();
       var username = document.getElementById('username').value;
       var password = document.getElementById('password').value;

        $.ajax({
            type : "POST",
            url : "/login/",
            data : {
                username : username,
                password : password
            },
            success : function(data)
            {
                console.log(data);
                if(data == 'OK')
                {
                    window.location = "/home/"
                }
            },
            error: function (xhr, errmsg, err)
            {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });
    });

    $('#registerbtn').on('click',function (event)
    {
        event.preventDefault();
        var name = document.getElementById('name').value;
        var email = document.getElementById('email').value;

        $.ajax({
            type : "POST",
            url : "/register/",
            data : {
                name : name,
                email : email
            },
            success : function(data)
            {
                console.log(data);
                if(data == 'OK')
                {
                    window.location = "/home/"
                }
            },
            error: function (xhr, errmsg, err)
            {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });


    });
});