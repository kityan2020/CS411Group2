const searchButton = document.querySelector('#search-button');
const searchInput = document.querySelector('#search-input');
const resultsDiv = document.querySelector('#results');
const addButton = document.querySelector('#add-button');
const addInput = document.querySelector('#add-input');

searchButton.addEventListener('click', async () => {
    const query = searchInput.value;
    console.log(query)
    
    const response = await fetch(`/api/search?q=${query}`);
    console.log(response.body)
    const data = await response.json();
    displayResults(data);
    console.log(data)
});

addButton.addEventListener('click', async () => {
    const s = addInput.value;
    console.log(s)
    const response = await fetch(`/add/song?s=${s}`);
    console.log(response.body)
});




function displayResults(data) {
    
    const results = data;
    resultsDiv.innerHTML = '';
    if (results.length === 0) {
        resultsDiv.textContent = 'No results found';
        return;
    }
    const ul = document.createElement('ul');
    results.forEach(result => {
        const li = document.createElement('li');
        li.textContent = result;
        ul.appendChild(li);
    });
    resultsDiv.appendChild(ul);
}
