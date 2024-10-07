from Crypto.PublicKey import RSA

def generate_rsa_key_pair(key_size=2048):
    """Generate an RSA key pair."""
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def main():
    private_key, public_key = generate_rsa_key_pair()
    print("Private Key:")
    print(private_key.decode())
    print("\nPublic Key:")
    print(public_key.decode())

if __name__ == "__main__":
    main()
