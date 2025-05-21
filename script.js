function getInputValue() {
    var inputValue = document.getElementById('nameInput').value;
    console.log('Input Value:', inputValue);
    const query = 'https://www.google.com/search?q=${inputValue}';
    document.location='https://www.google.com/search?q=', $;{inputValue}
}