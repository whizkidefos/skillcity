let currentInput = '';
let currentOperator = null;
let previousInput = null;

function appendNumber(number) {
    currentInput += number;
    updateDisplay();
}

function setOperator(operator) {
    if (currentInput !== '') {
        if (previousInput !== null) {
            calculate();
        }
        previousInput = currentInput;
        currentInput = '';
        currentOperator = operator;
    }
}

function clearDisplay() {
    currentInput = '';
    previousInput = null;
    currentOperator = null;
    updateDisplay();
}

function calculate() {
    let result;
    const num1 = parseFloat(previousInput);
    const num2 = parseFloat(currentInput);

    if (isNaN(num1) || isNaN(num2)) return;

    switch (currentOperator) {
        case '+': result = num1 + num2; break;
        case '-': result = num1 - num2; break;
        case '*': result = num1 * num2; break;
        case '/': result = num1 / num2; break;
    }
    currentInput = result.toString();
    previousInput = null;
    currentOperator = null;
    updateDisplay();
}

function updateDisplay() {
    document.getElementById('display').value = currentInput;
}
