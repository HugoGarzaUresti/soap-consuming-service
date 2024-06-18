# SOAP Country Service

This guide demonstrates how to set up a simple SOAP web service in Python using the `spyne` library to provide country information.

## Requirements

- Python 3.x
- `spyne` library
- `werkzeug` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the web service:
    ```sh
    python run.py
    ```

3. The web service will be available at `http://localhost:8080`.

## Endpoints

- `http://localhost:8080/?wsdl`: WSDL file for the SOAP web service.
- `http://localhost:8080/`: Endpoint for SOAP requests.

## Example SOAP Request

You can use the following SOAP request to get country information:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:gs="http://spyne.examples.country">
   <soapenv:Header/>
   <soapenv:Body>
      <gs:getCountry>
         <gs:name>Spain</gs:name>
      </gs:getCountry>
   </soapenv:Body>
</soapenv:Envelope>
