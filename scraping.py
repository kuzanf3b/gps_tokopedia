import pandas as pd
from google_play_scraper import Sort, reviews

print("Starting the scraping process...")

# Mengambil ulasan dari Google Play Store
# Kita ambil 11.000 data untuk memastikan melewati batas minimal 10.000 sampel
result, _ = reviews(
    "com.tokopedia.tkpd",
    lang="id",
    country="id",
    sort=Sort.NEWEST,
    count=11000
)

# Membuat DataFrame dari hasil scraping
df = pd.DataFrame(result)

# Memilih kolom yang relevan untuk analisis
df = df[['content', 'score']]

# Fungsi untuk pelabelan otomatis menjadi 3 kelas berdasarkan rating (score)
def pelabelan_sentimen(score):
    if score <= 2:
        return 'negatif'
    elif score == 3:
        return 'netral'
    else:
        return 'positif'

# Terapkan fungsi pelabelan
df['label'] = df['score'].apply(pelabelan_sentimen)

# Cek distribusi kelas untuk memastikan data cukup seimbang
print("\nJumlah data per kelas:")
print(df['label'].value_counts())

# Simpan ke dalam file CSV
df.to_csv('dataset_sentimen.csv', index=False, encoding='utf-8')
print("\nScraping selesai! Data disimpan dalam 'dataset_sentimen.csv'")