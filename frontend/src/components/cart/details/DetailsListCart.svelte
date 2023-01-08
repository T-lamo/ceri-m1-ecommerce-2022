<script lang="ts">
	import DetailsCart from './DetailsCart.svelte';

	let arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5];
</script>

<div class="container">
	<ul class="container">
		{#each arr as item}
			<li>
				<DetailsCart />
			</li>
		{/each}
	</ul>
</div>

<style lang="scss" scoped>
	.container {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}
</style>
