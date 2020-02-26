const chooseDate = (e) => {
    const date = e.target.value;
    const hoursEl = document.getElementById("hoursUsed");
    console.log("hi", hoursEl)

    if (hoursEl) {
        const usedHours = JSON.parse(hoursEl.textContent);
        if (usedHours[1] === date) {
            console.log("date=  " + date);
            console.log("date=  " + usedHours[1]);

            console.log(usedHours);
            const el = document.getElementById("id_hours");
            const allHours = [...el];
            const freeHours = [];
            for (element of usedHours) {
                if (element[1] === date) {
                    for (let i = 0; i < allHours.length; i++) {
                        let hourIsUsed = false;
                        for (let j = 0; j < usedHours.length; j++) {
                            if (allHours[i].text === usedHours[j]) {
                                console.log("Hour is used", allHours[i].text);
                                hourIsUsed = true;
                                break;
                            }
                        }
                        if (hourIsUsed === false) {
                            freeHours.push(allHours[i].text)
                        }
                    }

                }
            }
            return freeHours
        }


    }


    // const x = hours.filter(item => {
    //     return !item.text.includes("9:00")
    // });
    //
    // console.log(x);


//     var option = document.createElement("option");
// option.text = "Text";
// option.value = "myvalue";
// var select = document.getElementById("id-to-my-select-box");
// select.appendChild(option);


};

// document.getElementById('id_dates').addEventListener("click",chooseDate);

document.getElementById("id_dates").addEventListener("click", chooseDate);

