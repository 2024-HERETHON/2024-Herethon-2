document.addEventListener("DOMContentLoaded", function () {
    const today = new Date();
    let currentWeekStart = new Date(today);
    currentWeekStart.setDate(today.getDate() - today.getDay()); // 이번 주 시작 날짜 계산
    let currentMonthStart = new Date(today.getFullYear(), today.getMonth(), 1); // 이번 달 시작 날짜 계산

    const monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    // 날짜 업데이트 함수
    function updateCalendarDates(startOfWeek) {
        const days = document.querySelectorAll(".week-cal .day");
        days.forEach((dayElement, index) => {
            const date = new Date(startOfWeek);
            date.setDate(startOfWeek.getDate() + index);
            dayElement.textContent = date.getDate();
            dayElement.dataset.day = date.getDay();

            // 오늘 날짜 마킹
            if (date.getDate() === today.getDate() && date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear()) {
                dayElement.classList.add('today-mark');
            } else {
                dayElement.classList.remove('today-mark');
            }
        });
        updateTitleDate(startOfWeek, "week");
    }

    function updateMonthCalendarDates(startOfMonth) {
        const days = document.querySelectorAll(".month-cal .m-day");
        const year = startOfMonth.getFullYear();
        const month = startOfMonth.getMonth();
        const firstDayOfMonth = new Date(year, month, 1);
        const startDay = firstDayOfMonth.getDay(); // 월의 첫째 날의 요일 (0: 일요일, 1: 월요일, ..., 6: 토요일)
        const lastDate = monthDays[month];

        days.forEach((dayElement, index) => {
            if (index >= startDay && index < startDay + lastDate) {
                const date = new Date(year, month, index - startDay + 1);
                dayElement.textContent = date.getDate();
                dayElement.dataset.day = date.getDay();

                // 오늘 날짜 마킹
                if (date.getDate() === today.getDate() && date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear()) {
                    dayElement.classList.add('today-mark');
                } else {
                    dayElement.classList.remove('today-mark');
                }

                dayElement.style.display = 'block';
            } else {
                dayElement.textContent = "";
                dayElement.style.display = 'none';
            }
        });
        updateTitleDate(firstDayOfMonth, "month");
    }

    function updateTitleDate(startDate, viewType) {
        const titleDate = document.querySelector('.title-date');
        const year = startDate.getFullYear();

        if (viewType === "week") {
            const startMonth = startDate.getMonth() + 1;
            const endDate = new Date(startDate);
            endDate.setDate(startDate.getDate() + 6);
            const endMonth = endDate.getMonth() + 1;
            const monthDisplay = startMonth !== endMonth
                ? `${startMonth}월 - ${endMonth}월`
                : `${startMonth}월`;
            titleDate.textContent = `${year}년 ${monthDisplay}`;
        } else if (viewType === "month") {
            const month = startDate.getMonth() + 1;
            titleDate.textContent = `${year}년 ${month}월`;
        }
    }

    function initializeDates() {
        const year = today.getFullYear();
        const month = today.getMonth() + 1;
        const day = today.getDate();
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
    }

    function getWeekNumber(date) {
        const startOfMonth = new Date(date.getFullYear(), date.getMonth(), 1);
        const pastDaysOfMonth = (date - startOfMonth) / 86400000;
        return Math.ceil((pastDaysOfMonth + startOfMonth.getDay() + 1) / 7);
    }

    initializeDates();
    updateCalendarDates(currentWeekStart);

    // 주<->월 버튼
    const calBtn = document.querySelector(".cal_btn");
    const weekCal = document.querySelector(".week-cal");
    const monthCal = document.querySelector(".month-cal");
    const todo = document.querySelector(".todo");
    let isWeekView = true;

    calBtn.addEventListener('click', function () {
        if (isWeekView) {
            calBtn.textContent = '월';
            weekCal.classList.add('nodisplay');
            weekCal.classList.remove('display');
            todo.classList.add('nodisplay');
            todo.classList.remove('display');
            monthCal.classList.add('display');
            monthCal.classList.remove('nodisplay');
            currentMonthStart = new Date(today.getFullYear(), today.getMonth(), 1);
            updateMonthCalendarDates(currentMonthStart);
            isWeekView = false;
        } else {
            calBtn.textContent = '주';
            monthCal.classList.add('nodisplay');
            monthCal.classList.remove('display');
            weekCal.classList.add('display');
            weekCal.classList.remove('nodisplay');
            todo.classList.add('display');
            todo.classList.remove('nodisplay');
            currentWeekStart = new Date(today);
            currentWeekStart.setDate(today.getDate() - today.getDay());
            updateCalendarDates(currentWeekStart);
            isWeekView = true;
        }
    });

    // 캘린더 날짜 이동 버튼
    const leftBtn = document.querySelector(".left-btn");
    const rightBtn = document.querySelector(".right-btn");

    leftBtn.addEventListener('click', function () {
        if (isWeekView) {
            currentWeekStart.setDate(currentWeekStart.getDate() - 7);
            updateCalendarDates(currentWeekStart);
        } else {
            currentMonthStart.setMonth(currentMonthStart.getMonth() - 1);
            updateMonthCalendarDates(currentMonthStart);
        }
    });

    rightBtn.addEventListener('click', function () {
        if (isWeekView) {
            currentWeekStart.setDate(currentWeekStart.getDate() + 7);
            updateCalendarDates(currentWeekStart);
        } else {
            currentMonthStart.setMonth(currentMonthStart.getMonth() + 1);
            updateMonthCalendarDates(currentMonthStart);
        }
    });

    
});
