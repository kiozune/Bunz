function validateForm(){
    const principal = document.querySelector('input[name="principal"]').value.trim();
    const interest_rate = document.querySelector('input[name="interest_rate"]').value.trim();
    const years = document.querySelector('input[name="years"]').value.trim();


    // Check if the Principal field is empty
    if (!principal){
        document.getElementById("principal_error").innerHTML = 'This field is required !';
        return false;
    } else if(!/^[0-9.]+$/.test(principal)){
        document.getElementById("principal_error").innerHTML = "Please enter only numeric values !";
        return false;
    } else if (parseFloat(principal) === 0) {
        document.getElementById("principal_error").innerHTML = '0 is not allowed!';
        return false;
    }else {
        document.getElementById("principal_error").innerHTML = '';
    }

    // Check if the Interest Rate field is empty
    if (!interest_rate){
        document.getElementById("interest_rate_error").innerHTML = 'This field is required !';
        return false;
    } else if(!/^[0-9.]+$/.test(interest_rate)){
        document.getElementById("interest_rate_error").innerHTML = "Please enter a valid numeric value !";
        return false;
    } else if (parseFloat(interest_rate) === 0) {
        document.getElementById("interest_rate_error").innerHTML = '0 is not allowed!';
        return false;
    } else {
        document.getElementById("interest_rate_error").innerHTML = '';
    }

    // Check if the Years field is empty
    if (!years){
        document.getElementById("years_error").innerHTML = 'This field is required !';
        return false;
    } else if(!/^[0-9]+$/.test(years)){
        document.getElementById("years_error").innerHTML = "Please enter only numeric values!";
        return false;
    }else if (parseFloat(years) === 0) {
        document.getElementById("years_error").innerHTML = '0 is not allowed!';
        return false;
    } else {
        document.getElementById("years_error").innerHTML = '';
    }

    return true;
}
