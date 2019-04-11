from DB import DB

listaFacturas = []

def getLista():
    return listaFacturas


class Facturas(object):
    cuentaProveedor = None
    nroComprobante = None
    tipoFactura = None
    nroFactura = None
    estado = None
    fechaFactura = None
    importeFactura = None
    importeRetenciones = None

    @staticmethod
    def agregarFacturas():
        f = open('datos1.json', 'r')



        j = open('factprov.json', 'r')
        for item in range(1000):

            unaFactura = Facturas()

            j1 = j.read(5)
            j2 = j.read(6)
            j3 = j.read(3)
            j4 = j.read(12)
            j5 = j.read(3)
            j6 = j.read(8)
            j7 = j.read(1)
            j71 = j.read(1)
            j8 = j.read(9)
            j9 = j.read(1)
            j10 = j.read(9)
            j11 = j.read(1)

            unaFactura.cuentaProveedor = j1
            unaFactura.nroComprobante = j2
            unaFactura.tipoFactura = j3
            unaFactura.nroFactura = j4
            unaFactura.estado = j5
            unaFactura.fechaFactura = j6
            unaFactura.importeFactura = j8
            unaFactura.importeRetenciones = j10

            listaFacturas.append(unaFactura)

        j.close()

    @staticmethod
    def altaFacturas():
        for item in getLista():
            DB().run("INSERT INTO Facturas(idFacturas,cuentaProveedor,nroComprobante,tipoFactura,nroFactura,estado,fechaFactura,importeFactura,importeRetenciones) VALUES (NULL, " + str(item.cuentaProveedor) + "," + str(item.nroComprobante) + ",'" + item.tipoFactura + "'," + str(item.nroFactura) + ",'" + item.estado + "','" + item.fechaFactura + "','"+ item.importeFactura + "','" + item.importeRetenciones + "');")