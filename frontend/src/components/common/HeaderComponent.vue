<script lang="ts"></script>

<template>
  <div class="container">
    <div class="header">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- hide-xl-lg -->
      <ul class="hamberger hide-xl-lg">
        <li>
          <i class="fa-solid fa-bars hamberger" />
        </li>
      </ul>

      <h2 class="logo">
        <a class="logo-txt" href="/"> Vinyl</a>
      </h2>
      <form class="search hide-xs">
        <i class="fa-solid fa-magnifying-glass" />
        <input
          bind:value="{search_value}"
          type="text"
          placeholder="Recherche"
        />
      </form>
      <ul>
        <li>
          <a href="/cart">
            <div class="cart_qty">
              <!-- <span class="qty">{product_qty}</span> -->
              <i class="fa-solid fa-cart-shopping" />
            </div>
          </a>
        </li>
        <li>
          <i class="fa-solid fa-user" />
        </li>
        <li>
          <a href="/places">
            <i class="fa-sharp fa-solid fa-map-location" />
          </a>
          <!-- <i class="fa-solid fa-house" /> -->
        </li>
        <li>
          <i class="fa-solid fa-right-to-bracket" />
        </li>

        <!-- <li>
				<i class="fa-solid fa-right-from-bracket" />
			</li> -->
      </ul>
    </div>
    <form class="ctn-search hide-xl-lg-md-sm">
      <i class="fa-solid fa-magnifying-glass" />
      <input
        bind:value="{search_value}"
        id="search"
        type="text"
        placeholder="Recherche"
      />
    </form>
  </div>
</template>

<style lang="scss" scoped>
@use "./../../assets/scss/mixin" as mixin;

.container {
  position: sticky;
  top: 0px;
  display: flex;
  flex-direction: column;
  background: var(--gray-2);
  .header {
    display: flex;
    background: var(--primary-1);
    justify-content: space-between;
    flex: 1fr;

    border-bottom: 1px solid var(--primary-2);
    padding-left: 1rem;
    flex: 1fr;

    .logo {
      font-size: 1.8rem;
      margin-bottom: 0;
      display: flex;
      flex-flow: row nowrap;
      align-items: center;
      justify-content: center;
      a {
        font-size: 2rem;
        color: var(--gray-1);
        font-family: "Liu Jian Mao Cao", cursive;
        align-self: center;
        cursor: pointer;
      }
    }
    .search {
      display: flex;
      flex-flow: row nowrap;
      align-self: center;
      max-width: 500px;

      i {
        align-self: center;
        margin-left: 1rem;
      }

      input {
        background: var(--gray-1);
        min-width: 400px;
        padding: 0.8rem;
        margin: 0.5rem 0rem;
        color: var(--text-color);
        font-size: 1.2rem;
        outline: none;
        border: 0;
        border-bottom: 1px solid var(--gray-1);
        border-radius: 4px;
      }
      input:hover {
        border-bottom: 2px solid var(--gray-2);
      }
      ul {
        display: flex;
        align-items: center;
        li {
          align-self: center;
        }
      }
    }

    ul {
      display: flex;
      flex-flow: row nowrap;
    }
    ul li {
      padding: 0.4rem 0.4rem;
      color: var(--gray-1);
      margin-right: 0.8rem;
    }

    ul li a:hover {
      color: var(--gray-1);
    }
    i:hover {
      color: var(--gray-2);
    }
    a {
      color: white;
    }
    .cart_qty {
      position: relative;
      .qty {
        position: fixed;
        color: var(--gray-1);
        background-color: red;
        position: fixed;
        border-radius: 50%;
        padding: 2px;
      }
    }
  }

  .ctn-search {
    display: flex;
    margin: 1rem;
    height: 60px;
    width: auto;
    align-self: center;
    i {
      align-self: center;
      margin-left: 1rem;
      font-size: 2rem;
    }
    input {
      padding: 2rem;
      color: var(--gray-3);
      font-size: 2rem;
      outline: none;
      border: 0;
      border: 1px solid var(--gray-1);
    }
    input:hover {
      border: 2px solid var(--gray-1);
    }
  }
}

@include mixin.xs {
}
</style>
