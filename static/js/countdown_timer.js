    // Countdown timer
    let countdownElementID = document.getElementById('countdown_timer');
    let alertClass = document.getElementById('alert');
    let time = 2;

    function countdownTimer() {
        let countdownInterval = setInterval(function() {
            countdownElementID.textContent = time;
            time--;

            if (time < 0) {
                clearInterval(countdownInterval);
                window.location.href = redirectPageURL;
           }
       }, 1000);
    }

    countdownTimer();