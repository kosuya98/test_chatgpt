
import streamlit as st
import openai

# 챗지피티에게 글요약을 요청하는 함수
def askGPT(prompt, api_key):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    final_response = response.choices[0].message.content
    return final_response

## main 함수
def main():
    st.set_page_config(page_title="광고 문구 생성 프로그램")

    # session_state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    with st.sidebar:
        open_api_key = st.text_input(label='OPEN API 키', placeholder='Enter your api key')

        if open_api_key:
            st.session_state["OPENAI_API"] = open_api_key
        st.markdown('---')

    st.header(":mega:광고 문구 생성 프로그램:mega:")
    st.markdown('---')

    text = st.text_area("광고로 활용할 텍스트를 입력하세요")
    if st.button("생성"):
        prompt = f'''
        **광고 문구 생성 요청** :
    - 당신은 광고 문구를 생성하는 전문 어시스턴트입니다.
    - 주어진 텍스트를 기반으로 한 **한국어 광고 문구**를 생성하는 것이 당신의 임무입니다.
    - 생성된 광고 문구는 간결하고 효과적이어야 합니다.
    -text : {text}
    '''
        st.success(askGPT(prompt, st.session_state["OPENAI_API"]))

if __name__ == "__main__":
    main()
