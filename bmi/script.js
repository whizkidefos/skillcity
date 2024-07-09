function calculateBMI() {
    const weight = parseFloat(document.getElementById("weight").value);
    const height = parseFloat(document.getElementById("height").value) / 100; // Convert cm to meters

    if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {
        alert("Please enter valid weight and height.");
        return;
    }

    const bmi = weight / (height * height);
    const resultElement = document.getElementById("result");

    resultElement.innerHTML = `Your BMI is: ${bmi.toFixed(2)}`;

    if (bmi < 18.5) {
        resultElement.innerHTML += " (Underweight)";
    } else if (bmi >= 18.5 && bmi < 25) {
        resultElement.innerHTML += " (Normal weight)";
    } else if (bmi >= 25 && bmi < 30) {
        resultElement.innerHTML += " (Overweight)";
    } else {
        resultElement.innerHTML += " (Obese)";
    }
}