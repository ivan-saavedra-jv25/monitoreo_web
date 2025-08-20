// src/components/Card.js

import React, { useState, useEffect } from "react";
import { Modal, Button } from "react-bootstrap";
import { agregar_web } from "../services/api";

export default function BotonPagina({set_fechtData}) {

    const [show, setShow] = useState(false);
    const [nuevaWeb, setNuevaWeb] = useState("");

     const handleAgregarWeb = async (e) => {
          e.preventDefault();
          // Espera a que termine de agregar
          await agregar_web(nuevaWeb);
          setNuevaWeb("");
          setShow(false);
          if(set_fechtData){
              await set_fechtData(); // Refresca la tabla

          }
        };
    
        

  return (
    <>
    <li  onClick={() => setShow(true)}>
              Agregar Web
            </li>

            {/* Modal igual que arriba */}
            <Modal show={show} onHide={() => setShow(false)}>
              <Modal.Header closeButton>
                <Modal.Title>Ingrese Pagina web o IP</Modal.Title>
              </Modal.Header>
              <Modal.Body>
                <form onSubmit={handleAgregarWeb}>
                  <input
                    type="text"
                    className="form-control"
                    placeholder="Ingrese URL o IP"
                    value={nuevaWeb}
                    onChange={e => setNuevaWeb(e.target.value)}
                    required
                  />
                  <Button variant="success" type="submit" className="mt-2 w-100">
                    Agregar
                  </Button>
                </form>
              </Modal.Body>
              <Modal.Footer>
                <Button variant="secondary" onClick={() => setShow(false)}>
                  Cerrar
                </Button>
              </Modal.Footer>
            </Modal>
    </>
  );
}
