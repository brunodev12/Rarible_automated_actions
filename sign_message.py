import subprocess

def signTypedMessage(message):

    output = subprocess.check_output(['node', 'sign_message.js', message])

    signature = output.decode().strip()
    
    return signature