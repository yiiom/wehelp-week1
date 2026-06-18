const services = [
    { name: "S1", r: 4.5, c: 1000 },
    { name: "S2", r: 3, c: 1200 },
    { name: "S3", r: 3.8, c: 800 }
];

const bookings = {
    S1: [],
    S2: [],
    S3: []
};

function func2(ss, start, end, criteria) {
    let field;
    let value;
    let operator;

    if (criteria.includes(">=")) {
        [field, value] = criteria.split(">=");
        operator = ">=";
    } else if (criteria.includes("<=")) {
        [field, value] = criteria.split("<=");
        operator = "<=";
    } else {
        [field, value] = criteria.split("=");
        operator = "=";
    }

    if (field !== "name") {
        value = Number(value);
    }

    let candidates = [];

    for (let service of ss) {
        let match = false;

        if (operator === "=") {
            match = service[field] === value;
        } else if (operator === ">=") {
            match = service[field] >= value;
        } else if (operator === "<=") {
            match = service[field] <= value;
        }

        if (!match) {
            continue;
        }

        let conflict = false;

        for (let booking of bookings[service.name]) {
            let oldStart = booking[0];
            let oldEnd = booking[1];

            if (start < oldEnd && end > oldStart) {
                conflict = true;
                break;
            }
        }

        if (!conflict) {
            candidates.push(service);
        }
    }

    if (candidates.length === 0) {
        console.log("Sorry");
        return;
    }

    let chosen;

    if (operator === ">=") {
        chosen = candidates[0];

        for (let service of candidates) {
            if (service[field] < chosen[field]) {
                chosen = service;
            }
        }
    } else if (operator === "<=") {
        chosen = candidates[0];

        for (let service of candidates) {
            if (service[field] > chosen[field]) {
                chosen = service;
            }
        }
    } else {
        chosen = candidates[0];
    }

    console.log(chosen.name);

    bookings[chosen.name].push([start, end]);
}

func2(services, 15, 17, "c>=800");
func2(services, 11, 13, "r<=4");
func2(services, 10, 12, "name=S3");
func2(services, 15, 18, "r>=4.5");
func2(services, 16, 18, "r>=4");
func2(services, 13, 17, "name=S1");
func2(services, 8, 9, "c<=1500");