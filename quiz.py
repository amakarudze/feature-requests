# Solution to the quiz.


from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb9VzwEcWVC3QIjQzMF_Eetm81vi4oirzhXVCv_OMe52ICieDiFs5SL96WNR9MUfTas3R5TwODZTTxUbvUcXOJEj93f6hItYvBBqGmdDi6qMaZbmoPqfSZ0W6zsGLtMhI9MBAMuRNsdfr7Lo0cET-USsRkgxA81s3CFos6V9uaa_yBSO0zLUFBvnagyGMtV6gQgGfA'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if '__name__' != "__main__":
    main()
