<script>
    import './style.css'
    export let data;

</script>

<div class="page-team-id">
    <main>
        <div class = "bloque1">
            <h1 class="name">{data.team.name}</h1>
            <table class = "tabla-team">
                <tbody>
                    <tr>
                        <td>ID</td>
                        <td>{data.team.id}</td>
                    </tr>
                    <tr>
                        <td>Generation</td>
                        <td>{data.team.generation}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <table class = "tabla-members">
            <thead>
                <tr>
                    <th colspan="6">Members information</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class = "titulos">ID</td>
                    <td class = "titulos">Image</td>
                    <td class = "titulos">Name</td>
                    <td class = "titulos">Nature</td>
                </tr>
                {#each data.team.members_ as member}
                {#each data.pokemon_data as pokemon_info}
                    <tr>
                        <td>{member.id}</td>
                        <td><img class="pokemon-img" src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${member.pokemon_id}.png`} alt={member.pokemon_id} /></td>
                        <td class = "name">{pokemon_info.pokemon.identifier}</td>
                        <td>{member.nature}</td>
                    </tr>
                {/each}
                {/each}
            </tbody>
        </table>
    </main>
</div>

