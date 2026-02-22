<script>
  import Router from "svelte-spa-router";
  import Navbar from "./components/Navbar.svelte";

  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";
  import ImageConverter from "./routes/ImageConverter.svelte";

  const routes = {
    "/": Home,
    "/about": About,
    "/converter": ImageConverter
  };
</script>

<Navbar />

<main>
  <Router {routes} />
</main>

<style>
  main {
    padding: 20px;
  }
</style>