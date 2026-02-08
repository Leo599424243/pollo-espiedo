from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/pedido")
def pedido():
    return render_template("pedido.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    # DATOS DEL CLIENTE
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    horario = request.form["horario"]

    # CANTIDADES
    pollo = int(request.form["pollo"])
    milanesa = int(request.form["milanesa"])
    hamburguesa = int(request.form["hamburguesa"])
    hamburguesa_especial = int(request.form["hamburguesa_especial"])
    empanadas_carne = int(request.form["empanadas_carne"])
    empanadas_pollo = int(request.form["empanadas_pollo"])

    # PRECIOS
    precio_pollo = 18000
    precio_milanesa = 12000
    precio_hamburguesa = 2500
    precio_hamburguesa_especial = 3000
    precio_empanada_carne = 12000
    precio_empanada_pollo = 10000

    # TOTAL
    total = (
        pollo * precio_pollo +
        milanesa * precio_milanesa +
        hamburguesa * precio_hamburguesa +
        hamburguesa_especial * precio_hamburguesa_especial +
        empanadas_carne * precio_empanada_carne +
        empanadas_pollo * precio_empanada_pollo
    )

    # MENSAJE WHATSAPP
    mensaje = f"""
🍗 *PEDIDO POLLO AL ESPIEDO*

Pollo al espiedo: {pollo}
Milanesa: {milanesa}
Hamburguesa: {hamburguesa}
Hamburguesa especial: {hamburguesa_especial}
Empanadas carne: {empanadas_carne}
Empanadas pollo: {empanadas_pollo}

💰 *TOTAL: ${total}*

🕒 Retiro: {horario}

👤 Cliente: {nombre}
📞 Tel: {telefono}
"""

    mensaje = mensaje.replace(" ", "%20").replace("\n", "%0A")

    numero = "5493624134557"  # Argentina

    return f"""
    <script>
        window.location.href = "https://wa.me/{numero}?text={mensaje}";
    </script>
    """

# 👇 ESTA PARTE ES LA CLAVE PARA RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



