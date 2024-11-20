let string = '';
let buttons = document.querySelectorAll('button');

Array.from(buttons).forEach((button) => {
    button.addEventListener('click', (e) => {
        try {
            if (e.target.innerText == '=') {
                string = eval(string);
                document.querySelector('input').value = string;
            }
            else if (e.target.innerText == 'C') {
                string = '';
                document.querySelector('input').value = string;
            }
            else if (e.target.innerText == 'M+') {
                let memory = document.querySelector('input').value;
                localStorage.setItem('memory', memory);
            }
            else if (e.target.innerText == 'M-') {
                localStorage.removeItem('memory');
            }
            else if (e.target.innerText == 'MRC') {
                let memory = localStorage.getItem('memory');
                document.querySelector('input').value = memory;
            }
            else {
                console.log(e.target);
                string += e.target.innerText;
                document.querySelector('input').value = string;
            }
        } catch (error) {
            console.error('An error occurred:', error);
        }
    });
});