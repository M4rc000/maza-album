document.addEventListener("DOMContentLoaded", function () {
    // Select all audio elements
    const audioPlayers = document.querySelectorAll(".audio-player");
    
    // Generate a random index
    const randomIndex = Math.floor(Math.random() * audioPlayers.length);
    
    // Play the randomly selected audio
    audioPlayers[randomIndex].play();
});