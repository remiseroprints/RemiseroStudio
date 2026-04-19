import gradio as gr
from PIL import Image, ImageDraw, ImageFont

WHATSAPP = "51997064875"
WEB = "https://www.remiserostudio.com/impresion-color/tarjetas-personales/"

def generar_tarjeta(nombre, cargo, empresa, telefono, logo):
    img = Image.new("RGB", (1000, 600), color=(15, 15, 15))
    draw = ImageDraw.Draw(img)

    try:
        font_nombre = ImageFont.truetype("DejaVuSans-Bold.ttf", 65)
        font_texto = ImageFont.truetype("DejaVuSans.ttf", 40)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 25)
    except:
        font_nombre = None
        font_texto = None
        font_small = None

    if logo is not None:
        logo = logo.resize((180, 180))
        img.paste(logo, (750, 50))

    draw.text((80, 180), nombre, fill=(255, 255, 255), font=font_nombre)
    draw.text((80, 280), cargo, fill=(200, 200, 200), font=font_texto)
    draw.text((80, 340), empresa, fill=(0, 200, 150), font=font_texto)
    draw.text((80, 400), f"Tel: {telefono}", fill=(255, 255, 255), font=font_texto)

    # Branding + SEO
    draw.text((80, 520), "RemiseroStudio", fill=(255, 215, 0), font=font_texto)
    draw.text((80, 560), "www.remiserostudio.com", fill=(120,120,120), font=font_small)

    return img

def calcular_precio(cantidad):
    if cantidad == 100:
        total = 70
        tipo = "Impresión láser digital"
        material = "Couché 300 gr"
    elif cantidad == 200:
        total = 140
        tipo = "Impresión láser digital"
        material = "Couché 300 gr"
    elif cantidad == 500:
        total = 330
        tipo = "Impresión offset"
        material = "Couché 350 gr"
    elif cantidad == 1000:
        total = 380
        tipo = "Impresión offset"
        material = "Couché 350 gr"
    else:
        total = 0
        tipo = "-"
        material = "-"

    return f"""💰 PRECIO: S/ {total}

✔ {material}
✔ {tipo}
✔ Full color ambas caras
✔ Plástificado mate
✔ Corte recto
"""

def generar_link(nombre, cargo, empresa, telefono, cantidad, detalle):
    mensaje = f"""Hola, quiero hacer mi pedido de tarjetas:

👤 Nombre: {nombre}
💼 Cargo: {cargo}
🏢 Empresa: {empresa}
📞 Teléfono: {telefono}

📦 Cantidad: {cantidad}

{detalle}

Ya vi esta página:
{WEB}

Adjunto mi diseño.
Vengo desde la app 🚀
"""
    url = f"https://wa.me/{WHATSAPP}?text={mensaje.replace(' ', '%20')}"

    return f"""
<a href="{url}" target="_blank" style="
display:inline-block;
background-color:#25D366;
color:white;
padding:15px 25px;
font-size:18px;
font-weight:bold;
border-radius:8px;
text-decoration:none;
">
📲 ENVIAR PEDIDO POR WHATSAPP
</a>
"""

with gr.Blocks() as demo:
    gr.Markdown("# 🎨 Diseña tus tarjetas personales en Lima")
    gr.Markdown("Diseña gratis, descarga y pide en segundos 🚀")

    with gr.Row():
        with gr.Column():
            nombre = gr.Textbox(label="Nombre")
            cargo = gr.Textbox(label="Cargo")
            empresa = gr.Textbox(label="Empresa")
            telefono = gr.Textbox(label="Teléfono")
            logo = gr.Image(label="Sube tu logo", type="pil")

            cantidad = gr.Radio([100, 200, 500, 1000], label="Cantidad", value=100)

            btn = gr.Button("🔥 Generar diseño y cotizar")

        with gr.Column():
            salida_img = gr.Image(label="Descarga tu diseño")
            detalle = gr.Textbox(label="Precio y detalles")
            boton = gr.Markdown()

    btn.click(generar_tarjeta, inputs=[nombre, cargo, empresa, telefono, logo], outputs=salida_img)
    btn.click(calcular_precio, inputs=[cantidad], outputs=detalle)
    btn.click(generar_link, inputs=[nombre, cargo, empresa, telefono, cantidad, detalle], outputs=boton)

    gr.Markdown("👉 Descarga tu diseño y envíalo por WhatsApp para imprimirlo")
    gr.Markdown("🔗 Más info: https://www.remiserostudio.com/impresion-color/tarjetas-personales/")

demo.launch()
