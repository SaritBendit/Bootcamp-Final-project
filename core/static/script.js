const chooseDate = (e) => {
    const date = e.target.value;
    console.log(date)
    const hoursEl = document.getElementById("hoursUsed");
    if (hoursEl !== null) {
        const usedHours = JSON.parse(hoursEl.textContent);

        const el = document.getElementById("id_hours");
        const allHours = [...el];

        const freeHours = [];

        const usedPerDay = [];
        for (used of usedHours){
            if (used[0] === date){
                usedPerDay.push(used[1])
            }
        }
        const allH = document.querySelector('#id_hours').getElementsByTagName("option");
        for (hour of allHours){
            if (usedPerDay.includes(hour.text)){
                hour.disabled = true;
                hour.classList.add('white')
            }
            else{
                console.log(typeof (hour.text))
                console.log(hour.text , usedPerDay)
            }
        }
        console.log(freeHours);
        return freeHours
    }

};

// document.getElementById('id_dates').addEventListener("click",chooseDate);

document.getElementById("id_dates").addEventListener("click", chooseDate);



