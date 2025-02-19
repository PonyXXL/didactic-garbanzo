from main import greet

def generate_otp_code(t=5):
    return "".join([x for x in range(t)])

greet()