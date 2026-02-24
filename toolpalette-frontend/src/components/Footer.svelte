<script>
  import { link } from "svelte-spa-router";
</script>

<footer class="app-footer">
  <div class="footer-container">
    <!-- Left -->
    <div class="footer-left">
      <nav class="footer-nav">
        <a use:link href="/">Tools</a>
        <a use:link href="/about">About Us</a>
      </nav>
    </div>

    <!-- Center -->
    <div class="footer-center">
      <p>© {new Date().getFullYear()} Rukshan Ranasinghe</p>
    </div>

    <!-- Right -->
    <div class="footer-right">
      <p>
        Contact:
        <a href="mailto:navodrukshan2000@gmail.com">
          navodrukshan2000@gmail.com
        </a>
      </p>
    </div>
  </div>
</footer>

<style>
  .app-footer {
    width: 100%;
    background-color: #f2f2f2;
    padding: 20px 0;
  }

  .footer-container {
    max-width: 1140px;
    margin: 0 auto;
    padding: 0 20px;

    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
  }

  .footer-left,
  .footer-center,
  .footer-right {
    font-size: 0.95rem;
    color: #333;
  }

  .footer-right a {
    text-decoration: none;
    font-weight: 500;
    color: #333;
  }

  .footer-right a:hover {
    text-decoration: underline;
    color: #c41e3a;
  }

  .footer-nav {
    display: flex;
    gap: 20px;
  }

  .footer-nav a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
  }

  .footer-nav a:hover {
    color: #c41e3a;
  }

  @media (max-width: 768px) {
    .footer-container {
      flex-direction: column;
      text-align: center;
    }
  }
</style>
