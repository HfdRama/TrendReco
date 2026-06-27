from flask import render_template, request, jsonify


def init_chatbot_routes(app):

    @app.route('/chatbot')
    def chatbot_page():
        return render_template('chatbot.html')


    @app.route('/chatbot/send', methods=['POST'])
    def chatbot_send():

        data = request.get_json()
        message = data.get("message", "").lower().strip()

        # ==================================================
        # SAPAAN
        # ==================================================
        if any(x in message for x in [
            "halo", "hai", "hi", "pagi", "siang",
            "sore", "malam", "assalamualaikum"
        ]):

            reply = """
            <div class="space-y-3">

                <div class="flex items-center gap-2 text-blue-600 font-bold">
                    <i class="fa-solid fa-robot"></i>
                    <span>TrendReco Assistant</span>
                </div>

                <p>
                    Selamat datang di <b>TrendReco Assistant</b>.
                    Saya siap membantu Anda terkait penggunaan sistem dan strategi media sosial.
                </p>

                <div class="grid gap-2 mt-3">

                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-circle-info text-blue-500"></i>
                        Cara menggunakan sistem
                    </div>

                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-chart-line text-green-500"></i>
                        Informasi tren konten
                    </div>

                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-upload text-purple-500"></i>
                        Strategi upload
                    </div>

                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-heart text-red-500"></i>
                        Engagement media sosial
                    </div>

                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-gears text-amber-500"></i>
                        Algoritma platform
                    </div>

                </div>

                <div class="mt-3 p-3 bg-blue-50 rounded-xl text-sm">
                    Silakan tuliskan pertanyaan yang ingin Anda tanyakan.
                </div>

            </div>
            """

        # ==================================================
        # TERIMA KASIH
        # ==================================================
        elif any(x in message for x in [
            "terima kasih",
            "makasih",
            "thanks",
            "thx"
        ]):

            reply = """
Sama-sama 😊

Semoga informasi yang diberikan bermanfaat. Jika masih ada pertanyaan mengenai media sosial atau penggunaan sistem TrendReco, silakan tanyakan kembali.
"""

        # ==================================================
        # SIAPA KAMU
        # ==================================================
        elif any(x in message for x in [
            "siapa kamu",
            "kamu siapa",
            "apa itu trendreco assistant"
        ]):

            reply = """
Saya adalah TrendReco Assistant.

Saya bertugas membantu pengguna memahami sistem TrendReco serta memberikan informasi umum mengenai media sosial, tren digital, dan strategi konten.
"""

        # ==================================================
        # BANTUAN SISTEM
        # ==================================================
        elif any(x in message for x in [
            "cara menggunakan",
            "cara pakai",
            "bagaimana menggunakan",
            "menggunakan sistem",
            "bantuan"
        ]):

            reply = """
Cara menggunakan sistem TrendReco:

1. Masukkan kata kunci/topik yang diinginkan.
2. Pilih platform media sosial.
3. Pilih tujuan konten.
4. Klik tombol rekomendasi.
5. Sistem akan menampilkan ide konten beserta strategi dan analisis tren.

Jika ingin rekomendasi yang lebih spesifik, gunakan menu Rekomendasi Konten.
"""

        # ==================================================
        # MENU REKOMENDASI
        # ==================================================
        elif any(x in message for x in [
            "menu rekomendasi",
            "rekomendasi konten",
            "fitur rekomendasi"
        ]):

            reply = """
Menu Rekomendasi Konten digunakan untuk menghasilkan:

• Ide konten
• Judul konten
• Hook
• Caption
• Strategi konten
• Hashtag
• Analisis tren

Hasil rekomendasi dibuat berdasarkan tren online dan preferensi pengguna.
"""

        # ==================================================
        # TREN
        # ==================================================
        elif any(x in message for x in [
            "tren",
            "trend",
            "viral"
        ]):

            reply = """
Beberapa tren konten yang cukup populer saat ini antara lain:

• Artificial Intelligence (AI)
• Produktivitas
• Personal Branding
• Self Improvement
• Tutorial Singkat
• Daily Vlog
• Edukasi Karier
• Side Hustle
• Teknologi Digital

Untuk mengetahui tren spesifik sesuai topik Anda, gunakan menu Rekomendasi Konten.
"""

        # ==================================================
        # MEDIA SOSIAL
        # ==================================================
        elif "media sosial" in message:

            reply = """
Media sosial merupakan platform digital yang digunakan untuk membuat, membagikan, dan berinteraksi dengan konten.

Platform populer saat ini:

• TikTok
• Instagram
• YouTube
• Facebook
• X (Twitter)
• LinkedIn
"""

        # ==================================================
        # TIKTOK
        # ==================================================
        elif "tiktok" in message:

            reply = """
Faktor penting pada TikTok:

• Hook 3 detik pertama
• Watch Duration
• Retention Rate
• Engagement
• Konsistensi upload

Konten edukasi singkat, hiburan, dan tutorial biasanya memiliki performa yang baik di TikTok.
"""

        # ==================================================
        # INSTAGRAM
        # ==================================================
        elif "instagram" in message:

            reply = """
Instagram cenderung menonjolkan:

• Kualitas visual
• Konsistensi branding
• Engagement
• Estetika konten

Konten Reels, carousel edukasi, dan konten lifestyle cukup efektif di Instagram.
"""

        # ==================================================
        # YOUTUBE
        # ==================================================
        elif "youtube" in message:

            reply = """
YouTube Shorts lebih efektif jika:

• Memiliki storytelling yang jelas
• Menjaga retention audience
• Memberikan value yang kuat
• Menggunakan visual menarik

Konten edukasi, tutorial, dan storytelling memiliki potensi performa yang baik.
"""


        # ==================================================
        # JAM UPLOAD
        # ==================================================
        elif any(x in message for x in [
            "jam upload",
            "waktu upload",
            "upload jam berapa"
        ]):

            reply = """
            <div>

                <div class="flex items-center gap-2 mb-4">
                    <i class="fa-solid fa-clock text-blue-600"></i>
                    <b>Rekomendasi Waktu Upload</b>
                </div>

                <div class="space-y-3">

                    <div class="p-3 rounded-xl bg-slate-50 border">

                        <div class="font-semibold flex items-center gap-2">
                            <i class="fa-brands fa-tiktok"></i>
                            TikTok
                        </div>

                        <p class="text-sm mt-2">
                            11.00–13.00<br>
                            18.00–21.00
                        </p>

                    </div>

                    <div class="p-3 rounded-xl bg-slate-50 border">

                        <div class="font-semibold flex items-center gap-2">
                            <i class="fa-brands fa-instagram"></i>
                            Instagram
                        </div>

                        <p class="text-sm mt-2">
                            11.00–13.00<br>
                            18.00–20.00
                        </p>

                    </div>

                    <div class="p-3 rounded-xl bg-slate-50 border">

                        <div class="font-semibold flex items-center gap-2">
                            <i class="fa-brands fa-youtube"></i>
                            YouTube Shorts
                        </div>

                        <p class="text-sm mt-2">
                            17.00–21.00
                        </p>

                    </div>

                </div>

            </div>
            """

        # ==================================================
        # ENGAGEMENT
        # ==================================================
        elif "engagement" in message:

            reply = """
            <div>

                <div class="flex items-center gap-2 mb-4">
                    <i class="fa-solid fa-heart text-red-500"></i>
                    <b>Tips Meningkatkan Engagement</b>
                </div>

                <ul class="space-y-2">

                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i>Gunakan hook yang kuat</li>

                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i>Tambahkan Call To Action</li>

                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i>Ikuti tren terbaru</li>

                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i>Upload secara konsisten</li>

                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i>Balas komentar audience</li>

                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i>Gunakan visual yang menarik</li>

                </ul>

            </div>
            """

        # ==================================================
        # ALGORITMA
        # ==================================================
        elif "algoritma" in message:

            reply = """
Algoritma media sosial umumnya mempertimbangkan:

• Watch Duration
• Retention Rate
• Like
• Comment
• Share
• Save
• Relevansi topik
• Konsistensi upload
"""

        # ==================================================
        # GENERATOR
        # ==================================================
        elif any(x in message for x in [
            "caption",
            "judul",
            "hook",
            "strategi",
            "hashtag",
            "ide konten"
        ]):

            reply = """
Untuk menghasilkan:

• Ide Konten
• Judul
• Hook
• Caption
• Hashtag
• Strategi Konten

silakan gunakan menu Rekomendasi Konten agar hasil yang diperoleh sesuai dengan tren dan preferensi Anda.
        """
        # ==================================================
        # CUSTOMER SERVICE
        # ==================================================
        elif any(x in message for x in [
            "customer service",
            "cs",
            "admin",
            "kontak",
            "bantuan teknis",
            "lapor",
            "error",
            "bug",
            "masalah",
            "tidak bisa",
            "gagal",
            "kendala",
            "bantuan admin"
        ]):

            reply = """
            <div class="space-y-4">

                <div class="flex items-center gap-2 text-amber-600 font-bold">
                    <i class="fa-solid fa-headset"></i>
                    Customer Service TrendReco
                </div>

                <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
                    Jika Anda mengalami kendala saat menggunakan sistem,
                    silakan hubungi administrator.
                </div>

                <div>
                    <div class="font-semibold mb-2">
                        Kontak Administrator
                    </div>

                    <a href="mailto:admintrendreco@gmail.com"
                    class="text-blue-600 hover:underline">

                        <i class="fa-solid fa-envelope mr-2"></i>
                        admintrendreco@gmail.com

                    </a>
                </div>

                <div>

                    <div class="font-semibold mb-2">
                        Informasi yang perlu disertakan:
                    </div>

                    <ul class="space-y-2">
                        <li>
                            <i class="fa-solid fa-circle-dot mr-2 text-blue-500"></i>
                            Halaman yang bermasalah
                        </li>

                        <li>
                            <i class="fa-solid fa-circle-dot mr-2 text-blue-500"></i>
                            Deskripsi kendala
                        </li>

                        <li>
                            <i class="fa-solid fa-circle-dot mr-2 text-blue-500"></i>
                            Screenshot jika tersedia
                        </li>
                    </ul>

                </div>

            </div>
            """
        # ==================================================
        # DEFAULT
        # ==================================================
        else:

            reply = """
Maaf, saya belum memahami pertanyaan tersebut.

Saya dapat membantu menjawab pertanyaan mengenai:

• Media sosial
• Tren konten
• Engagement
• Algoritma platform
• TikTok, Instagram, dan YouTube
• Strategi upload
• Cara menggunakan sistem

Untuk menghasilkan ide konten, silakan gunakan menu Rekomendasi Konten.
"""

        return jsonify({"reply": reply})