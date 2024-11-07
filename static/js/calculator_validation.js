function validateForm(){
    const principal = document.querySelector('input[name="principal"]');
    const interest_rate = document.querySelector('input[name="interest_rate"]');
    const years = document.querySelector('input[name="years"]');

    // Check if the Principal field is empty
    if (!principal.value){
        document.getElementById("principal_error").innerHTML = 'This field is required !';
        return false;
    } else if(!/^[0-9]+$/.test(principal.value)){
        document.getElementById("principal_error").innerHTML = "Please enter only numeric values !";
        return false;
    } else {
        document.getElementById("principal_error").innerHTML = '';
    }

    // Check if the Interest Rate field is empty
    if (!interest_rate.value){
        document.getElementById("interest_rate_error").innerHTML = 'This field is required !';
        return false;
    } else if(!/^[0-9.]+$/.test(interest_rate.value)){
        document.getElementById("interest_rate_error").innerHTML = "Please enter a valid numeric value !";
        return false;
    } else {
        document.getElementById("interest_rate_error").innerHTML = '';
    }

    // Check if the Years field is empty
    if (!years.value){
        document.getElementById("years_error").innerHTML = 'This field is required !';
        return false;
    } else if(!/^[0-9]+$/.test(years.value)){
        document.getElementById("years_error").innerHTML = "Please enter only numeric values!";
        return false;
    } else {
        document.getElementById("years_error").innerHTML = '';
    }

    return true;
}
