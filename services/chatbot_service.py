from services.generator import (
    generate_title,
    generate_hooks,
    generate_caption,
    generate_strategy
)


def get_chatbot_response(message):

    msg = message.lower()

    topic = "AI untuk Mahasiswa"

    category = "Edukasi & Tutorial"

    goal = "edukasi"

    platform = "tiktok"

    # ===================
    # Hook
    # ===================
    if "hook" in msg:

        return generate_hooks(
            topic,
            category,
            goal
        )

    # ===================
    # Caption
    # ===================
    elif "caption" in msg:

        return generate_caption(
            topic,
            goal,
            category,
            platform
        )

    # ===================
    # Judul
    # ===================
    elif "judul" in msg:

        return generate_title(
            topic,
            goal,
            category
        )

    # ===================
    # Strategi
    # ===================
    elif "strategi" in msg:

        return generate_strategy(
            category,
            goal,
            platform
        )

    # ===================
    # Explainability
    # ===================
    elif "kenapa" in msg:

        return (
            f"Topik {topic} direkomendasikan "
            "karena memiliki tingkat kemiripan "
            "yang tinggi dengan preferensi pengguna "
            "dan sedang mengalami peningkatan tren."
        )

    return (
        "Halo 👋 Saya TrendReco Assistant.\n\n"
        "Saya dapat membantu:\n"
        "- Membuat judul\n"
        "- Membuat hook\n"
        "- Membuat caption\n"
        "- Memberikan strategi konten\n"
        "- Menjelaskan hasil rekomendasi"
    )