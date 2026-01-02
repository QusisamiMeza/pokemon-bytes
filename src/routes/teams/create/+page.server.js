import { BASE_URL } from '../../config.js';
import { error } from '@sveltejs/kit';

export async function load() {
	// Fetch pokemons
	const pokemonResponse = await fetch(`${BASE_URL}/pokemons/`);
	if (!pokemonResponse.ok) {
		throw error(pokemonResponse.status, 'Failed to fetch Pokémon data.');
	}
	const pokemons = await pokemonResponse.json();

	// Fetch natures
	const naturesResponse = await fetch(`${BASE_URL}/teams/natures`);
	if (!naturesResponse.ok) {
		throw new Error('Failed to fetch natures');
	}
	const natures = await naturesResponse.json();

	return { pokemons: pokemons, natures: natures };
}
