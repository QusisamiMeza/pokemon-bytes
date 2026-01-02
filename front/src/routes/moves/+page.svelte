<script>
    import { goto } from '$app/navigation';
    import Typeahead from 'svelte-typeahead';
    export let data;
    import './[id]/style_moves.css';

    function handleMoveSelect({ detail }) {
        goto(`/moves/${detail.original.id}`);
    }
</script>

<div class="page_moves">
    <h1>MOVES</h1>
    <Typeahead
        class="typeahead move-search"
        data={data.moves}
        extract={(moves) => moves.name}
        hideLabel={true}
        on:select={handleMoveSelect}
        placeholder="Search Move..."
    />
    <p>
        This is a full list of every <i>Pokemon move</i>.
        The ID, power, accuracy and power points are listed below.<br>
        Click a move name to see even more detailed information, including which Pokemon can learn that move.
    </p>
    <br><br>
    <table class="table_moves">
        <thead>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>POWER</th>
                <th>ACCURACY</th>
                <th>POWER POINTS</th>
            </tr>
        </thead>
        <tbody>
            {#each data.moves as move}
                <tr>
                    <td>{move.id}</td>
                    <td><a href="moves/{move.id}">{move.name}</a></td>
                    <td>{move.power}</td>
                    <td>{move.accuracy}</td>
                    <td>{move.power_points}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>