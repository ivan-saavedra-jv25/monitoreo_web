// src/components/Card.js


export default function Table({ lista, onEliminar }) {
  return (
    <div className="glass" style={{ width: "100%", padding: "10px" ,  borderRadius: "10px",}}>
      <h3>Lista de Páginas Web</h3>
      <table className="table table-hover table-sm">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Address / IP</th>
            <th scope="col">Titular</th>
            <th scope="col">Creacion</th>
            <th scope="col">Expiracion</th>
            <th scope="col">Estado</th>
            <th scope="col">Latencia</th>
            <th scope="col">Acciones</th> 
          </tr>
        </thead>
        <tbody>
          {lista.map((item, index) => (
            <tr key={index}>
              <th scope="row">{index + 1}</th>
              <td>{item.url}</td>
              <td>{item.titular}</td>
              <td>{item.fecha_creacion}</td>
              <td>{item.fecha_expiracion}</td>
              <td>
                {item.estado === 200 ? (
                  <span style={{
                    display: "inline-block",
                    width: 16,
                    height: 16,
                    borderRadius: "50%",
                    background: "green",
                    verticalAlign: "middle"
                  }} title="200 OK"></span>
                ) : (
                  <span style={{
                    display: "inline-block",
                    width: 16,
                    height: 16,
                    borderRadius: "50%",
                    background: "red",
                    verticalAlign: "middle"
                  }} title={item.estado ? item.estado : "Desconocido"}></span>
                )}
              </td>
              <td>{item.latency_ms}</td>
              <td>
                <button
                  className="btn btn-danger btn-sm"
                  onClick={() => onEliminar(item.id)}
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}