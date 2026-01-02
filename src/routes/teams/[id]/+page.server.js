
export async function load({params}) {
    const { id } =  params;

    let url = new URL(`http://localhost:8000/teams/${id}`)
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
    }
    let team = await response.json();
    const members = team.members_;
    let member;
    let pokemon_data = [];
    for (member of members){
        let pokemon_url = new URL(`http://localhost:8000/pokemons/${member.pokemon_id}`)
        const pokemon_response = await fetch(pokemon_url);
        if (!pokemon_response.ok) {
            throw new Error(`Error: ${pokemon_response.status}`);
        }
        let pokemon = await pokemon_response.json();

        pokemon_data.push({ member_id: member.id, pokemon: pokemon});
    }

    return {team, pokemon_data};
}
