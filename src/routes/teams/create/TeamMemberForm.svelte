<script>
	import { BASE_URL } from '../../config.js';
	import Typeahead from 'svelte-typeahead';
	import './style_team_create.css';

	// Props
	export let data;
	export let onAddMember;

	// State Variables
	let selectedPokemon = null;
	let nature = '';
	let moves = [];
	let availableMoves = [];
	let isLoadingMoves = false;
	let stats = {
		hp: 0,
		attack: 0,
		defense: 0,
		'special-attack': 0,
		'special-defense': 0,
		speed: 0,
		accuracy: 0,
		evasion: 0
	};
	let error = '';

	async function handlePokemonSelect({ detail }) {
		selectedPokemon = detail.original;
		moves = [];
		availableMoves = [];
		isLoadingMoves = true;

		try {
			availableMoves = await fetchAvailableMoves(selectedPokemon.id);
		} catch (err) {
			error = `Error fetching moves: ${err.message}`;
		} finally {
			isLoadingMoves = false;
		}
	}

	async function fetchAvailableMoves(pokemonId) {
		if (!pokemonId) {
			error = 'Invalid Pokémon ID';
			return [];
		}

		try {
			const response = await fetch(`${BASE_URL}/pokemons/${pokemonId}/moves`);

			if (!response.ok) {
				throw new Error(`Failed to fetch moves for Pokémon ID ${pokemonId}`);
			}

			const movesData = await response.json();
			const allMoves = [
				...(movesData['MOVES LEARNT BY LEVEL UP'] || []),
				...(movesData['MOVES LEARNT BY TIME MACHINES'] || []),
				...(movesData['MOVES LEARNT ACCORDING TO EGG GROUP'] || [])
			];

			// Remove duplicates
			return [...new Set(allMoves)];
		} catch (err) {
			error = `Error fetching moves: ${err.message}`;
			return [];
		}
	}

	function handleNatureSelect({ detail }) {
		nature = detail.original.identifier;
	}

	function handleMoveSelect({ detail }) {
		const selectedMove = detail.original.toLowerCase();

		if (moves.length >= 4) {
			error = 'You can only select up to 4 moves!';
			return;
		}

		if (!moves.includes(selectedMove)) {
			moves = [...moves, selectedMove];
			error = '';
		} else {
			error = 'Move already selected!';
		}
	}

	function removeMove(move) {
		moves = moves.filter((m) => m !== move);
		error = '';
	}

	function addMember() {
		if (!selectedPokemon) {
			error = 'Please select a Pokémon.';
			return;
		}

		if (!nature) {
			error = 'Please select a nature.';
			return;
		}

		// Validate stats
		const totalStats = Object.values(stats).reduce((sum, value) => sum + value, 0);
		const isInvalidStat = Object.values(stats).some(
			(value) => value < 0 || value > 255 || isNaN(value)
		);

		if (isInvalidStat) {
			error = 'Each stat must be between 0 and 255.';
			return;
		}

		if (totalStats > 510) {
			error = 'Total stats cannot exceed 510.';
			return;
		}

		error = '';

		const memberData = {
			pokemon: selectedPokemon,
			pokemon_id: selectedPokemon.id,
			nature,
			moves: [...moves],
			stats: { ...stats }
		};

		onAddMember(memberData);
		error = '';

		// Reset form
		selectedPokemon = null;
		nature = '';
		moves = [];
		availableMoves = [];
		stats = {
			hp: 0,
			attack: 0,
			defense: 0,
			'special-attack': 0,
			'special-defense': 0,
			speed: 0,
			accuracy: 0,
			evasion: 0
		};
	}
</script>

<div class="team-member-form team-fonts">
	<h3 class="team-heading">Add New Member</h3>

	<!-- Pokémon Selection -->
	<label class="custom-label">
		Pokémon:
		<div class="typeahead-container">
			<Typeahead
				class="typeahead"
				data={data.pokemons}
				extract={(pokemon) => pokemon.identifier}
				hideLabel={true}
				on:select={handlePokemonSelect}
				placeholder="Search Pokémon..."
				inputAfterSelect="clear"
			/>
		</div>
	</label>

	{#if selectedPokemon}
		<div>
			<h4 class="team-heading">Selected Pokémon: {selectedPokemon.identifier}</h4>

			<!-- Nature Selection -->
			<label class="custom-label">
				Nature:
				<div class="typeahead-container">
					<Typeahead
						data={data.natures}
						extract={(nature) => nature.identifier}
						on:select={handleNatureSelect}
						hideLabel={true}
						placeholder="Search and select nature..."
						inputAfterSelect="clear"
					/>
				</div>
			</label>

			<!-- Nature Display -->
			{#if nature}
				<h4 class="team-heading">Selected Nature: {nature}</h4>
			{/if}

			<!-- Moves Selection -->
			<label class="custom-label">
				Moves:
				{#if isLoadingMoves}
					<p>Loading moves...</p>
				{:else if availableMoves.length > 0}
					<div class="typeahead-container">
						<Typeahead
							data={availableMoves}
							on:select={handleMoveSelect}
							hideLabel={true}
							placeholder="Search and select moves..."
							inputAfterSelect="clear"
						/>
					</div>
				{:else}
					<p>No moves available for this Pokémon.</p>
				{/if}
			</label>

			<!-- Move Display -->
			{#if moves.length > 0}
				<ul class="custom-ul move-selection-list">
					{#each moves as move}
						<li>
							{move}
							<button class="base-button remove-btn" on:click={() => removeMove(move)}>Remove</button>
						</li>
					{/each}
				</ul>
			{/if}

			<!-- Stats Selection -->
			<h4 class="team-heading">Set Stats</h4>
			<div class="stats-grid">
				{#each Object.keys(stats) as stat}
					<div class="stat-item">
						<label class="custom-label">
							{stat.replace('-', ' ').toUpperCase()}:
							<input class="custom-input" type="number" min="0" max="255" bind:value={stats[stat]} />
						</label>
					</div>
				{/each}
			</div>

			<!-- Error/Success Display -->
			{#if error}
				<p class="error">{error}</p>
			{/if}

			<button class="base-button" on:click={addMember}>Add Member</button>
		</div>
	{/if}
</div>
