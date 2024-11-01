<script>
function validateForm(){
    const role = document.querySelector('input[name="role"]');
    const description = document.querySelector('input[name="description"]');
    if (!role.value) {
        alert('Role is required.');
        return false;
    }

    if (role.value.length > 50) {
        alert('Role must be 50 characters or less.');
        return false;
    }

    if (description.value.length > 200) {
        alert('Description must be 250 characters or less.');
        return false;
    }

     return true;
}
</script>