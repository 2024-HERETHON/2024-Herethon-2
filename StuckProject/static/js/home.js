document.addEventListener("DOMContentLoaded", function () {

    //진행도
    const progressContainer = document.querySelector('.progress-container');
    const progressBar = document.querySelector('.progress-bar');
    const progressValue = progressContainer.getAttribute('data-progress');

    const validatedProgress = Math.min(Math.max(progressValue, 0), 100);
    progressBar.style.width = validatedProgress + '%';

    //캘린더
    const today = new Date();
    const dayOfWeek = today.getDay();
    const startOfWeek = new Date(today);
    startOfWeek.setDate(today.getDate() - dayOfWeek);

    const year = today.getFullYear();
    const month = today.getMonth() + 1;
    const day = today.getDate();

    // 주차 계산 
    function getWeekNumber(date) {
        const startOfMonth = new Date(date.getFullYear(), date.getMonth(), 1);
        const pastDaysOfMonth = (date - startOfMonth) / 86400000;
        return Math.ceil((pastDaysOfMonth + startOfMonth.getDay() + 1) / 7);
    }

    // 몇 주차인지 계산
    const weekNumber = getWeekNumber(today);

    const yearElements = document.querySelectorAll('.year');
    yearElements.forEach(element => {
        element.textContent = year;
    });

    const monthElements = document.querySelectorAll('.month');
    monthElements.forEach(element => {
        element.textContent = month;
    });
    const dayElements = document.querySelectorAll('.day');
    dayElements.forEach(element => {
        element.textContent = day;
    });
    const weekElements = document.querySelectorAll('.week');
    weekElements.forEach(element => {
        element.textContent = weekNumber;
    });

    const days = document.querySelectorAll(".week-cal .day");
    days.forEach((dayElement, index) => {
        const date = new Date(startOfWeek);
        date.setDate(startOfWeek.getDate() + index);
        dayElement.textContent = date.getDate();
    });

    

});


