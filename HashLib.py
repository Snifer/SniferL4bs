import hashlib

print "Ejemplo del uso de Hashlib "
print "==========================\n"

String = "Python Forensic with Snifer@L4b's"

md5 = hashlib.md5()
sha1 = hashlib.sha1()

hexMD5 = md5.hexdigest()
hexSHA1 = sha1.hexdigest()

print ("El hash de " + String + " es:\n")

print ("MD5 Hash -> " + hexMD5 ) #Mostramos el hash en minúsculas
print ("SHA1 Hash -> " + hexSHA1.upper())#Mostramos el resultado del Hash en mayúsculas
