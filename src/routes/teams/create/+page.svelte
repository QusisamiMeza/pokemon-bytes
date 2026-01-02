<script>
	import { BASE_URL } from '../../config.js';
	import TeamMemberForm from './TeamMemberForm.svelte';
	import './style_team_create.css';

	export let data;

	let name = '';
	let generation = '';
	let members = [];
	let error = '';
	let success = '';

	function handleAddMember(memberData) {
		members = [...members, memberData];
		success = '';
	}

	function removeMember(index) {
		members = members.filter((_, i) => i !== index);
	}

	$: if (name || generation || members.length > 0) {
		error = '';
		success = '';
	}

	// Submit the form data
	async function createTeam() {
		error = '';
		success = '';

		if (members.length === 0) {
			error = 'Please add at least one team member.';
			return;
		}

		const teamData = {
			name,
			generation: parseInt(generation),
			members
		};

		try {
			const response = await fetch(`${BASE_URL}/teams/`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(teamData)
			});

			if (response.ok) {
				success = 'Team created successfully!';
				name = '';
				generation = '';
				members = [];
			} else {
				const errorData = await response.json();
				error = 'Failed to create the team: ' + errorData.detail;
			}
		} catch (err) {
			error = 'An unexpected error occurred: ' + err.message;
		}
	}
</script>

<div class="team-fonts">
	<h1 class="team-header team-heading">Create Team</h1>

	<!-- Main Form -->
	<form class="team-member-form" on:submit|preventDefault={createTeam}>
		<!-- Team Name -->
		<label class="custom-label">
			Team Name:
			<input class="team-fonts custom-input" type="text" bind:value={name} required />
		</label>

		<!-- Generation -->
		<label class="custom-label">
			Generation:
			<select class="team-fonts custom-input" bind:value={generation} required>
				<option value="" disabled>Select a generation</option>
				{#each [...Array(8).keys()] as i}
					<option value={i + 1}>{i + 1}</option>
				{/each}
			</select>
		</label>

		<!-- Members List -->
		<h2 class="team-heading">Members</h2>
		{#if members.length > 0}
			<table class="member-list">
				<thead>
					<tr>
						<th>#</th>
						<th>Pokémon</th>
						<th>Moves</th>
						<th>Stats</th>
						<th>Nature</th>
						<th>Action</th>
					</tr>
				</thead>
				<tbody>
					{#each members as member, index}
						<tr>
							<td>{index + 1}</td>
							<td>{member.pokemon.identifier}</td>
							<td>{member.moves.join(', ')}</td>
							<td>
								<ul class="custom-ul">
									{#each Object.entries(member.stats) as [stat, value]}
										<li>{stat}: {value}</li>
									{/each}
								</ul>
							</td>
							<td>{member.nature}</td>
							<td>
								<button class="base-button remove-btn" on:click={() => removeMember(index)}>Remove</button>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		{:else}
			<p>No members added yet.</p>
		{/if}

		<!-- Error/Success Display -->
		{#if error}
			<p class="error">{error}</p>
		{/if}

		{#if success}
			<p class="success">{success}</p>
		{/if}

		<button class="base-button" type="submit">Create Team</button>
	</form>

	<!-- Add New Member Section -->
	<TeamMemberForm {data} onAddMember={handleAddMember} />
</div>
