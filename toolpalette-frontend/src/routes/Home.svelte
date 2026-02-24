<script></script>

<div class="home-container">
  <h1>Welcome to Our WebP Converter</h1>
  <p>Convert your images to WebP easily.</p>
</div>

<style>
  .home-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%; /* Take full height of its parent (content-area) */
    text-align: center;
    padding: 20px;
  }

  h1 {
    font-size: 2.5rem; /* Responsive font size */
    margin-bottom: 0.5em;
    color: var(--mdc-theme-primary, #6200ee); /* Use SMUI primary color if defined */
  }

  p {
    font-size: 1.2rem; /* Responsive font size */
    max-width: 600px;
    line-height: 1.5;
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