import streamlit as st
import math

# 빛의 속도 (m/s)
c = 299792458.0

# 시간 변화율 계산 함수
def calc_time_dilation(v):
    # 감마값 계산
    print(c)
    print(v)
    print(1 - (v / c) ** 2)
    gamma = 1.0 / math.sqrt(1 - (v / c) ** 2)
    # 시간 변화율 계산
    time_dilation = gamma
    return time_dilation

# LaTeX 수식
latex_str = r"T = t\sqrt{1 - \frac{v^2}{c^2}}"

st.header("상대성 이론 계산기")

# 빛의 상대속도를 입력받는 슬라이더
rel_c = st.slider("빛에 대한 상대속도", 0.0, 0.99999999, 0.0, 0.00001)

# 시간 변화율 계산
time_dilation = calc_time_dilation(rel_c*c)

# 출력
st.latex(latex_str)

st.markdown(f"속도가 **{rel_c*c:.1f} m/s ({rel_c} C)** 일 때, 시간은 지구에서보다 **{time_dilation:.5f}** 배 느리게 흐릅니다.")
