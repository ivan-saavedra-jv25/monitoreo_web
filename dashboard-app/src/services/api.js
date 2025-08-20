
const API_URL = "http://127.0.0.1:5000/websites";

export async function lista_monitoreo() {
  try {
    const response = await fetch(API_URL)
    if(!response.ok){ return []; }
    const data = await response.json();

    return data

  } catch (err) {
    console.error("API error:", err);
    return [];
  }
}

export async function agregar_web(url) {
    try {
        const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
        });
        if (!response.ok) {
        throw new Error("Error adding website");
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.error("API error:", err);
        throw err;
    }
}

export async function eliminar_web(id) {
  console.log("Eliminando web con ID:", id); // Log para verificar el ID recibido
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE",
        });
        if (!response.ok) {
            throw new Error("Error deleting website");
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.error("API error:", err);
        throw err;
    }
}

export async function actualizar_info_web() {
    try {
        const response = await fetch(`${API_URL}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            
        });
        if (!response.ok) {
            throw new Error("Error updating website info");
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.error("API error:", err);
        throw err;
    }
}