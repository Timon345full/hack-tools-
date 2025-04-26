import qrcode

def qr_geration(sites, fileSave):
    data = sites
    filename = fileSave  # имя конечного файла
    img = qrcode.make(data) # генерируем QR-код
    img.save(filename) # сохраняем img в файл