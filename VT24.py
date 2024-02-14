import streamlit as st

def main():
    # Biến để theo dõi trạng thái hiển thị
    display_video = False

    # Thêm CSS để thay đổi màu nền và màu chữ
    st.markdown(
        """
        <style>
            [data-testid="stAppViewContainer"] > .main {
                background-image: url("https://minhtuanmobile.com/uploads/blog/tinh-be-binh-voi-bo-hinh-valentine-sieu-lang-man-230202111215.jpg");
                background-size: cover;
            }
            .stButton>button {
                background-color: white;
                color: #FF1D1D;
                transition: 0.3s;
            }
            .stButton>button:hover {
                opacity: 0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown( 
        """
        <style>
        .centered {   
            display: flex;
            justify-content: center;
            align-items: center;
            height: 8vh;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Hiển thị nút và xử lý sự kiện khi nút được nhấn
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        bt_video = st.button('NHẤP CHUỘT VÀO')
    
    if bt_video:
        display_video = True

    # Nếu trạng thái hiển thị video được kích hoạt, ẩn nội dung hiện tại và hiển thị video
    if display_video:
        st.markdown(
        """
        <style>
            [data-testid="stAppViewContainer"] > .main {
                background-image: url("https://i.pinimg.com/originals/c3/aa/cd/c3aacdb10d1c0d550b7fa08b6d0bddb1.jpg");
                background-size: cover;
            }
            .stButton>button {
                background-color: white;
                color: #FF1D1D;
                transition: 999999999s;
            }
            .stButton>button:hover {
                opacity: 0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
        # Tạo đoạn mã JavaScript để ẩn nội dung
        hide_content_script = """
        <script>
            document.getElementById("content").style.display = "none";
        </script>
        """

        # Thực thi đoạn mã JavaScript
        st.markdown(hide_content_script, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.markdown(
                """
                <div class="centered">
                    <h4 style="color: white;">Valentine vui vẻ nha emiu của anh
                    Anh cảm ơn em suốt thời gian vẫn luôn bên anh và mong sau này vẫn vậy. Anh yêu em ❤
                    Trong thời gian tới anh phải làm đồ án tốt nghiệp cho đàng hoàng lại chắc sẽ ít thời gian bên em như bây giờ nhưng anh vẫn sẽ cố gắng để có thể bên em nhiều nhất có thể. Còn bây giờ thì chúng ta cùng đón Valentine vui vẻ nha.
                    Huỳnh Anh Kiệt yêu Dương Thị Diệu Thanh ❤</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            
            st.video("video.mp4", start_time=0)  # Bắt đầu video từ thời điểm 0
  
if __name__ == "__main__":
    main()
