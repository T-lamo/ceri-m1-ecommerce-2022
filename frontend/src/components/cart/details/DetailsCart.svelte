<script lang="ts">
	let image: string =
		'https://images.unsplash.com/photo-1603884574615-7b6ec4198a8c?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzNDF8fG1vdmllfGVufDB8fHx8MTY2ODY0MjgyMQ&ixlib=rb-4.0.3&w=500&h=1000';
</script>

<div class="container">
	<div class="image" style="background-image: url({image})" />
	<div class="main">
		<h2>Nom du produit</h2>
		<div class="line" />
		<div class="description">
			<h3>Description</h3>
			<p>
				Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste dignissimos non quo quisquam
				ipsa nostrum ab aspernatur laudantium doloribus ex omnis obcaecati eos nam mollitia unde
				quaerat, quia laborum porro.
			</p>
		</div>
		<div class="line" />
		<div class="price">
			<span class="btn btn-primary">$25</span>
			<div>
				<i class="fa-solid fa-plus" />
				<span class="btn btn-primary">2</span>

				<i class="fa-solid fa-minus" />
			</div>
			<span class="btn btn-primary">50</span>
		</div>
		<div class="line" />
		<div class="icons">
			<span><i class="fa-solid fa-heart" /></span>
			<div>
				<span><i class="fa-solid fa-trash" /></span>
				<span><i class="fa-sharp fa-solid fa-pen" /> </span>
			</div>
		</div>
	</div>
</div>

<style lang="scss" scoped>
	.container {
		background: var(--gray-1);
		padding: 1rem;
		display: grid;
		grid-template-columns: 200px 1fr;
		height: max-content;
		gap: 1rem;
		.image {
			height: 200px;
			align-self: center;
		}
		.main {
			display: flex;
			flex-direction: column;
			gap: 1rem;
			align-self: center;
			.price {
				display: flex;
				justify-content: space-between;
				span {
					font-size: 1.5rem;
					padding: 1rem;
				}
			}

			.icons {
				display: flex;
				justify-content: space-between;
			}
		}

		i {
			color: var(--primary-1);
			padding: 1rem;
		}
		i:hover {
			color: var(--primary-2);
		}
	}
</style>
