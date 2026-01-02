<script>
   export let data;
   import './style_moves.css';
</script>

<div class="page_moves_id">
    <h1>{data.move.name}</h1>
    <h2 class="aclaracion_titulo">~ Move ~</h2>
    <h2>MOVE DATA</h2>
    <table class="table_move_data">
        <tbody>
            <tr class="fila_par">
                <th>ID</th>
                <td>{data.move.id}</td>
            </tr>
            <tr class="fila_impar">
                <th>Name</th>
                <td>{data.move.name}</td>
            </tr>
            <tr class="fila_par">
                <th>Type</th>
                <td>{data.move.move_type}</td>
            </tr>
            <tr class="fila_impar">
                <th>Power</th>
                <td>{data.move.power}</td>
            </tr>
            <tr class="fila_par">
                <th>Accuracy</th>
                <td>{data.move.accuracy}</td>
            </tr>
            <tr class="fila_impar">
                <th>Power Points</th>
                <td>{data.move.power_points}</td>
            </tr>
            <tr class="fila_par">
                <th>Generation</th>
                <td>{data.move.generation}</td>
            </tr>
            <tr class="fila_impar">
                <th>Category</th>
                <td>{data.move.category}</td>
            </tr>
            <tr class="fila_par">
                <th>Effect</th>
                <td>{data.move.effect}</td>
            </tr>  
        </tbody>
    </table>
    <br>
    <br>
    <h2>POKEMONS THAT CAN LEARN THIS MOVE</h2>
    <p>Click on a Pokemon's name to see more details about it!</p>
    <table class="table_move_pokemons">
        <thead>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>IMAGE</th>
                <th>TYPES</th>
            </tr>
        </thead>
        <tbody>
            {#each data.move_pokemons as move_pokemon}
                <tr>
                    <td>{move_pokemon.id}</td>
                    <td><a href="/pokemons/{move_pokemon.id}">{move_pokemon.identifier}</a></td>
                    <td><img src="{move_pokemon.image}" alt=""/></td>
                    <td>
                        <ul>
                            {#each move_pokemon.types as type}
                                <li style="text-align: left;">{type}</li>
                            {/each}
                        </ul>
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>