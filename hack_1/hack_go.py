import qrcode

def get_qrcode(url='https://google.com',name= 'default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f"{name}.png")

    return f"qr was created! open the {name}.png"

def main():
    print(get_qrcode(url='https://vk.com/id497242500',name = "vk"))
    print(get_qrcode(url='https://www.instagram.com/xmir_abbosx/',name = "ins"))


if __name__ == '__main__':
    main()