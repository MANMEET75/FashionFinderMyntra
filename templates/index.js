function updateCountdown() {
    // Set the target date and time (e.g., May 31, 2023 00:00:00)
    const targetDate = new Date("May 31, 2023 00:00:00").getTime();

    // Get the current date and time
    const currentDate = new Date().getTime();

    // Calculate the difference in seconds between the target and current date/time
    const difference = Math.floor((targetDate - currentDate) / 1000);

    // Calculate the days, hours, minutes, and seconds
    const days = Math.floor(difference / (24 * 60 * 60));
    const hours = Math.floor((difference % (24 * 60 * 60)) / (60 * 60));
    const minutes = Math.floor((difference % (60 * 60)) / 60);
    const seconds = Math.floor(difference % 60);

    // Display the countdown in the HTML elements
    document.getElementById("days").textContent = formatTime(days);
    document.getElementById("hours").textContent = formatTime(hours);
    document.getElementById("minutes").textContent = formatTime(minutes);
    document.getElementById("seconds").textContent = formatTime(seconds);
}

function formatTime(time) {
    // Pad the time with leading zeros if it's less than 10
    return time < 10 ? `0${time}` : time;
}

// Update the countdown every second
setInterval(updateCountdown, 1000);

