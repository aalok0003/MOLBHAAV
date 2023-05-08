import streamlit as st

#st.text('e.g mL- Oil & Milk')
#st.text('e.g g- Vegetable, Paneer, Pulses, Dry Fruits e.t.c.')
#st.text('Remember 1 Kg = 1000 g & 1 L = 1000 mL')
#st.text("e.g Bananas")
#st.text("Remember 1 Dozen is 12 Units")



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.talentedge.co.uk/wp-content/uploads/2020/10/AdobeStock_254445293-scaled.jpeg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.title('मोल भाव')
list_of_items=['Unit','ग्राम/मिलीलीटर']
item_type = st.selectbox("समान की इकाई",list_of_items)

quantity=st.number_input(f'कितना है ({item_type} में) ?',min_value=1)
value=st.number_input('कितने रूपे का है ?',min_value=1)

objective= st.radio(
    "कोई एक विकल्प चुनें",
    ('कितना खरीदना है यह पता है ','कितने रुपये का खरीदना है यह पता है ','जानना चाहते हैं कौन सा इंटरनेट पैक सस्ता है ?'))

if objective=='कितने रुपये का खरीदना है यह पता है ':
    if item_type=='ग्राम/मिलीलीटर':

        price=st.number_input('कितने रुपये का खरीदना है ?')
        kitna_milega=price/(value/quantity)
        st.write(kitna_milega)
        st.write(item_type)
    elif item_type=='Unit':

        price=st.number_input('कितने रुपये का खरीदना है ?')
        kitna_milega=price/(value/quantity)
        st.write(kitna_milega)
        st.write(item_type)

elif objective=='कितना खरीदना है यह पता है ':
    if item_type=='ग्राम/मिलीलीटर':
        kitna_lena_hai=st.number_input(f"कितना खरीदना है ({item_type} में)?",min_value=1)
        itne_ka_milega=(value/quantity)*kitna_lena_hai
        st.write(itne_ka_milega)
    if item_type=='Unit':
        kitna_lena_hai=st.number_input(f"कितना खरीदना है ({item_type} में)?",min_value=1)
        itne_ka_milega=(value/quantity)*kitna_lena_hai
        st.write(itne_ka_milega)

elif objective=='जानना चाहते हैं कौन सा इंटरनेट पैक सस्ता है ?':
    col1,col2=st.columns([1,1])
    with col1:
        kitna_GB=st.number_input('कुल कितने जीबी (GB)',min_value=0.5, key='kitna_GB_1')
        kitne_din=st.number_input('पैक की वैधता कितने दिन की है',min_value=1, key='kitne_din_1')
        kitne_ka=st.number_input('पैक की कीमत क्या है',min_value=1, key='kitne_ka_1')
        cost_per_day=kitne_ka/kitne_din
        net_per_day=kitna_GB/kitne_din
        st.write("आपके एक दिन का खर्च है",cost_per_day)
        st.write('इंटरनेट प्रतिदिन',net_per_day)
        cost_per_GB=kitne_ka/kitna_GB
        st.write('1 GB इंटरनेट की लागत',cost_per_GB)
    
    with col2:
        kitna_GB_second=st.number_input('कुल कितने जीबी (GB)',min_value=0.5, key='kitna_GB_2')
        kitne_din_second=st.number_input('पैक की वैधता कितने दिन की है',min_value=1, key='kitne_din_2')
        kitne_ka_second=st.number_input('पैक की कीमत क्या है',min_value=1, key='kitne_ka_2')
        cost_per_day_second = kitne_ka_second/kitne_din_second
        net_per_day_second = kitna_GB_second/kitne_din_second
        cost_per_GB_second = kitne_ka_second/kitna_GB_second
        st.write("आपके एक दिन का खर्च है",cost_per_day_second)
        st.write('इंटरनेट प्रतिदिन',net_per_day_second)
        st.write('1 GB इंटरनेट की लागत',cost_per_GB_second)
