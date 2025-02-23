import streamlit as st

# タイトル
st.title("Simple Calculator")

# セクションで計算の入力を整理
st.subheader("Enter your numbers:")

# ユーザーからの入力を受け取る
num1 = st.number_input("First number", value=0.0, format="%.2f")
num2 = st.number_input("Second number", value=0.0, format="%.2f")

# 演算方法の選択
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# ボタンを押して計算を実行
if st.button("Calculate"):
    # 計算処理
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    # 結果の表示
    st.subheader("Result:")
    st.write(f"Result: {result}")

# 追加でスタイルを整えるためにCSSを使用
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        height: 3em;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSelectbox>div>div>div>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        height: 3em;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

