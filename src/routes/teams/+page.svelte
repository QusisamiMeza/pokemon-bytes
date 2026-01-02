<script>
    import { goto } from '$app/navigation';
    import Typeahead from 'svelte-typeahead';
    import './style_teams.css'

    let currentPage = 0;
    const pageSize = 10;
    let data = [];
    
    async function fetchTeams(page) {
        let url = new URL(`http://localhost:8000/teams/`)
        url.searchParams.set('page', page);
        url.searchParams.set('page_size', pageSize);
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        data = await response.json();
    }

    function handleTeamSelect({ detail }) {
        goto(`/teams/${detail.original.id}`);
    }

    function nextPage() {
        let dataLength = data.length;
        if(dataLength === pageSize){
            currentPage += 1;
            fetchTeams(currentPage);
        }
    }

    function previousPage() {
        if(currentPage > 0){
            currentPage -= 1;
            fetchTeams(currentPage);
        }
    }

    async function deleteTeam(teamId) {
        const url = `http://localhost:8000/teams/${teamId}`;
        try {
            const response = await fetch(url, {
                method: 'DELETE',
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            fetchTeams(currentPage);
        } catch (error) {
            alert(`Error: ${error.message}`);
        }
    }

    fetchTeams(currentPage);
</script>

<div >
    <main class="page-teams">
        <h1 class="team-tittle">Teams</h1>
        <Typeahead
                class="typeahead team-search"
                data={data}
                extract={(data) => data.name}
                hideLabel={true}
                on:select={handleTeamSelect}
                placeholder="Search Team..."
            />
        <div class="team-conteiner">
            <div class="list-teams">
            {#each data as team}
                <div class="team-box">
                    <div class="id-box">
                        ID: #{team.id}
                        <button class="button-delete" on:click={deleteTeam(team.id)}>x</button>
                    </div>
                    
                    <div class="members-box">
                        {#each team.members as member}
                            ‣ {member} 
                        {/each}
                    </div>
                    <a href="teams/{team.id}" class="team-name">{team.name}</a>
                </div> 
            {/each}
            </div>  
            <a href="/teams/create" class="create-team-link">ADD A NEW TEAM +</a> 
        </div>  
        <div class="pagination">
            <button class="button-page" on:click={previousPage}>
                ◄
            </button>
            <button class="button-page" on:click={nextPage}>
                ▶
            </button>
        </div>
    </main>
</div>