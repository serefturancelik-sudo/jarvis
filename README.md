/jarvis-core
├── main.py          # FastAPI sunucusu ve ana kontrolcü
├── requirements.txt # Kullanılan kütüphanelerin listesi
├── services/        # Modüllerin bulunduğu klasör
│   ├── camera.py    # Kamera ve görüntü işleme
│   ├── hardware.py  # COM port ve ESP32 haberleşmesi
│   └── excel.py     # Excel dosyaları işlemleri
└── static/          # Web arayüzü dosyaların (index.html, js, css)
    └── index.html
