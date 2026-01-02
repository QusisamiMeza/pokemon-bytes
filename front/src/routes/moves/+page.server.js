export async function load() {

   let url = new URL('http://localhost:8000/moves/')
   const response = await fetch(url);
   if (!response.ok) {
       throw new Error(`Response status: ${response.status}`);
   }

   let moves = await response.json();

   return {
       moves: moves
   };
}
