from flask import Flask, render_template, send_file, request
from datetime import datetime
from weasyprint import HTML
import io
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def invoice_template():

    posted_data = request.get_json() or {}

    today = datetime.today().strftime("%-d %B %Y")
    underscored_today = datetime.today().strftime("%-d_%m_%Y")
    year = datetime.today().strftime("%Y")

    default_data = {
        "duedate": "28 February 2022",
        "from_addr": {
            "company_name": "André Lopes LDA.",
            "addr1": "Rua 1º de Maio, 44-A",
            "addr2": "6300-111 Guarda",
        },
        "invoice_number": f'1/{year}',
        "items": [
            {"title": "Montagem servidor", "charge": 450.00},
            {"title": "Configuração servidor", "charge": 150.00},
            {"title": "Website c/ domínio", "charge": 80.00},
        ],
        "to_addr": {
            "company_name": "Empresa ABC",
            "client_name": "José Augusto",
            "client_email": "jaugusto@mail.com",
        },
    }

    duedate = posted_data.get("duedate", default_data["duedate"])
    from_addr = posted_data.get("from_addr", default_data["from_addr"])
    to_addr = posted_data.get("to_addr", default_data["to_addr"])
    invoice_number = posted_data.get("invoice_number", default_data["invoice_number"])
    items = posted_data.get("items", default_data["items"])

    total = sum([i["charge"] for i in items])

    rendered = render_template(
        "invoice.html",
        date=today,
        from_addr=from_addr,
        to_addr=to_addr,
        items=items,
        total=total,
        invoice_number=invoice_number,
        duedate=duedate,
    )

    html = HTML(string=rendered)

    rendered_pdf = (
        html.write_pdf()
    )  # enter the relative path here if you want to save the invoice instead of sending it,
    # be aware that will make the webpage show a "Could not load the PDF" error

    return send_file(io.BytesIO(rendered_pdf), download_name=f"invoice_{underscored_today}.pdf")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
