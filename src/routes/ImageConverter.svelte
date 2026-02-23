<script>
  let file = $state(null);
  let previewUrl = $state(null);
  let convertedUrl = $state(null);

  let fromFormats = ["WEBP"];
  let toFormats = ["PNG", "JPG", "WEBP", "GIF", "AVIF"];

  let fromFormat = $state("WEBP");
  let toFormat = $state("PNG");
  let fileInput;

  function handleFileUpload(event) {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      file = selectedFile;
      previewUrl = URL.createObjectURL(file);
      convertedUrl = null;
    }
  }

  async function convertImage() {
    if (!file) return alert("Please upload an image");

    const img = new Image();
    img.src = previewUrl;

    await new Promise((resolve) => (img.onload = resolve));

    const canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    const mime = `image/${toFormat.toLowerCase()}`;

    canvas.toBlob(
      (blob) => {
        convertedUrl = URL.createObjectURL(blob);
      },
      mime,
      0.9,
    );
  }

  function removeFile() {
    file = null;
    previewUrl = null;
    convertedUrl = null;
  }
</script>

<div class="image-converter-container">
  <!-- HERO SECTION -->
  <div class="hero-div">
    <div class="hero-section">
      <div class="hero-left">
        <h1>WEBP Converter</h1>
        <p>
          Convert your WEBP images to PNG, JPG, PDF, AVIF and more formats
          online.
        </p>
      </div>

      <div class="hero-right">
        <span>convert</span>

        <select bind:value={fromFormat} style="width:120px;">
          {#each fromFormats as format}
            <option value={format}>{format}</option>
          {/each}
        </select>

        <span>to</span>

        <select bind:value={toFormat} style="width:120px;">
          {#each toFormats as format}
            <option value={format}>{format}</option>
          {/each}
        </select>
      </div>
    </div>
  </div>

  <br />

  <!-- CONVERTER CARD -->
  <div class="converter-card">
    <input
      type="file"
      accept="image/*"
      bind:this={fileInput}
      onchange={(e) => handleFileUpload(e)}
      style="display: none"
    />
    {#if !file}
      <button class="select-file-btn icon-btn" onclick={() => fileInput?.click()}>
        <i class="fa-solid fa-file"></i>Select File
      </button>
    {/if}

    {#if file}
  <div class="file-info">
    <span class="file-icon">
      <i class="fa-solid fa-file"></i>
    </span>
    <span class="file-name">{file.name}</span>

    <button
      class="remove-btn"
      onclick={removeFile}
      aria-label="Remove selected file"
      title="Remove file"
    >
      <i class="fa-solid fa-xmark"></i>
    </button>
  </div>
{/if}

    <br />

    {#if file}
      <button class="icon-btn" onclick={() => convertImage()}><i class="fa fa-sync-alt mr-1"></i>Convert</button>
    {/if}

    {#if convertedUrl}
      <div class="result">
        <h3>Converted Image</h3>
        <img src={convertedUrl} alt="Converted" />
        <br />
        <a href={convertedUrl} download={"converted." + toFormat.toLowerCase()}>
          <button>Download</button>
        </a>
      </div>
    {/if}
  </div>

  <div class="info-sections-wrapper">
    <div class="two-column-cards">
      <section class="info-section card">
        <h2>About This WEBP Converter</h2>
        <p class="intro-text">
          Our WEBP Converter allows you to convert your image files online.
          Amongst many others, we support PNG, JPG, GIF, WEBP and HEIC. You will
          soon be able to use options to control image resolution, quality and
          file size.
        </p>
      </section>

      <section class="info-section card">
        <h2>What is WebP?</h2>
        <p>
          WebP ("weppy") is a modern
          <strong
            >image format that provides superior lossless and lossy compression
            for images on the web.</strong
          >
          It was developed by Google, based on acquired technology of On2.
        </p>
      </section>
    </div>

    <section class="info-section">
      <h2>Supported Conversions</h2>
      <div class="conversion-lists">
        <section class="card list-column" style="max-height: 246px;">
          <h3>Convert From WEBP</h3>
          <ul style="columns:3; -webkit-columns:3; -moz-columns:3;">
            <li>WEBP to PDF</li><li>WEBP to AVIF</li><li>WEBP to BMP</li><li>WEBP to EPS</li><li>WEBP to GIF</li>
            <li>WEBP to ICO</li><li>WEBP to JPG</li><li>WEBP to ODD</li><li>WEBP to PNG</li><li>WEBP to PS</li>
            <li>WEBP to PSD</li><li>WEBP to TIFF</li><li>WEBP to WEBP</li>
          </ul>
        </section>
        <section class="card list-column">
          <h3>Convert To WEBP</h3>
          <ul style="columns:3; -webkit-columns:3; -moz-columns:3;">
            <li>3FR to WEBP</li><li>ARW to WEBP</li><li>AVIF to WEBP</li><li>BMP to WEBP</li>
            <li>CR2 to WEBP</li><li>CR3 to WEBP</li><li>CRW to WEBP</li><li>DCR to WEBP</li><li>DNG to WEBP</li>
            <li>EMF to WEBP</li><li>EPS to WEBP</li><li>ERF to WEBP</li><li>GIF to WEBP</li><li>HEIC to WEBP</li>
            <li>HEIF to WEBP</li><li>ICO to WEBP</li><li>JFIF to WEBP</li><li>JPEG to WEBP</li>
            <li>JPG to WEBP</li><li>MOS to WEBP</li><li>MRW to WEBP</li><li>NEF to WEBP</li><li>ODD to WEBP</li>
            <li>ORF to WEBP</li><li>PDF to WEBP</li><li>PEF to WEBP</li><li>PNG to WEBP</li>
            <li>PPM to WEBP</li><li>PS to WEBP</li><li>PSB to WEBP</li><li>PSD to WEBP</li><li>RAF to WEBP</li>
            <li>RAW to WEBP</li><li>RW2 to WEBP</li><li>SVG to WEBP</li><li>SVGZ to WEBP</li><li>TGA to WEBP</li>
            <li>TIF to WEBP</li><li>TIFF to WEBP</li><li>WEBP to WEBP</li><li>X3F to WEBP</li><li>XCF to WEBP</li>
            <li>XPS to WEBP</li>
          </ul>
        </section>
      </div>
    </section>

    <div class="two-column-cards">
      <section class="info-section card">
        <h2>Data Security</h2>
        <p>
          We prioritize your privacy and data security. Files processed through
          our converter are handled with utmost care. We do not store your files
          longer than necessary for conversion and download. No one except you
          will ever have access to your files.
        </p>
      </section>

      <section class="info-section card">
        <h2>High-Quality Conversions</h2>
        <p>
          Utilizing robust open-source software, our goal is to provide the best
          possible conversion results. Most conversion types will soon be
          adjustable to your needs such as setting the quality and many other
          options.
        </p>
      </section>
    </div>
  </div>
</div>

<style>
  .image-converter-container {
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    align-items: center;
    height: 100%;
    overflow-y: auto;
  }

  .hero-section {
    width: 100%;
    max-width: 960px;
    min-height: 160px;
    padding: 30px;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    box-sizing: border-box;
  }
  .hero-div {
    width: 100%;
    display: flex;
    justify-content: center;
    background: radial-gradient(circle at top left, #3a3a3a, #1e1e1e);
  }

  .hero-left {
    max-width: 600px;
    text-align: left;
  }

  .hero-left h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
  }

  .hero-left p {
    font-size: 1rem;
    opacity: 0.9;
  }

  .hero-right {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .converter-card {
    padding: 20px;
    width: 100%;
    max-width: 600px;
    margin: auto;
    text-align: center;
  }

  .preview img,
  .result img {
    max-width: 100%;
    margin-top: 15px;
    border-radius: 8px;
  }

  button {
    padding: 10px 20px;
    margin: 10px 5px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    font-size: 1rem;
  }

  button:hover {
    background-color: #0056b3;
  }

  select {
    padding: 8px 12px;
    margin: 0 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
  }

  input[type="file"] {
    margin: 10px 0;
  }

  .file-info {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 15px 0;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 6px;
    margin-left: auto;
    margin-right: auto;
    background-color: #fff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .file-icon {
    font-size: 1.2rem;
  }

  .file-name {
    flex: 1;
    word-break: break-all;
    color: #333;
    font-size: 0.95rem;
  }

  .remove-btn {
    background-color: transparent;
    color: #999;
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
    font-size: 1.2rem;
    min-width: unset;
  }

  .remove-btn:hover {
    color: #d32f2f;
    background-color: transparent;
  }

  .select-file-btn {
    padding: 12px 24px;
    margin: 10px 5px;
    border: none;
    border-radius: 6px;
    background-color: #c41e3a;
    color: white;
    cursor: pointer;
    font-size: 1.5rem;
    font-weight: 350;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: background-color 0.3s ease;
  }

  .select-file-btn:hover {
    background-color: #a01830;
  }

  button:not(.select-file-btn):not(.remove-btn) {
    padding: 12px 24px;
    margin: 10px 5px;
    border: none;
    border-radius: 6px;
    background-color: #c41e3a;
    color: white;
    cursor: pointer;
    font-size: 1.5rem;
    font-weight: 350;
    transition: background-color 0.3s ease;
  }

  button:not(.select-file-btn):not(.remove-btn):hover {
    background-color: #a01830;
  }

  .info-sections-wrapper {
    width: 100%;
    max-width: 960px;
    margin-top: 40px;
    padding: 20px;
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }

  .two-column-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    width: 100%;
  }

  .card {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .info-section {
    width: 100%;
    text-align: left;
  }

  .intro-text,
  .tool-palette-desc,
  .formats-supported {
    font-size: 1.1rem;
    max-width: 700px;
    line-height: 1.6;
  }

  .intro-text {
    font-weight: 500;
  }

  .formats-supported {
    margin-top: 15px;
    font-weight: bold;
    color: var(--mdc-theme-secondary, #018786);
  }

  .conversion-lists {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    margin-top: 20px;
  }

  .list-column {
    flex: 1;
    min-width: 250px;
    max-width: 400px;
    text-align: left;
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    color: #333;
  }

  .list-column h3 {
    color: #333;
    margin-top: 0;
  }

  .list-column ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .list-column li {
    font-size: 1rem;
    line-height: 1.8;
  }

  .icon-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px; 
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    .hero-section {
      flex-direction: column;
      text-align: center;
      gap: 20px;
    }
    .hero-left h1 {
      font-size: 2rem;
    }
    .info-sections-wrapper {
      padding: 15px;
    }
    .two-column-cards {
      grid-template-columns: 1fr;
    }
  }
</style>
