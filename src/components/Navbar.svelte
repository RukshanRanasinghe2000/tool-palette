<script>
  import TopAppBar, { Row, Section } from '@smui/top-app-bar';
  import IconButton from '@smui/icon-button';
  import Button from '@smui/button';
  import { link } from 'svelte-spa-router';
</script>

<TopAppBar variant="static">
  <Row>
    <Section>
      <IconButton class="material-icons">menu</IconButton>
      <span class="title">WebP Converter</span>
    </Section>
    <Section align="end" toolbar>
      <a use:link href="/"><Button>Home</Button></a>
      <a use:link href="/about"><Button>About Us</Button></a>
      <a use:link href="/converter"><Button>Image Converter</Button></a>
    </Section>
  </Row>
</TopAppBar>

<style>
  .title {
    margin-left: 16px;
  }
  a {
    text-decoration: none;
    color: white;
  }
</style>