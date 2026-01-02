
<script>
    import { goto } from '$app/navigation';
    import Typeahead from 'svelte-typeahead';
    export let data;
    import './style_pokemons.css'

    function handlePokemonSelect({ detail }) {
        goto(`/pokemons/${detail.original.id}`);
    }
</script>

<div class="page-pokemons">
    <main class="main">
        <h1>List of Pokemons</h1>
        <Typeahead
            class="typeahead pokemon-search"
            data={data.pokemons}
            extract={(pokemons) => pokemons.identifier}
            hideLabel={true}
            on:select={handlePokemonSelect}
            placeholder="Search Pokemon..."
        />
        <div class="info-box">Click on a Pokémon's name to see its details.</div>
        <div class="list-pokemon">
            {#each data.pokemons as pokemon}
                <div class="pokemon-box">
                    <small class="pokemon-id">#{pokemon.id}</small>
                    <a href="pokemons/{pokemon.id}" class="pokemon-name">{pokemon.identifier}</a> 
                    <img class="pokemons-img" src={pokemon.image} alt="{pokemon.identifier}" />
                    <div class="pokemon-type">
                        ⊲
                        {#each pokemon.types as type}
                            <small>{type}</small>
                        {/each}
                        ⊳
                    </div>
                </div>
            {/each}
        </div>
    </main>
</div>

