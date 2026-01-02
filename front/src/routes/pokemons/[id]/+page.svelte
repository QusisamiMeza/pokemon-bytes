
<script> 
    import './style.css'
    export let data;
 </script>

<div class="page-pokemon">
    <main>
        <h1 class = "name">{data.pokemon.identifier}</h1>
        <div class = "bloque1">
            <img class="pokemon-img" src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${data.pokemon.id}.png`} alt={data.pokemon.identifier} />
            <table class = "tabla">
                <tbody>
                    <tr>
                        <td>ID</td>
                        <td>{data.pokemon.id}</td>
                    </tr>
                    <tr>
                        <td>Height</td>
                        <td>{data.pokemon.height} decimeters</td>
                    </tr>
                    <tr>
                        <td>Weight</td>
                        <td>{data.pokemon.weight} hectogrammes </td>
                    </tr>
                    <tr>
                        <td>Types</td>
                        <td>{data.pokemon.types}</td>
                    </tr>
                    <tr>
                        <td>Abilities</td>
                        <td>{data.pokemon.abilities}</td>
                    </tr>
                    <tr>
                        <td>Egg Groups</td>
                        <td>{data.pokemon.egg_groups}</td>
                    </tr>
                </tbody>
            </table>
            
        </div>
        <div class = "bloque2">
            <table class = "tabla-stat">
                <tbody>
                    <tr>
                        <td>HP</td>
                        <td>{data.pokemon.stats.hp}</td>
                    </tr>
                    <tr>
                        <td>Attack</td>
                        <td>{data.pokemon.stats.attack}</td>
                    </tr>
                    <tr>
                        <td>Defense</td>
                        <td>{data.pokemon.stats.defense}</td>
                    </tr>
                    <tr>
                        <td>Special Attack</td>
                        <td>{data.pokemon.stats['special-attack']}</td>
                    </tr>
                    <tr>
                        <td>Special Defense</td>
                        <td>{data.pokemon.stats['special-defense']}</td>
                    </tr>
                    <tr>
                        <td>Speed</td>
                        <td>{data.pokemon.stats.speed}</td>
                    </tr>
                    <tr>
                        <td>Total</td>
                        <td>{data.pokemon.stats.total}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="bloque3">
            <table class= "tabla-moves">
                <thead>
                    <tr>
                        <th colspan="3"><strong class = "name">{data.pokemon.identifier}</strong>'s moves</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class ="titulos">Moves learnt by level up</td>
                        <td class ="titulos">Moves learnt by time machines</td>
                        <td class ="titulos">Moves learnt according to egg group</td>
                    </tr>
                    <tr class = "fila-moves">
                        <td>
                            {#if data.moves_pokemon["MOVES LEARNT BY LEVEL UP"] && data.moves_pokemon["MOVES LEARNT BY LEVEL UP"].length > 0}
                                {#each data.moves_pokemon["MOVES LEARNT BY LEVEL UP"] as move_level_up}
                                    <div>{move_level_up}</div>
                                {/each}
                            {:else}
                                <div>No moves available</div>
                            {/if}
                        </td>
                        <td>
                            {#if data.moves_pokemon["MOVES LEARNT BY TIME MACHINES"] && data.moves_pokemon["MOVES LEARNT BY TIME MACHINES"].length > 0}
                                {#each data.moves_pokemon["MOVES LEARNT BY TIME MACHINES"] as move_time_machine}
                                    <div>{move_time_machine}</div>
                                {/each}
                            {:else}
                                <div>No moves available</div>
                            {/if}
                        </td>
                        <td>
                            {#if data.moves_pokemon["MOVES LEARNT ACCORDING TO EGG GROUP"] && data.moves_pokemon["MOVES LEARNT ACCORDING TO EGG GROUP"].length > 0}
                                {#each data.moves_pokemon["MOVES LEARNT ACCORDING TO EGG GROUP"] as move_egg_group}
                                    <div>{move_egg_group}</div>
                                {/each}
                            {:else}
                                <div>No moves available</div>
                            {/if}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
</div>
