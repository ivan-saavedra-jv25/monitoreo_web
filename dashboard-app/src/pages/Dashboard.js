// src/pages/Dashboard.js
import React, { useState, useEffect } from "react";

import Card from "../components/Card";
import Table from "../components/Table";
import BotonPagina from "../components/BotonPagina";

import { lista_monitoreo,  eliminar_web, actualizar_info_web} from "../services/api";


import './Dashboard.css';

export default function Dashboard() {


    const [lista, setLista] = useState([]);
    const [total, setTotal] = useState(0);
    const [paginasActivas, setPaginasActivas] = useState(0);
    const [paginasDesactivadas, setPaginasDesactivadas] = useState(0)
    

    async function fetchData() {
      const data = await lista_monitoreo();
      prepar_data_fecht(data)
    }
    
    const prepar_data_fecht=(data)=>{
      // NO renderices el círculo aquí, solo pasa el valor real
      const prepared = data.map((item) => ({
        id: item.id,
        url: item.url || "Sin datos",
        titular: item.titular || "Desconocido",
        fecha_creacion: item.fecha_creacion,
        fecha_expiracion: item.fecha_expiracion,
        estado: item.estado,
        latency_ms: item.latency_ms !== undefined ? `${parseInt(item.latency_ms)} ms` : "N/A",
      }));
  
      setLista(prepared);      
      setTotal(data.length);
      const paginas_activa = data.filter(item => item.estado === 200).length;
      setPaginasActivas(paginas_activa);
      const paginas_desactivada = data.filter(item => item.estado !== 200).length;
      setPaginasDesactivadas(paginas_desactivada);

    }

    const handleEliminarWeb = async (id)=>{
      await eliminar_web(id);
      await fetchData();
    }

    const handleActulizarweb= async ()=>{

      const daata = await actualizar_info_web();
      console.log("Actualizando datos de las webs", daata);
      prepar_data_fecht(daata)
      

    }
    
    
   

    useEffect(() => {   
      fetchData();
    }, []);



 return (
    
    <div className="dashboard-layout">
      {/* Contenido principal */}
      <main className="main-content">
        <header className="header">
          <h1>Dashboard</h1>
        </header>

        <section className="cards">
          <Card title={'Total de Páginas'} value={total}/>
          <Card title={'Activas'} value={paginasActivas}/>
          <Card title={'Desactivadas'} value={paginasDesactivadas}/>
        </section>

        <section className="table-container">  
          <Table lista={lista} onEliminar={handleEliminarWeb} />
        </section>

      </main>

      {/* Footer menú */}
      <footer className="footer-menu">
        <ul>
          <BotonPagina set_fechtData={fetchData}/>

           <li  onClick={() => handleActulizarweb()}>
              Actualizar latencia
            </li>
         
        </ul>
      </footer>
    </div>
  
  );
}
