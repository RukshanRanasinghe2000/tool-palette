<script></script>

<div class="about-container">
  <h1>About Us</h1>
  <p>
    We are a small team creating web tools to simplify image processing. Our goal is to provide
    efficient and user-friendly solutions for your daily web development and design needs.
  </p>
  <p>
    This Tool Palette project is built with Svelte and Material UI components,
    demonstrating modern web development practices.
  </p>
</div>

<style>
  .about-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    height: 100%;
    text-align: center;
    padding: 20px;
  }

  h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5em;
    color: var(--mdc-theme-primary, #6200ee);
  }

  p {
    font-size: 1.1rem;
    max-width: 700px;
    line-height: 1.6;
    margin-bottom: 1em;
  }

  /* Media queries for smaller screens */
  @media (max-width: 768px) {
    h1 {
      font-size: 2rem;
    }
    p {
      font-size: 1rem;
    }
  }

  @media (max-width: 480px) {
    h1 {
      font-size: 1.5rem;
    }
    p {
      font-size: 0.9rem;
    }
  }
</style>