<script>
  import { link } from 'svelte-spa-router';
</script>

<nav class="navbar">
  <div class="navbar-brand">
    <span class="title">ToolPalette</span>
  </div>
  <div class="navbar-menu">
    <a use:link href="/">Tools</a>
    <a use:link href="/about">About Us</a>
  </div>
</nav>

<style>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #333;
    color: white;
  }

  .navbar-brand {
    font-size: 1.5rem;
    font-weight: bold;
  }

  .title {
    margin-left: 16px;
  }

  .navbar-menu {
    display: flex;
    gap: 2rem;
  }

  a {
    text-decoration: none;
    color: white;
    transition: color 0.3s ease;
  }

  a:hover {
    color: #c41e3a;
  }
</style>