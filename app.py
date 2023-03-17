import streamlit as st
import sklearn
model = pickle.load(open("model.pickle", "rb"))
st.title('Revenue Prediction')
temp = st.number_input('Input Temperature')
temp = np.array([temp]).reshape(-1,1)
results = model.predict(temp)[0]
if st.button("Predict"):
  st.write("Revenue Prediction")
  st.write(results)
