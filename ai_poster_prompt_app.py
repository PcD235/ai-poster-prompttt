import streamlit as st
import openai

from openai import OpenAI

st.title("🎬 AI Tạo Prompt Poster Phim Theo Tên")

api_key = st.text_input("🔑 Nhập OpenAI API Key của bạn", type="password")
movie_name = st.text_input("🎞️ Nhập tên phim:")

system_prompt = """
Bạn là một chuyên gia thiết kế poster phim. Dưới đây là cấu trúc bạn phải dùng để tạo prompt hình ảnh AI.

Cấu trúc prompt:
Poster Creation: Top half: [Nam chính (Diễn viên)], [Nữ chính (Diễn viên)] in seductive pose, with [Nhân vật phụ 1 (Diễn viên)], [Nhân vật phụ 2 (Diễn viên)], [vật phẩm chính], surreal style, cinematic lighting, cool gray tones, natural skin texture, soft shadows, realistic hair, 8K, sharp realistic skin texture, [yếu tố nền phụ liên quan phim] in the background, Middle strip: swirling fog with [vật phẩm phụ] in the middle, [dấu vết phù hợp với phim], [yếu tố nổi bật nội dung phim] behind, Bottom half: [bối cảnh chính] with [khu vực hoặc chi tiết đặc trưng], realistic fog, rising mist, translucent gray reflective ground, natural stone, The title "[Tên phim]" in [phong cách font + màu] font at the middle, surreal [thể loại] setting.
"""

if api_key and movie_name:
    client = OpenAI(api_key=api_key)

    with st.spinner("🧠 Đang tạo prompt..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Tên phim: {movie_name}\nPrompt:"}
                ],
                temperature=0.9,
                max_tokens=500
            )
            result = response.choices[0].message.content
            st.text_area("📄 Prompt được tạo", result, height=400)
        except Exception as e:
            st.error(f"❌ Lỗi: {e}")
elif movie_name and not api_key:
    st.warning("🔐 Vui lòng nhập API Key để tạo prompt.")
