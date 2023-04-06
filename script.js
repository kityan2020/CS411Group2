const searchButton = document.querySelector('#search-button');
const searchInput = document.querySelector('#search-input');
const resultsDiv = document.querySelector('#results');

searchButton.addEventListener('click', async () => {
    const query = searchInput.value;
    const response = await fetch(`/api/search?q=${query}`);
    const data = await response.json();
    displayResults(data);
});

function displayResults(data) {
    const results = data.artists.items;
    resultsDiv.innerHTML = '';
    if (results.length === 0) {
        resultsDiv.textContent = 'No results found';
        return;
    }
    const ul = document.createElement('ul');
    results.forEach(result => {
        const li = document.createElement('li');
        li.textContent = result.name;
        ul.appendChild(li);
    });
    resultsDiv.appendChild(ul);
}
