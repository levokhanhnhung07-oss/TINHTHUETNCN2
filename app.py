import streamlit as st

# ==========================
# CẤU HÌNH TRANG
# ==========================
st.set_page_config(
    page_title="Tính Thuế Thu Nhập Cá Nhân",
    page_icon="💰",
    layout="wide"
)

# ==========================
# LOGO
# ==========================
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("LOGO.JPG", width=250)

# ==========================
# TIÊU ĐỀ
# ==========================
st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN")
st.markdown("---")

# ==========================
# NHẬP DỮ LIỆU
# ==========================
st.header("📋 Nhập thông tin")

gross = st.number_input(
    "💵 Thu nhập Gross (VNĐ)",
    min_value=0,
    value=20_000_000,
    step=100_000
)

dependents = st.number_input(
    "👨‍👩‍👧‍👦 Số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)

calculate = st.button("🧮 Tính thuế")

# ==========================
# HÀM TÍNH THUẾ
# ==========================
def personal_income_tax(income):

    tax = 0

    brackets = [
        (5000000, 0.05),
        (5000000, 0.10),
        (8000000, 0.15),
        (14000000, 0.20),
        (20000000, 0.25),
        (28000000, 0.30),
        (float("inf"), 0.35)
    ]

    remain = income

    for limit, rate in brackets:

        if remain <= 0:
            break

        taxable = min(remain, limit)

        tax += taxable * rate

        remain -= taxable

    return tax

# ==========================
# TÍNH TOÁN
# ==========================
if calculate:

    insurance = gross * 0.105

    personal_deduction = 11_000_000

    dependent_deduction = dependents * 4_400_000

    taxable_income = max(
        gross
        - insurance
        - personal_deduction
        - dependent_deduction,
        0
    )

    tax = personal_income_tax(taxable_income)

    net = gross - insurance - tax

    st.markdown("---")
    st.header("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🛡️ Bảo hiểm",
            f"{insurance:,.0f} VNĐ"
        )

        st.metric(
            "📄 Thu nhập tính thuế",
            f"{taxable_income:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "💰 Thuế phải nộp",
            f"{tax:,.0f} VNĐ"
        )

        st.metric(
            "🏦 Thu nhập thực nhận",
            f"{net:,.0f} VNĐ"
        )

    with st.expander("📑 Xem chi tiết phép tính"):

        st.write(f"**Thu nhập Gross:** {gross:,.0f} VNĐ")

        st.write(f"**Bảo hiểm (10.5%):** {insurance:,.0f} VNĐ")

        st.write(f"**Giảm trừ bản thân:** {personal_deduction:,.0f} VNĐ")

        st.write(f"**Giảm trừ người phụ thuộc:** {dependent_deduction:,.0f} VNĐ")

        st.write(f"**Thu nhập tính thuế:** {taxable_income:,.0f} VNĐ")

        st.write(f"**Thuế TNCN:** {tax:,.0f} VNĐ")

        st.write(f"**Thu nhập thực nhận:** {net:,.0f} VNĐ")

        st.success("✅ Tính thuế thành công!")

else:

    st.info("👆 Vui lòng nhập thông tin và nhấn **Tính thuế**.")
