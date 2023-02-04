import sys

ISPU = [
    {
        'min': 0,
        'max': 50,
        'pm25_value': 15.5,
        'emoji': '🙂',
        'category': 'Baik',
        'description': 'Tingkat kualitas udara yang sangat baik, tidak memberikan efek negatif terhadap manusia, hewan, tumbuhan.',
        'suggestion': 'Sangat baik melakukan kegiatan di luar.'
    },
    {
        'min': 51,
        'max': 100,
        'pm25_value': 55.4,
        'emoji': '😐',
        'category': 'Sedang',
        'description': 'Tingkat kualitas udara masih dapat diterima pada kesehatan manusia, hewan dan tumbuhan.',
        'suggestion': 'Kelompok sensitif: Kurangi aktivitas fisik yang terlalu lama atau berat.\n\nSetiap orang: Masih dapat beraktivitas di luar.'
    },
    {
        'min': 101,
        'max': 200,
        'pm25_value': 150.4,
        'emoji': '😷',
        'category': 'Tidak Sehat',
        'description': 'Tingkat kualitas udara yang bersifat merugikan pada manusia, hewan dan tumbuhan.',
        'suggestion': 'Kelompok sensitif: Boleh melakukan aktivitas di luar, tetapi mengambil rehat lebih sering dan melakukan aktivitas ringan. Amati gejala berupa batuk atau nafas sesak. \n\nPenderita asma harus mengikuti pentunjuk kesehatan untuk asma dan menyimpan obat asma.\n\nPenderita penyakit jantung: gejala seperti palpitasi / jantung berdetak lebih cepat, sesak nafas, atau kelelahan yang tidak biasa mungkin mengindikasikan masalah serius.\n\nSetiap orang: Mengurangi aktivitas fisik yang terlalu lama di luar ruangan.'
    },
    {
        'min': 201,
        'max': 300,
        'pm25_value': 250.4,
        'emoji': '🤒',
        'category': 'Sangat Tidak Sehat',
        'description': 'Tingkat kualitas udara yang dapat mengakibatkan resiko kesehatan pada sejumlah segmen populasi yang terpapar.',
        'suggestion': 'Kelompok sensitif: Hindari semua aktivitas di luar. Perbanyak aktivitas di dalam ruangan atau lakukan penjadwalan ulang pada waktu dengan kualitas udara yang baik.\n\nSetiap orang: Hindari aktivitas fisik yang terlalu lama di luar ruangan, pertimbangkan untuk melakukan aktivitas di dalam ruangan.'
    },
    {
        'min': 300,
        'max': sys.maxsize,
        'pm25_value': 500,
        'emoji': '🤢',
        'category': 'Berbahaya',
        'description': 'Tingkat kualitas udara yang dapat merugikan kesehatan serius pada populasi dan perlu penanganan cepat.',
        'suggestion': 'Kelompok sensitif: Tetap di dalam ruangan dan hanya melakukan sedikit aktivitas.\n\nSetiap orang: Hindari semua aktivitas di luar.'
    },
]

day_of_week = [
    'Senin',
    'Selasa',
    'Rabu',
    'Kamis',
    'Jumat',
    'Sabtu',
    'Minggu',
]

month = [
    'Januari',
    'Februari',
    'Maret',
    'April',
    'Mei',
    'Juni',
    'Juli',
    'Agustus',
    'September',
    'Oktober',
    'November',
    'Desember',
]

def transform_to_class_name(category_name: str) -> str:
    return category_name.replace(' ', '-').lower()