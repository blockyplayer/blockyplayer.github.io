function getInputValue() {
    var inputValue = document.getElementById('nameInput').value;
    console.log('Input Value:', inputValue);
    const query = 'https://www.google.com/search?q=${inputValue}';
    document.location='https://www.google.com/search?q=', $;{inputValue}
}

const url = 'https://api.ipstack.com/check?access_key=20c69cfe46bda218d7180411032a148e';
const options = {
	method: 'GET'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}