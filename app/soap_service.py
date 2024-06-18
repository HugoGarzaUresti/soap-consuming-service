from spyne import Application, rpc, ServiceBase, Unicode, Integer, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.complex import ComplexModel
from werkzeug.serving import run_simple

class Currency(ComplexModel):
    name = Unicode

class Country(ComplexModel):
    name = Unicode
    capital = Unicode
    population = Integer
    currencies = Array(Currency)

class CountryService(ServiceBase):
    @rpc(Unicode, _returns=Country)
    def getCountry(ctx, name):
        if name == "Spain":
            return Country(
                name="Spain",
                capital="Madrid",
                population=46704314,
                currencies=[Currency(name="Euro")]
            )
        elif name == "United Kingdom":
            return Country(
                name="United Kingdom",
                capital="London",
                population=67886011,
                currencies=[Currency(name="Pound Sterling")]
            )
        return None

application = Application([CountryService], 'spyne.examples.country',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

def main():
    run_simple('localhost', 8080, wsgi_application)

if __name__ == "__main__":
    main()
