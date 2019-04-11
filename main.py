from DB import DB
from facturas import *
from proveedores import *

DB().setconnection("localhost", "root", "alumno", "mydb")

Facturas.agregarFacturas()
