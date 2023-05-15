# 1. Skenario: Pengelolaan Buku Telepon
# 2. Deskripsi: Anda diminta untuk membuat sistem backend sederhana untuk mengelola buku telepon. Sistem ini harus mampu menyimpan kontak telepon dengan nama dan nomor teleponnya.
# Tugas:
#     * Buatlah sebuah kelas Contact yang memiliki atribut nama dan nomor telepon.
#     * Buatlah sebuah kelas AddressBook yang memiliki fungsi untuk menambah kontak baru, menghapus kontak, dan mencari kontak berdasarkan nama.
#         * Implementasikan fungsi-fungsi berikut:
#         * add_contact(name: str, phone_number: str) -> None: Menambahkan kontak baru dengan nama dan nomor telepon ke dalam buku telepon.
#         * remove_contact(name: str) -> None: Menghapus kontak dari buku telepon berdasarkan nama.
#         * search_contact(name: str) -> str: Mencari nomor telepon kontak berdasarkan nama. Mengembalikan nomor telepon jika kontak ditemukan, dan pesan "Kontak tidak ditemukan" jika tidak ditemukan.
# 3. Kriteria penilaian:
#     * Fungsi-fungsi harus diimplementasikan dengan benar dan menghasilkan hasil yang sesuai.
#     * Kode harus bersih, terorganisir, dan mudah dibaca.

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class AddressBook:
    def __init__(self):
        self.contact_list = []


    def add_contact(self, name, phone_number):
        self.contact_list.append(Contact(name, phone_number))


    def remove_contact(self, name):
        for contact in self.contact_list:
            if contact.name == name:
                self.contact_list.remove(contact)
                return


    def search_contact(self, name):
        for contact in self.contact_list:
            if contact.name == name:
                return contact.phone_number
        return "Kontak tidak ditemukan"

address_book = AddressBook()
address_book.add_contact("Andi", "08123456789")
address_book.add_contact("Budi", "08987654321")
address_book.add_contact("Cici", "08123456789")
address_book.remove_contact("Budi")
print(address_book.search_contact("Andi"))
print(address_book.search_contact("Budi"))
print(address_book.search_contact("Cici"))
