from camelcase import CamelCase

instanceCC = CamelCase('al','del')
texto = "Bienvenidos al mundo del backend"
print(instanceCC.hump(texto))