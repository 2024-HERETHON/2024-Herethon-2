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

    //주<->월
    const calBtn = document.querySelector(".cal_btn");
    const weekCal = document.querySelector(".week-cal");
    const monthCal = document.querySelector(".month-cal");
    calBtn.addEventListener('click', function() {
        let buttonText = calBtn.textContent.trim();
        if (buttonText === '주') {
            calBtn.textContent = '월';
            weekCal.classList.remove('display');
            weekCal.classList.add('nodisplay');
            monthCal.classList.remove('nodisplay');
            monthCal.classList.add('display');

        } else {
            calBtn.textContent = '주';
            monthCal.classList.remove('display');
            monthCal.classList.add('nodisplay');
            weekCal.classList.remove('nodisplay');
            weekCal.classList.add('display');
        }
        
    });
});


