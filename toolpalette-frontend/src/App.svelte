<script>
  import Router from "svelte-spa-router";
  import Navbar from "./components/Navbar.svelte";
  import Footer from "./components/Footer.svelte";

  import About from "./routes/About.svelte";
  import ImageConverter from "./routes/ImageConverter.svelte";

  const routes = {
    "/": ImageConverter,
    "/about": About
  };
</script>

<div class="app-container">
  <Navbar />

  <main class="content-area">
    <div class="responsive-container">
      <Router {routes} />
    </div>
  </main>
  <Footer />

</div>

<style>
  :global(body) {
    font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    
  }

  .app-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  .content-area {
    flex-grow: 1; 
    display: flex;
    justify-content: center; 
    align-items: flex-start; 
    overflow-y: auto; 
    background-color: #F9F9F9;
  }

  .responsive-container {
    width: 100%;
     
    margin: 0 auto; 
  }

  @media (min-width: 768px) {
    .content-area {
    }
  }
</style>