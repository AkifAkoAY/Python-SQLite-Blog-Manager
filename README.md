📝 Python SQLite Blog Manager (CLI)
Bu proje, Python'ın yerleşik sqlite3 kütüphanesi kullanılarak geliştirilmiş, komut satırı üzerinden çalışan basit bir blog yönetim sistemidir. Herhangi bir harici kütüphane kurulumu gerektirmez.

✨ Özellikler
Otomatik Veritabanı Kurulumu: Kod çalıştırıldığında blog.db dosyası ve gerekli tablolar yoksa otomatik oluşturulur.

Tam CRUD Desteği: - Create: Yeni blog yazıları ekleme.

Read: Tüm yazıları listeleme.

Update: Yazı başlığı ve yazarını güncelleme.

Delete: ID bazlı silme işlemi.

Güvenli Sorgular: SQL Injection riskine karşı parametreli (?) SQL yapısı kullanılmıştır.

🛠️ Kurulum ve Kullanım
Bilgisayarınızda Python'ın yüklü olduğundan emin olun.

Blog.py dosyasını indirin.

Terminal veya komut istemcisini açıp dosyanın bulunduğu klasöre gidin.

Aşağıdaki komutu çalıştırın:

Bash

python Blog.py
📂 Kod Yapısı
create_database(): Veritabanı bağlantısını açar ve şemayı oluşturur.

add_post() / get_all_posts(): Veri ekleme ve listeleme işlemlerini yönetir.

remove_post() / update_post(): Mevcut verileri yönetme ve düzenleme yeteneği sağlar.

main(): Kullanıcı arayüzünü (menü) ve uygulama döngüsünü kontrol eder.

⚠️ Önemli Not
Uygulama verileri yerel bir blog.db dosyasında saklar. Dosyayı silseniz bile kod her çalıştığında tablo yapısını yeniden kuracaktır (ancak eski verileriniz silinir).
