function validateForm(){
    const username = document.querySelector('input[name="username"]');
    const password = document.querySelector('input[name="password"]');
    const role = document.querySelector('select[name="role_id"]');
    const email = document.querySelector('input[name="email"]')
    const phone = document.querySelector('input[name="phone"]');

    if (!username.value){
        document.getElementById("username_error").innerHTML = 'This field is required.';
        return false
    }else{
        document.getElementById("username_error").innerHTML = '';
    }

     if (!password.value){
        document.getElementById("password_error").innerHTML = 'This field is required.';
        return false
    }else{
        document.getElementById("password_error").innerHTML = '';
    }

     if (!role.value){
        document.getElementById("role_error").innerHTML = 'This field is required.';
        return false
    }else{
        document.getElementById("role_error").innerHTML = '';
    }

     if (!email.value){
        document.getElementById("email_error").innerHTML = 'This field is required.';
        return false
    }else{
        document.getElementById("email_error").innerHTML = '';
    }

     if (!phone.value){
        document.getElementById("phone_error").innerHTML = 'This field is required.';
        return false
    }else{
        document.getElementById("phone_error").innerHTML = '';
    }



    if(username.value.length > 50){
        document.getElementById("username_error").innerHTML = 'Username must be 50 characters or less.';
        return false;
    }else if (username.value.length < 8){
        document.getElementById("username_error").innerHTML = 'Username must be 8 characters or more.';
        return false;
    }else{
        document.getElementById("username_error").innerHTML = '';
    }


    if(password.value.length > 50){
        document.getElementById("password_error").innerHTML ='Password must be 50 characters or less.';
        return false;
    }else if (password.value.length < 8){
        document.getElementById("password_error").innerHTML = 'Password must be 8 characters or more.';
        return false;
    }else{
        document.getElementById("password_error").innerHTML = '';
    }

    if(!/^[0-9]+$/.test(phone.value)){
        document.getElementById("phone_error").innerHTML = "Please only enter numeric number only for your Phone Number!";
        return false;
     }else{
        document.getElementById("phone_error").innerHTML = '';
    }

     return true;
}