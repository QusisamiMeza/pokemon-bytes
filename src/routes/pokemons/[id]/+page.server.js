
export async function load({params}) {
    const { id } =  params;

    let url = new URL(`http://localhost:8000/pokemons/${id}`) 
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
    }
    let pokemon = await response.json();

    let url_pokemon_id_moves = new URL(`http://localhost:8000/pokemons/${id}/moves`)
    const response_pokemon_id_moves= await fetch(url_pokemon_id_moves);
    if (!response_pokemon_id_moves.ok) {
        throw new Error(`Error: ${response_pokemon_id_moves.status}`);
    }
    let moves_pokemon = await response_pokemon_id_moves.json();

    return {pokemon,moves_pokemon};
}
