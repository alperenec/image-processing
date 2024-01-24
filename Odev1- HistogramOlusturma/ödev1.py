gri_seviye_goruntu = [
    [50, 75, 100, 50],
    [25, 50, 75, 100],
    [100, 75, 50, 25],
    [75, 100, 25, 50]
]

# Görüntünün genişlik ve yüksekliğini al
w = len(gri_seviye_goruntu)
h = len(gri_seviye_goruntu[0])

# Histogram için bir dizi oluştur
histogram = [0] * 256  # Gri seviyeler 0-255 arasında olduğu için 256 elemanlı bir dizi oluşturduk

# Görüntüde dolaşarak histogramı hesapla
for v in range(h):
    for u in range(w):
        piksel_degeri = gri_seviye_goruntu[u][v]
        histogram[piksel_degeri] += 1

# Sonucu görüntüle
for i, count in enumerate(histogram):
    if count > 0:
        print(f"Piksel değeri {i}: {count} adet")