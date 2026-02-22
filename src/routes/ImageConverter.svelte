<script>
  let file;
  let previewUrl = null;
  let webpUrl = null;
  let loading = false;

  function handleFile(event) {
    file = event.target.files[0];
    previewUrl = URL.createObjectURL(file);
    webpUrl = null;
  }

  async function convertToWebP() {
    if (!file) {
      alert("Please select an image first");
      return;
    }

    loading = true;

    const formData = new FormData();
    formData.append("image", file);

    const response = await fetch("YOUR_API_URL_HERE", {  // Replace with Choreo API URL
      method: "POST",
      body: formData
    });

    const blob = await response.blob();
    webpUrl = URL.createObjectURL(blob);
    loading = false;
  }
</script>

<style>
  .converter {
    text-align: center;
  }
  img {
    max-width: 100%;
    margin-top: 10px;
  }
  button {
    padding: 10px 16px;
    margin-top: 10px;
  }
</style>

<div class="converter">
  <h2>Image → WebP Converter</h2>

  <input type="file" accept="image/*" on:change={handleFile} />

  {#if previewUrl}
    <h3>Original Image</h3>
    <img src={previewUrl} alt="preview" />
  {/if}

  <br />
  <button on:click={convertToWebP} disabled={loading}>
    {loading ? "Converting..." : "Convert to WebP"}
  </button>

  {#if webpUrl}
    <h3>WebP Image</h3>
    <img src={webpUrl} alt="webp" />
    <br />
    <a href={webpUrl} download="converted.webp">Download WebP</a>
  {/if}
</div>