import os
from python_anvil_encryption import encryption

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


def main():
    # Read your public and private keys
    public_key = None
    private_key = None
    with open(os.path.join(CURRENT_PATH, "keys/public.pub"), "rb") as pub_file:
        public_key = pub_file.read()

    with open(os.path.join(CURRENT_PATH, "./keys/private.pem"), "rb") as priv_file:
        private_key = priv_file.read()

    # RSA
    message = b"Super secret message"
    encrypted_message = encryption.encrypt_rsa(public_key, message)
    decrypted_message = encryption.decrypt_rsa(private_key, encrypted_message)
    assert decrypted_message == message
    print(f"Are equal? {decrypted_message == message}")

    # AES
    aes_key = encryption.generate_aes_key()
    aes_encrypted_message = encryption.encrypt_aes(aes_key, message)
    # The aes key in the first parameter is required to be in a hex
    # byte string format.
    decrypted_message = encryption.decrypt_aes(
        aes_key.hex().encode(), aes_encrypted_message
    )
    assert decrypted_message == message
    print(f"Are equal? {decrypted_message == message}")


if __name__ == "__main__":
    main()
    print(CURRENT_PATH)
