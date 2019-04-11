listaProveedores = []

class Proveedores(object):
    CUIT = None
    CuentaProveedor = None
    Nombre = None
    Dir = None
    codigoPostal = None
    Loc = None
    Tel = None
    Fax = None
    Retiva = None
    Poriva = None
    Retibr = None
    Poribr = None
    Retgcia = None
    Porgcia = None
    Retseg = None
    Porseg = None

    def getLista(self):
        return listaProveedores

    def agregarProveedor(self):
        f = open('datos1.json', 'r')

        unProveedor = Proveedores()

        for item in range(1000):
            f1 = f.read(11)
            f2 = f.read(5)
            f3 = f.read(30)
            f4 = f.read(30)
            f5 = f.read(4)
            f6 = f.read(15)
            f7 = f.read(20)
            f8 = f.read(20)
            f9 = f.read(2)
            f10 = f.read(10)
            f11 = f.read(2)
            f12 = f.read(10)
            f13 = f.read(2)
            f14 = f.read(10)
            f15 = f.read(2)
            f16 = f.read(10)

            unProveedor.CUIT = f1
            unProveedor.CuentaProveedor = f2
            unProveedor.Nombre = f3
            unProveedor.Dir = f4
            unProveedor.codigoPostal = f5
            unProveedor.Loc = f6
            unProveedor.Tel = f7
            unProveedor.Fax = f8
            unProveedor.Retiva = f9
            unProveedor.Poriva = f10
            unProveedor.Retibr = f11
            unProveedor.Poribr = f12
            unProveedor.Retgcia = f13
            unProveedor.Porgcia = f14
            unProveedor.Retseg = f15
            unProveedor.Porseg = f16

            listaProveedores.append(unProveedor)
