import streamlit as st
# st.set_page_config(page_title='Do Uong',page_icon=':smile',layout = 'wide')
# st.title('Cua Hang Do Uong')
# st.write('Lap trinh web = streamlit')
# with st.expander('Menu'):
#   st.write('Tra sua')
#   st.write('Sinh to')
#   st.write('Ca phe')

# c1,c2 = st.columns(2)
# with c1:
#   st.header('a cat')
#   st.write('con mèo')
# with c2:
#   st.header('a dog')
#   st.write('con chó')

# st.sidebar.write('1.Lời nói đầu')
# with st.sidebar:
#   st.write('2.Mục lục')


# st.set_page_config('Trắc Nghiệm Tính Cách',page_icon='❓',layout='wide')
# st.title('Hãy chọn 1 con vật mà bạn yêu thích')
# c1,c2,c3,c4,c5 = st.columns(5)
# personality = {'Con mèo': 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, bạn khao khát được đi nghỉ.','Con chó': 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề xảy ra.','Con sư tử': 'Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng.','Con ngựa': 'Có điều gì đó đang hạn chế sự tự do của bạn.','Thiên nga': 'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé.'}
# with c1:
#   b1 = st.button('Con mèo')
# with c2:
#   b2 = st.button('Con chó')
# with c3:
#   b3 = st.button('Con sư tử')
# with c4:
#   b4 = st.button('Con ngựa')
# with c5:
#   b5 = st.button('Thiên nga')

# if b1:
#   with st.expander('Con mèo'):
#     st.write(personality['Con mèo'])
# if b2:
#   with st.expander('Con chó'):
#     st.write(personality['Con chó'])
# if b3:
#   with st.expander('Con sư tử'):
#     st.write(personality['Con sư tử'])
# if b4:
#   with st.expander('Con ngựa'):
#     st.write(personality['Con ngựa'])
# if b5:
#   with st.expander('Thiên nga'):
#     st.write(personality['Thiên nga'])

# with st.sidebar:
#   st.title('Trắc nghiệm tính cách')
#   if b1:
#     st.write('Bạn đã chọn con mèo')
#   if b2:
#     st.write('Bạn đã chọn con chó')
#   if b3:
#     st.write('Bạn đã chọn con sư tử')
#   if b4:
#     st.write('Bạn đã chọn con ngựa')
#   if b5:
#     st.write('Bạn đã chọn con thiên nga')




st.set_page_config('Trắc Nghiệm Tính Cách',page_icon='❓',layout='wide')
st.title('Hãy chọn 1 người bạn mà bạn yêu thích')
c1,c2,c3,c4,c5 = st.columns(5)
personality = {'Nguyên': '26/6, An Lâm',
               'Bảo': '26/3, Nam Trung',
               'Huy': '1/6, Nam Chính',
               'Long': '8/11, Thanh Quang',
               'Vũ': '13/11, Nam Tân'}
with c1:
  b1 = st.button('Nguyên')
with c2:
  b2 = st.button('Bảo')
with c3:
  b3 = st.button('Huy')
with c4:
  b4 = st.button('Long')
with c5:
  b5 = st.button('Vũ')

if b1:
  with st.expander('Nguyên'):
    st.write(personality['Nguyên'])
if b2:
  with st.expander('Bảo'):
    st.write(personality['Bảo'])
if b3:
  with st.expander('Huy'):
    st.write(personality['Huy'])
if b4:
  with st.expander('Long'):
    st.write(personality['Long'])
if b5:
  with st.expander('Vũ'):
    st.write(personality['Vũ'])

with st.sidebar:
  st.title('Trắc nghiệm tính cách')
  if b1:
    st.write('Bạn đã chọn Nguyên')
  if b2:
    st.write('Bạn đã chọn Bảo')
  if b3:
    st.write('Bạn đã chọn Huy')
  if b4:
    st.write('Bạn đã chọn Long')
  if b5:
    st.write('Bạn đã chọn Vũ')