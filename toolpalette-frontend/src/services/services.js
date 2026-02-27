export async function convertImage(file) {
  const formData = new FormData();
  formData.append("file", file);

  const baseUrl = import.meta.env.VITE_API_URL;
  const token = import.meta.env.VITE_SECURITY_HEADER;

  const res = await fetch(`${baseUrl}/convert-to-webp`, {
    method: "POST",
    headers: {
      "api-key": `${token}`
    },
    body: formData,
  });

  if (!res.ok) {
    throw new Error(`HTTP error! status: ${res.status}`);
  }

  const blob = await res.blob();
  return blob;
}