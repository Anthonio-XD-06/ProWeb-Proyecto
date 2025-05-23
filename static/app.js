document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();
    let username = document.getElementById("username").value;
    document.getElementById("user").textContent = username;
    document.getElementById("login").style.display = "none";
    document.getElementById("dashboard").style.display = "block";
    fetchTarjetas();
});

document.getElementById("formAgregarTarjeta").addEventListener("submit", function(e) {
    e.preventDefault();
    const data = {
        numero: document.getElementById("numeroTarjeta").value,
        fecha_corte: document.getElementById("fechaCorte").value,
        fecha_pago: document.getElementById("fechaPago").value,
        debe: document.getElementById("cantidadDebe").value
    };

    fetch("/agregar_tarjeta", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(res => res.json()).then(res => {
        fetchTarjetas();
    });
});

function fetchTarjetas() {
    fetch("/tarjetas").then(res => res.json()).then(data => {
        const container = document.getElementById("tarjetasContainer");
        container.innerHTML = '';
        let total = 0;
        data.forEach(t => {
            total += parseFloat(t.debe);
            container.innerHTML += `<div>
                <p><strong>${t.numero}</strong></p>
                <p>Fecha de corte: ${t.fecha_corte}</p>
                <p>Fecha de pago: ${t.fecha_pago}</p>
                <p>Debe: $${t.debe}</p>
            </div>`;
        });
        document.getElementById("totalDeuda").textContent = total.toFixed(2);
    });
}

function simularGasto() {
    let monto = parseFloat(document.getElementById("monto").value);
    let meses = parseInt(document.getElementById("meses").value);
    let interes = parseFloat(document.getElementById("interes").value);

    let interesTotal = monto * (interes / 100);
    let total = monto + interesTotal;
    let mensual = total / meses;

    document.getElementById("resultadoSimulacion").textContent =
        `Total a pagar: $${total.toFixed(2)} - Pago mensual: $${mensual.toFixed(2)}`;
}

function mostrarSeccion(nombre) {
    const secciones = document.querySelectorAll('.seccion');
    secciones.forEach(sec => sec.style.display = 'none');
    document.getElementById(nombre).style.display = 'block';
}
