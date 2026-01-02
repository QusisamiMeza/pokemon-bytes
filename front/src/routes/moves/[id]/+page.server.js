import { error } from '@sveltejs/kit';

export async function load({ params }) {
   let url_move = new URL(`http://localhost:8000/moves/${params.id}`)
   const response_move = await fetch(url_move);
   if (!response_move.ok) {
       throw error(response_move.status)
   }

   let move = await response_move.json();

   let url_move_id_pokemon = new URL(`http://localhost:8000/moves/${params.id}/pokemons`)
   const response_move_id_pokemon = await fetch(url_move_id_pokemon);
   if (!response_move_id_pokemon.ok) {
       throw error(response_move_id_pokemon.status)
   }

   let move_pokemons = await response_move_id_pokemon.json();

   return {
       move,
       move_pokemons
   };
}
