document.addEventListener("DOMContentLoaded", function() {
    const progressContainer = document.querySelector('.progress-container');
    const progressBar = document.getElementById('progress-bar');
    const progressValue = progressContainer.getAttribute('data-progress');
    
    const validatedProgress = Math.min(Math.max(progressValue, 0), 100); // Ensure value is between 0 and 100
    progressBar.style.width = validatedProgress + '%';
});
