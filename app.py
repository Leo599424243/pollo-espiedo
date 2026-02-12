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

    # CANTIDADES POR DOCENA O UNIDAD
    sandwich_especial = int(request.form.get("sandwich_especial", 0))
    sandwich_comun = int(request.form.get("sandwich_comun", 0))

    docena_carne = int(request.form.get("docena_carne", 0))
    docena_jamon_queso = int(request.form.get("docena_jamon_queso", 0))
    docena_pollo = int(request.form.get("docena_pollo", 0))

    milanesa_napolitana = int(request.form.get("milanesa_napolitana", 0))
    milanesa_marinera = int(request.form.get("milanesa_marinera", 0))
    costeleta_completa = int(request.form.get("costeleta_completa", 0))

    pizza_muzzarella = int(request.form.get("pizza_muzzarella", 0))
    pizza_especial = int(request.form.get("pizza_especial", 0))

    # NUEVAS HAMBURGUESAS
    hamburguesa_comun = int(request.form.get("hamburguesa_comun", 0))
    hamburguesa_especial = int(request.form.get("hamburguesa_especial", 0))
    promo_5_hamburguesas = int(request.form.get("promo_5_hamburguesas", 0))  # cantidad de promos

    # PRECIOS
    precio_sandwich_especial = 13000
    precio_sandwich_comun = 10000

    precio_docena_carne = 12000
    precio_docena_jamon_queso = 14000
    precio_docena_pollo = 10000

    precio_milanesa_napolitana = 15000
    precio_milanesa_marinera = 15000
    precio_costeleta_completa = 15000

    precio_pizza_muzzarella = 10000
    precio_pizza_especial = 12000

    # HAMBURGUESAS
    precio_hamburguesa_comun = 2500
    precio_hamburguesa_especial = 3000
    precio_promo_5_hamburguesas = 12000

    # TOTAL
    total = (
        sandwich_especial * precio_sandwich_especial +
        sandwich_comun * precio_sandwich_comun +
        docena_carne * precio_docena_carne +
        docena_jamon_queso * precio_docena_jamon_queso +
        docena_pollo * precio_docena_pollo +
        milanesa_napolitana * precio_milanesa_napolitana +
        milanesa_marinera * precio_milanesa_marinera +
        costeleta_completa * precio_costeleta_completa +
        pizza_muzzarella * precio_pizza_muzzarella +
        pizza_especial * precio_pizza_especial +
        hamburguesa_comun * precio_hamburguesa_comun +
        hamburguesa_especial * precio_hamburguesa_especial +
        promo_5_hamburguesas * precio_promo_5_hamburguesas
    )

    # MENSAJE WHATSAPP
    mensaje = f"""
🍽 *PEDIDO ROTISERÍA KILLO*

🥪 Sándwich de Milanesa Especial: {sandwich_especial}
🥪 Sándwich de Milanesa Común: {sandwich_comun}

🥟 Empanada Carne - Docenas: {docena_carne}
🥟 Empanada Jamón y Queso - Docenas: {docena_jamon_queso}
🥟 Empanada Pollo - Docenas: {docena_pollo}

🍖 Milanesa Napolitana: {milanesa_napolitana}
🍖 Milanesa Marinera: {milanesa_marinera}
🥩 Costeleta Completa: {costeleta_completa}

🍕 Pizza Muzzarella: {pizza_muzzarella}
🍕 Pizza Especial: {pizza_especial}

🍔 Hamburguesa Común: {hamburguesa_comun}
🍔 Hamburguesa Especial: {hamburguesa_especial}
🍔 Promo 5 Hamburguesas + Papas: {promo_5_hamburguesas}

💰 *TOTAL: ${total}*

🕒 Retiro: {horario}

👤 Cliente: {nombre}
📞 Tel: {telefono}
"""

    mensaje = mensaje.replace(" ", "%20").replace("\n", "%0A")
    numero = "5493624134557"

    return f"""
    <script>
        window.location.href = "https://wa.me/{numero}?text={mensaje}";
    </script>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
