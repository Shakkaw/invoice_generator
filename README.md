# Generates a invoice PDF from a HTML template.


## Installation 

``` shell
mkdir invoice_generator
cd invoice_generator
git clone https://github.com/Shakkaw/invoice_generator.git
python -m venv ./
source ./bin/Activate.ps1 #choose the activate script right for your platform, this example is for windows powershell
pip install -r requirements.txt
```

## Usage

Launch a local session of the server by running **`generate_invoice.py`**
Open your browser on the IP address provided on the console to view a template invoice filled with data

Launch **`api_call.py`** and follow the instructions to generate a custom invoice with your data



### Credits
 

Invoice template based on https://github.com/sparksuite/simple-html-invoice-template