# main.py

from url_validator import is_valid_url


def main():
    print("=== Simulasi Validasi URL (berbasis kode dari Firefox) ===")
    url = input("Masukkan URL: ")

    if is_valid_url(url):
        print("✅ URL valid.")
    else:
        print("❌ Bukan URL yang valid.")


if __name__ == "__main__":
    main()