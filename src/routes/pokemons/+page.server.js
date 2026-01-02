export async function load() {

    let url = new URL(`http://localhost:8000/pokemons/`)
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
    }
    let pokemons = await response.json();
    return {
        pokemons: pokemons
    };
}