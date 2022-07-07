var doc1 = document.getElementById('doc1')
var doc2 = document.getElementById('doc2')
doc1_data = doc1.innerText()
doc2_data = doc2.innerText()

var percentage = 0
var msg = document.getElementById('message')

var submit_button = document.getElementById('submit-b')
submit_button.addEventListener('click', send_data)

function send_data() {
    // send the two strings to python function
    // Send doc1_data and doc2_data to python file and get plagiarism data in percentage variable
}

if (percentage == 0) {
    msg.textContent = 'Message: No Plagiarism Found. Your document is unique!';
}
if (percentage > 0 && percentage < 20) {
    msg.textContent = 'Message: Plagiarism level can reach zero with some improvements!';
}
if (percentage > 20 && percentage < 50) {
    msg.textContent = 'Message: Little amout of plagiarism detected!';
}
if (percentage > 50 && percentage < 100) {
    msg.textContent = 'Message: Significant amout of plagiarism detected!';
}
if (percentage == 100) {
    msg.textContent = 'Message: The two documents are same!';
}
console.log('Job Done')
// var tag = document.getElementsById("doc1")[0];
// text = tag.innerHTML;
// // Here I would like to call the Python interpreter with Python function
// final_output = openSomehowPythonInterpreter("plagiarism-checker.py", "Plagiarism_Checker(doc1_data, doc2_data)");
// console.log(final_output)
